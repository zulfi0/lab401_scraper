# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab401Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_link = scrapy.Field()
    product_name = scrapy.Field()
    product_currency = scrapy.Field()
    product_price = scrapy.Field()
    product_description = scrapy.Field()
