import scrapy
import product

class Sp1Spider(scrapy.Spider):
    name = 'sp1'
    start_urls = ['https://www.tokstok.com.br/luminaria-mesa-preto-preto-arkit/p']

    def parse(self, response):
        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        product_name=response.xpath("//span[@class='vtex-store-components-3-x-productBrand ']/text()").extract_first()
        product_price=response.xpath("//span[@class='tokstoksponsorio-pdp-components-0-x-sellingPriceValue']/text()").extract_first()
        yield{'nome': product_name,
              'preco': product_price}
        '''
        SET_SELECTOR = '.bg-base'
        for preco in response.css(SET_SELECTOR):
            print("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            PRICE_SELECTOR = '.tokstoksponsorio-pdp-components-0-x-currencyInteger .tokstoksponsorio-pdp-components-0-x-currencyDecimal .tokstoksponsorio-pdp-components-0-x-currencyFraction ::text'
            yield {
                'preco': preco.css(PRICE_SELECTOR).extract_first(),
            }'''

