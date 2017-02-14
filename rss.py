# coding=utf-8
import feedparser
import MySQLdb

RSS_URL = "url"

yahoo_news = feedparser.parse(RSS_URL)

for entry in yahoo_news.entries:

 title = (entry.title).encode("shift-jis")
 link  = (entry.link).encode("shift-jis")
 date  = (entry.updated).encode("shift-jis")

 

 print title
 print link
 print date

 connect = MySQLdb.connect(host='********',
                      user='********',
                      passwd='********',
                      db='db')
 cursor = connect.cursor()

 cursor.execute ("insert into rss(title,link,date)values(%s,%s,%s)",(title,link,date))


 connect.commit()
 cursor.close()
 connect.close()

