import scrapy
open('dantri.text', 'w+', encoding='utf-8')

class QuotesSpider(scrapy.Spider):
    name = "dantri"
    start_urls = [
        'https://dantri.com.vn/'
    ]

    def parse(self, response):
        title=response.xpath('//*[@id="html"]/body/div/div/div/div/div/div/div//*/@title').getall()
        title=set(title)
        stitle='\n'.join(title)
        filename = 'dantri.text'
        with open(filename, 'a+',encoding='utf-8') as f:
            f.write(stitle)
