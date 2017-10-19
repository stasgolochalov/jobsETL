import pymysql
import csv

db = pymysql.connect(host="localhost", user="root", password="112358", use_unicode=True, charset="utf8")
cursor = db.cursor()
sql = 'CREATE DATABASE  Jobs'

sql = 'USE Jobs'
cursor.execute(sql)
sql = ("""CREATE TABLE JOB
    (
        Job_Id INT NOT NULL AUTO_INCREMENT,
        Job_Title VARCHAR(70) NOT NULL, 
        Category VARCHAR(30) NOT NULL, 
        Status VARCHAR(30) NOT NULL, 
        Location VARCHAR(20) NOT NULL,
        PRIMARY KEY(Job_Id)
    ) """)
cursor.execute(sql)

csv_data = csv.reader(open('snap.csv'))
next(csv_data)
for row in csv_data:
     cursor.execute('INSERT INTO JOb(Job_Title,Category,Status,Location) VALUES (%s, %s, %s, %s)',row)
db.commit()
cursor.close()
