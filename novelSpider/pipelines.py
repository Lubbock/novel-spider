# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from novelSpider.items import NovelspiderItem
import os

class NovelspiderPipeline:
    def process_item(self, item, spider):
        # if isinstance(item,NovelspiderItem):
        link = item['link']
        article = item['article']
        ugroups = link.split("/")
        fname = ".".join([ugroups[len(ugroups)-1],"txt"])
        with open("./chap0/"+fname,'w') as f:
            f.writelines(article)
        return item
