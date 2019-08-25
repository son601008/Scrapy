import scrapy
from scrapy_splash import SplashRequest
from tutorial.items import tiki   

class MySpider(scrapy.Spider):
    name = "jsscraper"

    start_urls = ["https://tiki.vn/dien-thoai-may-tinh-bang/c1789?_lc=Vk4wMzQwMjAwMDg%3D"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        quote = tiki()
        quote["did"] = response.css('data-id').extract_first()
        quote["link"] = None
        quote["title"] = None
        yield quote