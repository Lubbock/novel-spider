# -*- coding: utf-8 -*-
from scrapy import cmdline
import os

if __name__ == "__main__":
    # os.makedirs("./chap0")
    cmdline.execute("scrapy crawl novelSpider".split())