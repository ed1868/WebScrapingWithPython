# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        header = response.xpath('//h1/a/text()').extract()
        tags =response.xpath('//*[@class="tag-item"]/a/text()')
        
        yield{
            'Header' : header,
            'Tags' : tags 
        }