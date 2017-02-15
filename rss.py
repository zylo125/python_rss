# coding=utf-8
import feedparser
import MySQLdb

RSS_URL = "url"

yahoo_news = feedparser.parse("url")

for entry in yahoo_news.entries:

 title = (entry.title)
 link  = (entry.link)
 date  = (entry.updated)

 

 print title
 print link
 print date

 connect = MySQLdb.connect(host='********',
                      user='********',
                      passwd='********',
                      db='********',
                      charset='utf8')

 cursor = connect.cursor()
 cursor.execute("insert into rss(title,link,date)values(%s,%s,%s)",(title,link,date))


 connect.commit()
 cursor.close()
 connect.close()

