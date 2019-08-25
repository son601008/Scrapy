import scrapy


class QuotesSpider(scrapy.Spider):
    name = "dantrihref"
    start_urls = [
        'https://dantri.com.vn/'
    ]

    def parse(self, response):
        href=response.xpath('//*[@id="html"]/body//*/@href').getall()
        href=set(href)
        t=[]
        for s in href:
            if s.startswith('/kinh-doanh'):
                t.append(s)
        
        shref='\n'.join(t)
        filename = 'dantrihrefkd.text'
        with open(filename, 'w') as f:
            f.write(shref)
