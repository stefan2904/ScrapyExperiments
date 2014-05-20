# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Scrapytest1Pipeline(object):
     def __init__(self):
         self.file = open('items.jl', 'wb')

     def process_item(self, item, spider):
         line = json.dumps(dict(item)) + "\n"
         self.file.write(line)
         return item

     def close_spider(self, spider):
         #line = json.dumps(dict(spider.tree)) + "\n"
         #self.file.write(line)
         pass
         