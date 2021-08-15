import argparse

from scrapy.crawler import CrawlerProcess
from repo_name_scraper import RepoNameSearchSpider

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', help='output file name default:README.md', default='README.md')
    parser.add_argument('-d', '--data_file', help='data file name', required=True)
    parser.add_argument('--discover', action='store_true', help='discover new repositories')
    args = parser.parse_args()

    process = CrawlerProcess()

    if args.discover:
        f = open(args.data_file, 'a+')
        process.crawl(RepoNameSearchSpider, output_file=f)
        process.start()

    print('UMUT:done')
