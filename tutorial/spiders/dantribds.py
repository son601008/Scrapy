import scrapy
open('dantribds.text', 'w+', encoding='utf-8')

class QuotesSpider(scrapy.Spider):
    name = "dantribds"
    start_urls = [
        'https://dantri.com.vn/bat-dong-san.htm'
    ]

    def parse(self, response):
        title=response.xpath('//*[@id="listcheckepl"]//a[starts-with(@href,"/bat-dong-san/")]/@title').getall()
        title=set(title)
        stitle='\n'.join(title)
        filename = 'dantribds.text'
        with open(filename, 'a+',encoding='utf-8') as f:
            f.write(stitle)
        next_page = response.xpath('//*[@id="html"]/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
