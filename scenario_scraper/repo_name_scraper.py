import json
import time
import scrapy

from scrapy.crawler import CrawlerProcess


class RepoNameSearchSpider(scrapy.Spider):
    name = 'repo_names'
    uniqueNames = {}
    max_pages = 300  # limit the max crawled page count to avoid infinite loop on a parsing error
    page = 0

    def __init__(self, output_file=None, **kwargs):
        super().__init__(**kwargs)
        self.output_file = output_file

    def start_requests(self):
        urls = [
            'https://github.com/search?q=extension%3Afeature+path%3A%2Ffeatures&type=Code&ref=advsearch&l=&l=',
            'https://github.com/search?l=&o=desc&q=extension%3Afeature+path%3A%2Ffeatures&s=indexed&type=Code',
        ]
        for url in urls:
            # github's search page requires a login.
            # visit the url above, open dev console->Network and copy the cookie in request headers to use that session
            yield scrapy.Request(url=url, cookies={'user_session': '!!!!!!FILL ME!!!!!!',
                                                   'logged_in': 'yes',
                                                   'dotcom_user': '!!!!!!FILL ME!!!!!!',
                                                   '_gh_sess': '!!!!!!FILL ME!!!!!!'
                                                   }, callback=self.parse)

    def parse(self, response):

        for repoSelector in response.css('a.Link--secondary'):
            repo_name = repoSelector.xpath('text()').get().strip(),

            # TODO: these operations are not re-entrant. Not sure how crawler processes multiple start_urls
            # if they are truly parallel, below critical section requires an execution barrier
            if repo_name not in self.uniqueNames:
                result = {
                    'repoName': repo_name[0],
                }
                yield result
                self.output_file.write(json.dumps(result) + '\n')
                self.output_file.flush()
                self.uniqueNames[repo_name] = True
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
