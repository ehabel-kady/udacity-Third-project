# Summery:
The pyhton program attached when it run it makes queiries from view created in the database
## Program Design:
the program is designed to call views that were created using psql command line.
each query selects the data from each view and print it from the list using a loop.
for example
```
Query_1 = 'select * from articlesviews limit 3'
```
This example contains the query statement that should be executed once the program is called
##Views Created Query Statements:
Question 1
```create view article as select author, title, concat('/article/',slug) as newpath from articles;
create view articlesviews as select title,author, count(*) as views from article, log where log.path=article.newpath group by title,author order by views desc;```

Question 2:
```create view authorviews as select name, sum(articlesviews.views) as views from articlesviews join authors on author=id group by name order by views desc;```

Quesrion 3:
```create view dates as select status, cast(time as DATE) from log;
create view totaldates as select time, count(*) as total from dates group by time;
create view errornum as select totaldates.time, count(*) as errors from dates join totaldates on dates.time=totaldates.time and dates.status='404 NOT FOUND' group by totaldates.time;
create view five as select errornum.time, (cast(errornum.errors as float)/cast(totaldates.total as float)*100) as result from totaldates join errornum on totaldates.time=errornum.time;
create view final as select TO_CHAR(time, 'monthDD, yyyy'), cast(result as decimal(53,2)) from five;```

### To run the code
- If you use windows you have only to run the `project_code.py` file and the queiries results will be printed
- If you use linux, make the terminal at the same directory of `project_code.py` and use the following command `python project_code.py` and the queiries results will be printed
