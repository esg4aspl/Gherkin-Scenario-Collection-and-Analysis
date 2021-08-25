import json
import time
import scrapy

from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from threading import Lock


class RepoNameSearchSpider(scrapy.Spider):
    name = 'repo_names'
    uniqueNames = {}
    max_pages = 600  # limit the max crawled page count to avoid infinite loop on a parsing error
    page = 0

    def __init__(self, output_file=None, **kwargs):
        super().__init__(**kwargs)
        self.lock = Lock()
        self.output_file = output_file
        self.output_file.seek(0)
        for line in self.output_file.readlines():
            jl = json.loads(line)
            self.uniqueNames[jl['name']] = True

    def start_requests(self):
        urls = [
            # feature/*.feature best match
            'https://github.com/search?q=extension%3Afeature+path%3A%2Ffeatures&type=Code&ref=advsearch&l=&l=',
            # feature/*.feature most recently indexed
            'https://github.com/search?l=&o=desc&q=extension%3Afeature+path%3A%2Ffeatures&s=indexed&type=Code',
            # feature/*.feature lesth recently indexed
            'https://github.com/search?l=&o=asc&q=extension%3Afeature+path%3A%2Ffeatures&s=indexed&type=Code',
            # *.feature best match
            'https://github.com/search?q=extension%3Afeature+path%3A%2Ffeatures+extension%3Afeature&type=Code&ref=advsearch&l=&l=',
            # *.feature most recently indexed
            'https://github.com/search?l=&o=desc&q=extension%3Afeature+path%3A%2Ffeatures+extension%3Afeature&s=indexed&type=Code',
            # *.feature least recently indexed
            'https://github.com/search?l=&o=asc&q=extension%3Afeature+path%3A%2Ffeatures+extension%3Afeature&s=indexed&type=Code'
        ]
        credfile = open('credentials.json', 'r')
        creds = json.load(credfile)
        for url in urls:
            # github's search page requires a login.
            # visit the url above, open dev console->Network and copy the cookie in request headers to use that session
            yield scrapy.Request(url=url, cookies=creds, callback=self.parse)

    def parse(self, response):
        if response.css('title::text').get().startswith('Sign in to GitHub'):
            raise CloseSpider('Search page has redirected to user login \n Follow the instructions given in'
            'https://github.com/esg4aspl/Gherkin-Scenario-Collection-and-Analysis#setting-up-credentials-for-the-search-page')

        for repoSelector in response.css('a.Link--secondary'):
            repo_name = repoSelector.xpath('text()').get().strip(),
            repo_name = repo_name[0]

            # these operations are not re-entrant. need to protect uniqueNames dict
            self.lock.acquire()
            if repo_name not in self.uniqueNames:
                result = {
                    'name': repo_name,
                }
                yield result
                self.output_file.write(json.dumps(result) + '\n')
                self.output_file.flush()
                self.uniqueNames[repo_name] = True
            self.lock.release()
            # end critical section

        next_page_anchor = response.css('a.next_page')
        if 'href' in next_page_anchor.attrib:
            next_page = next_page_anchor.attrib['href']
        else:
            next_page = None
        # debug outputs, not written to file
        yield {
            'page': self.page,
            'next': next_page,
            'max': self.max_pages,
        }

        if next_page is not None and self.max_pages > self.page:
            time.sleep(15)  # otherwise gives 429:TooManyReqs
            next_page = response.urljoin(next_page)
            self.page = self.page + 1
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            yield {
                'pageEndAt': self.page,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    f = open('repo_names_.jl', 'a')
    process.crawl(RepoNameSearchSpider, output_file=f)
    process.start()
