import scrapy
from tutorial.items import News    
import pandas as pd
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "graph"))
newstitle=News()
newstitle['link']=[]
newstitle['name']=[]
class test(scrapy.Spider):
    name='vnexpress'
    start_urls=['https://vnexpress.net/kinh-doanh']
    def parse(self, response):
        newstitle['link'].extend(response.xpath('//section[@class="container"]/section[@class="sidebar_1"]//h4[@class="title_news"]/a[1]/@href').getall())
        for link in newstitle['link']:
            if (response.xpath('//section[@class="sidebar_1"]//h4[@class="title_news"]/a[@href="%s"]/@title' % link).get()) is not None:
                newstitle['name'].append(((response.xpath('//section[@class="sidebar_1"]//h4[@class="title_news"]/a[@href="%s"]/@title' % link))).get())
        news = {'link': newstitle['link'], 'name':newstitle['name']}
        next_page = response.xpath('//*[@id="pagination"]/a[@class="next"]/@href').get()
        if next_page is not None and len(newstitle['link']) < 200:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            news = {'link': newstitle['link'], 'name':newstitle['name']}
            df=pd.DataFrame(news)
            df.to_csv('C:/Users/Kazami Akatsuki/.Neo4jDesktop/neo4jDatabases/database-d3f667aa-5b13-45b3-821c-6c6904fd3e8e/installation-3.5.6/import/vnexpress.csv', encoding='utf-16')
            with driver.session() as session:
                session.run("LOAD CSV WITH HEADERS FROM \"file:/vnexpress.csv\" AS line " 
                            "MERGE (n:news {link: line.link, name: line.name})")
        return newstitle