# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    start_urls = [
        'https://www.amazon.in/s?bbn=4149779031&rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149751031%2Cn%3A4149790031%2Cn%3A4149779031%2Cp_n_publication_date%3A2684819031&dc&fst=as%3Aoff&qid=1586597168&rnid=2684818031&ref=lp_4149779031_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        # multiple class so .css('::text')
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        # one class so ::text directly
        product_price = response.css('.a-price-whole::text').extract()
        product_imagelink = response.css('.s-image-fixed-height .s-image').css('::attr(src)').extract()

        items = AmazontutorialItem(product_name=product_name, product_author=product_author,
                                   product_price=product_price, product_imagelink=product_imagelink)

        yield items
