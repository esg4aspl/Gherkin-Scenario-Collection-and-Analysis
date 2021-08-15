import argparse
import json

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from add_read_me_table import add_table_to_file
from repo_metadata_scraper import MetadataSpider
from repo_name_scraper import RepoNameSearchSpider

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_file', help='data file name', required=True)
    parser.add_argument('--discover', action='store_true', help='discover new repositories')
    parser.add_argument('--collect_metadata', help='scrape metadata for all or new repos', choices=['all', 'new'])
    parser.add_argument('-o', '--output_file', help='output file name')
    args = parser.parse_args()

    process = CrawlerProcess()

    if args.discover:
        f = open(args.data_file, 'a+')
        process.crawl(RepoNameSearchSpider, output_file=f)
        process.start()
        f.close()

    if args.collect_metadata is not None:
        urls = []
        results = []
        data = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
        # connect callback to dispatcher to get crawler results after all urls are consumed
        dispatcher.connect(crawler_results, signal=signals.item_passed)
        # read repo names from data file as required
        with open(args.data_file) as f:
            for line in f:
                jl = (json.loads(line))
                data.append(jl)
                # if collect_metadata is all, scrape all. Else scrape the ones that are
                # not scraped before (i.e. does not have a 'url')
                if 'name' in jl and (args.collect_metadata == 'all' or 'url' not in jl):
                    urls.append('https://github.com/' + jl['name'])

        print('Running metadata scraper for', len(urls), 'urls')
        process.crawl(MetadataSpider, in_urls=urls)
        process.start()
        # after scraping ends, merge existing and new results
        # below section has O(n*n) complexity. If one of the DS are switched to a map, can be reduced to O(n)
        # at the current n (~500), it does not make a great difference
        for data_index in range(len(data)):
            for result in results:
                if data[data_index]['name'] == result['name']:
                    data[data_index] = result
                    break

        # overwrite data file with the new results
        with open(args.data_file, 'w') as f:
            f.seek(0)
            for d in data:
                f.write(json.dumps(d) + '\n')
            f.truncate()

    if args.output_file is not None:
        add_table_to_file(args.data_file, args.output_file)
