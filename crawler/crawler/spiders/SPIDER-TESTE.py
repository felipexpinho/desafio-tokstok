import scrapy


class Sp2Spider(scrapy.Spider):
    name = 'sp2'
    start_urls = ['https://www.cloudsigma.com/blog']
 
    def parse(self, response):
        SET_SELECTOR = '.post'
        for tutorial in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.entry-wrap .entry-header > h2 > a ::text'
            yield {
                'title': tutorial.css(NAME_SELECTOR).extract_first(),
            }
