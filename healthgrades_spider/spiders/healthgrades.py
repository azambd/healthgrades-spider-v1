# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import HealthgradesSpiderItem

#Header For Sleep Timer
from time import sleep
import random

sleep(random.randrange(1,3))

class HealthgradesSpider(CrawlSpider):
    name = 'healthgrades'
    allowed_domains = ['healthgrades.com']

    start_urls = ['http://healthgrades.com/']

    rules = (
        Rule(
            LinkExtractor(
                # allow= (r'physician/\S+',), #https://www.healthgrades.com/physician/dr-richard-pearce-2dmnh/comments?currentPage=2
                allow = (r'physician/.*-[0-9a-z]*',), #https://www.healthgrades.com/physician/dr-james-kennedy-263bh
                unique=True,
            ), 
            callback='parse_item', 
            follow=True
        ),
    )

    def parse_item(self, response):
        
        item = HealthgradesSpiderItem()

        item['name'] = response.xpath('//div[@class="provider-name"]/h1/text()').extract()
        # for names in item['name']:
        #     if names == '':
        #         continue
        #     else:
        #         item['name'] = response.xpath('//div[@class="provider-name"]/h1/text()').extract_first()

        item['link'] = response.url
        item['speciality'] = response.xpath('//div[@class="provider-speciality"]/span/text()').extract_first()
        item['gender'] = response.xpath('//div[@class="provider-gender"]/span/text()').extract_first()
        item['street_address'] = response.xpath('//p[@itemprop="streetAddress"]/text()').extract_first()
        item['city'] = response.xpath('//p[@class="city-state-info"]/span[@itemprop="addressLocality"]/text()').extract_first()
        item['state'] = response.xpath('//p[@class="city-state-info"]/span[@itemprop="addressRegion"]/text()').extract_first()
        item['zip_code'] = response.xpath('//p[@class="city-state-info"]/span[@itemprop="postalCode"]/text()').extract_first()

        yield item
