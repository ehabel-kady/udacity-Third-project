#! /usr/bin/env python
import psycopg2

Query_1 = 'select * from articlesviews limit 3'
Query_2 = 'select * from authorviews limit 3'
Query_3 = 'select * from final where result>1'

dbname = 'news'

db = psycopg2.connect(database=dbname)

c = db.cursor()
c.execute(Query_1)
articles = c.fetchall()
c.execute(Query_2)
authors = c.fetchall()
c.execute(Query_3)
errors = c.fetchall()

db.close()
print 'Top viewed articles'
for elem in articles:
    print '"'+elem[0]+'" _ '+str(elem[2])+'views'
print 'Top viewed authors'
for elem in authors:
    print elem[0]+' _ '+str(elem[1])+'views'
print 'errors more than 1%  in one day'
for elem in errors:
    print elem[0]+' _ '+str(elem[1])+'%  errors'
