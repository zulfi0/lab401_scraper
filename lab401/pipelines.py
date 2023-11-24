# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pandas as pd


class Lab401Pipeline:
    def __init__(self) -> None:
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
    
    def close_spider(self, spider):
        data = self.items

        df = pd.DataFrame(data)
        df.to_csv('lab401_scraped.csv', index=False)
        df.to_excel('lab401_scraped.xlsx', index=False)

        with open('lab401_scraped.json', 'w') as f:
            json.dump(data, f)

