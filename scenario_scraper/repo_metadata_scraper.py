import json
import time
from datetime import datetime, timezone
from scrapy.signalmanager import dispatcher
from scrapy import signals

import scrapy
from scrapy.crawler import CrawlerProcess
from gherkin_parse_util import get_language_from_feature


class MetadataSpider(scrapy.Spider):
    name = 'quotes'
    uniqueNames = {}
    max_pages = 300
    page = 0
    handle_httpstatus_list = [404]

    def __init__(self, in_urls=None, **kwargs):
        super().__init__(**kwargs)
        if in_urls is None:
            in_urls = []
        self.urls = in_urls

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parseSingleRawFeature(self, response):
        feature_body = response.xpath('//p/text()').get()
        item = response.meta['item']
        item['gherkinLang'] = get_language_from_feature(feature_body)
        yield item

    def parse_gherkin_search(self, response):
        item = response.meta['item']
        item['featureCount'] = response.xpath('//span[@data-search-type="Code"]/text()').get()
        url_to_first_feature = response.xpath('//div[@class="f4 text-normal"]').xpath('a')[0].attrib['href']
        # get the raw page
        url_to_first_feature = 'https://raw.githubusercontent.com' + url_to_first_feature
        url_to_first_feature = url_to_first_feature.replace('/blob', '')
        feature_page_req = scrapy.Request(url_to_first_feature, callback=self.parseSingleRawFeature)
        feature_page_req.meta['item'] = item
        yield feature_page_req

    def parse(self, response):

        results = {'name': response.url.split('/', 3)[-1], 'url': response.url}
        # if repo is not reachable, mark it as such and return
        if response.status == 404:
            results['is_reachable'] = False
            yield results
            return

        for counterSelector in response.css('a.Link--primary.no-underline'):
            counter_name = counterSelector.xpath('text()').get().strip(),
            counter_name = counter_name[0]
            if len(counter_name) != 0 and 'title' in counterSelector.css('span.Counter').attrib:
                results[counter_name] = counterSelector.css('span.Counter').attrib['title']

        langs = {}
        for langStatSelector in response.css('li.d-inline'):
            lang_name = langStatSelector.css('span::text')[0].get().strip()
            lang_ratio = langStatSelector.css('span::text')[1].get().strip()
            if lang_name:
                langs[lang_name] = lang_ratio
        results['languages'] = langs

        licenseSelector = response.xpath('//svg[@class="octicon octicon-law mr-2"]/..')
        sw_license = ''
        for licenseTextSelector in licenseSelector.xpath('text()'):
            sw_license = sw_license + licenseTextSelector.get().strip()
        results['license'] = sw_license
        if 'href' in licenseSelector.attrib:
            results['licenseLink'] = licenseSelector.attrib['href']

        results['scrapedAt'] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")

        search_gherkin_url = response.url + '/search?l=Gherkin'
        search_page_req = scrapy.Request(search_gherkin_url, callback=self.parse_gherkin_search)
        search_page_req.meta['item'] = results

        # to prevent TooManyRequests Error
        time.sleep(5)

        yield search_page_req


def crawler_results(signal, sender, item, response, spider):
    results.append(item)


if __name__ == "__main__":
    process = CrawlerProcess()
    urls = []
    results = []

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    with open('repo_names.jl') as f:
        for line in f:
            jl = (json.loads(line))
            if 'repoName' in jl:
                urls.append('https://github.com/' + jl['repoName'])
    output_file = open('metadata_output.jl', 'a')
    process.crawl(MetadataSpider, in_urls=urls)
    process.start()
    print(results)
    for result in results:
        output_file.write(json.dumps(result) + '\n')


