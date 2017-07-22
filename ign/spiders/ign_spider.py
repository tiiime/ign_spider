import scrapy

from ign.items import IgnItem


class IGNSpider(scrapy.Spider):
    name = "IGN_Spider"

    def start_requests(self):
        urls = []
        base = "http://www.ign.com/games/reviews-ajax?startIndex=%d"
        for index in range(1, 2):
            urls.append(base % index)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        for sel in response.css('body > div'):
            item = IgnItem()
            item['cover'] = sel.xpath('div[1]/a/img/@src').extract_first().strip()
            item['title'] = sel.xpath('div[2]/div[1]/h3/a/text()').extract_first().strip()
            item['platform'] = sel.xpath('div[2]/div[1]/h3/span/text()').extract_first().strip()
            item['type'] = sel.xpath('div[2]/p/span/text()').extract_first().strip()
            item['details'] = sel.xpath('div[2]/p/text()').extract_first().strip()
            item['date'] = sel.xpath('div[3]/div/text()').extract_first().strip()
            item['score'] = sel.xpath('div[4]/div/a/span[1]/text()').extract_first().strip()
            item['scorePhrase'] = sel.xpath('div[4]/div/a/span[2]/text()').extract_first().strip()
            items.append(item)
        return items
