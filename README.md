# jobsETL
ETL​​ ​jobs​ ​from​ ​company​ ​website​ ​to​ ​database.

Crawler.py - crawl website with Chroe selenium wedriver and returns snap.html
Extractor.py - extract required data to snap.csv
ETL_1.py - create new MySQL database and import snap.csv into it
ETL_2.py - MySQL database normalization
API.py - creates API with Flask to acess the database

example: http://localhost:5000/jobs/London returns all the open jobs in London
