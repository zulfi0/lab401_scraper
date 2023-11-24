from pathlib import Path

import scrapy
from lab401.items import Lab401Item


class Lab401Spider(scrapy.Spider):
    name = "lab401"
    allowed_domains = ["lab401.com"]
    start_urls = ["https://lab401.com/collections"]

    def parse(self, response):
        # category_names = response.css('a.featured-box:not(:contains("All Products"))::text').getall()
        category_links = response.css('a.featured-box::attr(href)').extract()

        ctg_links = [link for link in category_links if "all-products" not in link]
        
        for ctg_link in ctg_links:
            link = response.urljoin(ctg_link)
            yield scrapy.Request(link, callback=self.parse_category)

    def parse_category(self, response):
        product_links =  response.css('a.product-grid-item::attr(href)').getall()

        for product_link in product_links:
            product_link = response.urljoin(product_link)
            yield scrapy.Request(url=product_link, callback=self.parse_product)

    def parse_product(self, response):
        item = Lab401Item()
        item['product_link'] = response.url

        if response.css('meta[name="twitter:title"]::attr(content)').get() is not None:
            item['product_name'] = response.css('meta[name="twitter:title"]::attr(content)').get()
            item['product_currency'] =  response.css('meta[property="og:price:currency"]::attr(content)').get()
            item['product_price'] = response.css('meta[property="og:price:amount"]::attr(content)').get()
            item['product_description'] = response.css('meta[property="og:description"]::attr(content)').get()
        else:
            item['product_name'] = response.css('h1.h2::text').get()
            item['product_currency'] =  response.css('meta[itemprop="priceCurrency"]::attr(content)').get()
            item['product_price'] = response.css('meta[itemprop="price"]::attr(content)').get()
            item['product_description'] = ''.join(response.css('p:nth-of-type(2)::text').getall())

        yield item
