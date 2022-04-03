
from gettext import install
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import time

import scrapy
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
import os
from crochet import setup
#setup()
from items import WebscrapeItem

class TechSpider(scrapy.Spider):
    name = 'tech'
    allowed_domains = ['techcrunch.com']
    start_urls = ['https://techcrunch.com/2022/04/01/staten-island-amazon-workers-vote-to-unionize/']
    
    def parse(self, response):
        #c=response.css('.content a::attr(href)').getall()
        #print(type(c))
        #for i in c:
        #i=response.urljoin(i)
        parse_content(response)   
        #yield response.follow(i,self.parse_content)
           
         
    


    def parse_content(self,response):
        q={}
        ittem = WebscrapeItem()
        item = {}
        Title=response.css('h1.article__title::text').extract()
        Author=response.css('div.article__byline a::text').extract()
        post=response.css('div.article-content ::text').extract()
            
        item['title']= Title
        item['author']=Author
        item['post']=post

        
          
        a = item['title']
        #print(type(a))

        b = item['author']
        

        listt = list(item['post'])
        result= ''
        for element in listt:
            result += str(element)
        c=[]
        c.append(result)
        if len(a)==1 :
            ittem['title']= a[0]
            ittem['author']=b[0]
            ittem['post']=c[0]
        
        
                     
        yield ittem
        


#if __name__=="__main__":
#def s():

    #process = CrawlerProcess(get_project_settings())
    # 'followall' is the name of one of the spiders of the project.
    #process.crawl(TechSpider)
    #process.start(stop_after_crawl=True) # the script will block here until the crawling is finished
   
    #configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    #runner = CrawlerRunner(get_project_settings())
    #runner.crawl(TechSpider)
    #d.addBoth(lambda _: reactor.stop())
    #reactor.run()
#s()
#print(c)
#def run_spider(spiderName):
    #module_name="first_scrapy.spiders.{}".format(spiderName)
    #scrapy_var = import_module(module_name)   #do some dynamic import of selected spider   
    #spiderObj=scrapy_var.mySpider()           #get mySpider-object from spider module
    #crawler = CrawlerRunner(get_project_settings())   #from Scrapy docs
    #crawler.crawl(spiderObj)  

def crawl(runner):
    d = runner.crawl(TechSpider)
    d.addBoth(lambda _: reactor.stop())
    return d


def loop_crawl():
    runner = CrawlerRunner(get_project_settings())
    crawl(runner)
    reactor.run()
    
def startspider():
    loop_crawl()
