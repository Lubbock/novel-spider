# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
import scrapy
from novelSpider.items import NovelspiderItem
class NovelSpider(Spider):
    name="novelSpider"
    start_urls=["https://www.soshuw.com/ShiSiRuGuiWeiJunZi/"]
    domain_name = "https://www.soshuw.com/"
    allowed_domains = ['www.soshuw.com']
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.soshuw.com"
    }

    def parse(self, response):
        articles = response.xpath('//div[@class="novel_list"]/dl/dd/a')
        for article in articles:
            link = article.xpath("@href").extract_first().strip()
            next_page = response.urljoin(link)
            yield scrapy.Request(next_page, callback=self.article_parse)

    def article_parse(self, response):
        item = NovelspiderItem()
        item['link'] = response.url[len(self.domain_name):]
        item['article'] = response.xpath('//div[@class="content"]').xpath('string(.)').extract_first()
        return item