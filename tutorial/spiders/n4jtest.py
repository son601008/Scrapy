import scrapy
from tutorial.items import NewsTitle    
import pandas as pd
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "graph"))
newstitle=NewsTitle()
newstitle['link']=[]
newstitle['name']=[]
newstitle['data_id']=[]
class test(scrapy.Spider):
    name='testn4j'
    start_urls=['https://dantri.com.vn/bat-dong-san.htm']
    def parse(self, response):
        outlist=[]
        newlist=response.xpath('//*[@id="listcheckepl"]//div[@data-boxtype="timelineposition"]/div/h2/a[starts-with(@href,"/bat-dong-san/")]/@data-id').getall()
        for i in newstitle['data_id']:
            if i in newlist:
                outlist.append(i)
                newlist.remove(i)
        newstitle['data_id'].extend(newlist)
        for dataid in newstitle['data_id']:
            if response.xpath('//*[@id="listcheckepl"]//div[@data-boxtype="timelineposition"]/div/h2/a[@data-id="%s"]/@href' % dataid).get() is not None and dataid not in outlist:
                newstitle['link'].append(response.xpath('//*[@id="listcheckepl"]//div[@data-boxtype="timelineposition"]/div/h2/a[@data-id="%s"]/@href' % dataid).get())
                newstitle['name'].append(response.xpath('//*[@id="listcheckepl"]//div[@data-boxtype="timelineposition"]/div/h2/a[@data-id="%s"]/@title' % dataid).get())
        next_page = response.xpath('//*[@id="html"]/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/a/@href').get()
        if next_page is not None and response.url!=response.urljoin(next_page):
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
        else:
            news = {'dataid': newstitle['data_id'], 'link': newstitle['link'], 'name':newstitle['name']}
            df=pd.DataFrame(news)
            df.to_csv('C:/Users/Kazami Akatsuki/.Neo4jDesktop/neo4jDatabases/database-d3f667aa-5b13-45b3-821c-6c6904fd3e8e/installation-3.5.6/import/dantribds.csv', encoding='utf-16')
            '''with driver.session() as session:
                session.run("LOAD CSV WITH HEADERS FROM \"file:/dantribds.csv\" AS line " 
                            "MERGE (n:news {link: line.link, name: line.name})")'''
        return newstitle