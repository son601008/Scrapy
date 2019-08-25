import scrapy
filename = 'dantrikd.text'
open(filename, 'w')
class QuotesSpider(scrapy.Spider):
    name = "dantrikd"
    start_urls = [
        'https://dantri.com.vn/kinh-doanh.htm'
    ]
    def parse(self, response):
        href=response.xpath('//*[@id="listcheckepl"]//@href').getall()
        href=set(href)
        t=[]
        for s in href:
            if s.startswith("/kinh-doanh/"):
                t.append(s)
        shref='\n'.join(t)        
        with open(filename, 'a+') as f:
            f.write(shref)
        next_page = response.xpath('//*[@id="html"]/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)