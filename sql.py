import sqlite3
import pandas as pd
con = sqlite3.connect(r"C:\Users\VARUN\Desktop\flask\Web Scraper\Webscrape\Webscrape\mydata.db")

#con = sqlite3.connect(r"C:\Users\VARUN\Desktop\flask\Web Scraper\Webscrape\Webscrape\mydata.db")
cur = con.cursor()
cur.execute("SELECT * FROM data_tb")
data = cur.fetchall()
print(data[0][0])
#sql_query = pd.read_sql_query ('''
#                               SELECT
#                               *
#                               FROM data_tb
#                              ''', con)

#df = pd.DataFrame(sql_query, columns = ['Title', 'Author', 'Paragraph'])
#print (df)