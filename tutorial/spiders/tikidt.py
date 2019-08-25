import scrapy
from tutorial.items import tiki   
import pandas as pd
from scrapy_splash import SplashRequest
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "graph"))

script = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""
#Lấy thông tin từ trang các trang con
script2 = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""
items=tiki()
items['link']=[]
items['did']=[]
items['title']=[]
items['pic']=[]

class TikiSpider(scrapy.Spider):
    name = 'tiki'
    allowed_domains = ['tiki.vn']
    start_urls = [
        "https://tiki.vn/dien-thoai-may-tinh-bang/c1789"
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute',
                                args={'lua_source': script})

    def parse(self, response):   
        # Get URL in page and yield Request
        url_selector = response.xpath(
            '//*[@class="product-box-list"]/div/a/@href')
        for url in url_selector.extract():
            if url not in items['link']:
                items['link'].append(url)
                items['did'].append(response.xpath(
                    '//a[@href="%s"]/@data-id' % url).get())
                items['title'].append(response.xpath(
                    '//a[@href="%s"]/@title' % url).get())
                items['pic'].append(response.xpath(
                    '//a[@href="%s"]//*[@class="image"]//@src' % url).get())
            '''yield SplashRequest(url, callback=self.parse_item,
                                endpoint='execute',
                                args={'lua_source': script2})'''
        # Get the next page and yield Request
        next_selector = response.xpath('//*[@rel="next"]/@href').extract_first()
        if next_selector is not None:
            yield SplashRequest(next_selector, callback=self.parse,
                                endpoint='execute', args={'lua_source':script2})
        else:
            products={'dataid': items['did'],'link': items['link'],'title':items['title'],'pic':items['pic']}
            cv=pd.DataFrame(products)
            cv.to_csv('C:/Users/Kazami Akatsuki/.Neo4jDesktop/neo4jDatabases/database-d3f667aa-5b13-45b3-821c-6c6904fd3e8e/installation-3.5.6/import/tiki.csv', encoding='utf-16')
            with driver.session() as session:
                session.run("LOAD CSV WITH HEADERS FROM \"file:/tiki.csv\" AS line " 
                            "MERGE (n:products {dataid: line.dataid, title: line.title, link: line.link, pic: line.pic})")
    def parse_item(self, response):
        pass
        