import scrapy


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
        self.log(response)
        self.log("get")
