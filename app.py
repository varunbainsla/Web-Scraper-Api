
from ast import parse
from re import A
import sqlite3
from urllib import response
from urllib.request import ProxyDigestAuthHandler
from flask import Flask
from flask import render_template
from flask import request
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import scrapy
from tech import *


app = Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def root():
    if request.method=='GET':
            return render_template('home.html')
    elif request.method=='POST':
        startspider()
        con = sqlite3.connect(r"C:\Users\VARUN\Desktop\flask\Web Scraper\Webscrape\Webscrape\mydata.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM data_tb")
        data = cur.fetchall()
        #d=data['Title']
        #print(d)
        return render_template('home.html', data=data)
        
        #p=['1','2','3','4','5']
        
        #return  render_template('home.html',proxies=p)


if __name__=='__main__':
    app.run(debug=True, threaded=True)