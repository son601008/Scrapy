import scrapy
from tutorial.items import NewsTitle    
import pandas as pd
import openpyxl
#open('test.txt','w+',encoding='utf-8')
class test(scrapy.Spider):
    name='test'
    start_urls=['https://dantri.com.vn/bat-dong-san.htm']
    def parse(self, response):
        newstitle=NewsTitle()
        newstitle['link']=[]
        newstitle['name']=[]
        newstitle['data_id']=response.xpath('//*[@id="listcheckepl"]//div[@data-boxtype="timelineposition"]//a[starts-with(@href,"/bat-dong-san/")]/@data-id').getall()
        for dataid in newstitle['data_id']:
            newstitle['link'].append((response.xpath('//*[@id="listcheckepl"]//a[@data-id="%s"]/@href' % dataid)).get())
            newstitle['name'].append((response.xpath('//*[@id="listcheckepl"]//a[@data-id="%s"]/@title' % dataid)).get())
        news = {'dataid': newstitle['data_id'], 'link': newstitle['link'], 'name':newstitle['name']}
        df=pd.DataFrame(news)
        df.to_csv('test7.csv', encoding='utf-16')
        '''with open('test.txt', 'a+',encoding='utf-8') as f:
            print(df, file=f)'''
        '''next_page = response.xpath('//*[@id="html"]/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)'''
        return newstitle