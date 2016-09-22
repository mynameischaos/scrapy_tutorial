#!/usr/bin/python

import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
     ]

#    def parse(self, response):
#        filename = 'quotes-' + response.url.split("/")[-2] + '.html'
#        with open(filename,  'wb') as f:
#            f.write(response.body)

#    def parse(self, response):
#        for quote in response.xpath('//div[@class="quote"]'):
#            text = quote.xpath('span[@class="text"]/text()').extract_first()
#            author = quote.xpath('span/small/text()').extract_first()
#            print author, text
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
           item = QuoteItem()
           item['text'] = quote.xpath('span[@class="text"]/text()').extract_first()
           item['author'] = quote.xpath('span/small/text()').extract_first()
           yield item
        next_page = quote.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
