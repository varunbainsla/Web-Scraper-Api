# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from asyncio.windows_events import NULL
from itemadapter import ItemAdapter

import sqlite3

class WebscrapePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()



    def  create_connection(self):
        self.conn=sqlite3.connect('mydata.db')
        self.curr=self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS data_tb""")
        self.curr.execute("""create table  data_tb(Title text NOT NULL DEFAULT 'null',Author text NOT NULL DEFAULT 'null',Paragraph text)""")

    def process_item(self, item, spider):
        
        self.curr.execute("""INSERT INTO data_tb(Title,Author,Paragraph) VALUES(?,?,?)""",(item['title'],item['author'],item['post']))
        #self.curr.execute("""INSERT INTO data_tb(Author) VALUES(?)""",(b))
  #      self.curr.execute("""INSERT INTO data_tb(Paragraph) VALUES(?)""",(c))
        
        self.conn.commit()
    
        return item