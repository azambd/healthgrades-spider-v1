# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HealthgradesSpiderItem(scrapy.Item):

	name = scrapy.Field()
	gender = scrapy.Field()
	speciality = scrapy.Field()
	street_address = scrapy.Field()
	city = scrapy.Field()
	state = scrapy.Field()
	zip_code = scrapy.Field()
	link = scrapy.Field() 