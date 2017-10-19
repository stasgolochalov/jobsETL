import pymysql

db = pymysql.connect(host="localhost", user="root", password="112358", use_unicode=True, charset="utf8")
cursor = db.cursor()

sql = 'USE Jobs'
cursor.execute(sql)

sql = ("""CREATE TABLE Locations
    (
        Location_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Location VARCHAR(20) NOT NULL
    ) AS
    SELECT Location from Job
    GROUP BY Location
    ORDER BY Location 
    """)
cursor.execute(sql)
sql = 'ALTER TABLE Job ADD COLUMN Job_Title_Id INT NOT NULL, Category_Id INT NOT NULL, Status_Id INT NOT NULL, Location_Id INT NOT NULL '
cursor.execute(sql)
sql ='SET FOREIGN_KEY_CHECKS=0'
cursor.execute(sql)
sql = ('ALTER TABLE Job Add constraint Location_Id foreign key (Location_Id) references Locations(Location_Id)')
cursor.execute(sql)
sql = 'SET SQL_SAFE_UPDATES = 0'
cursor.execute(sql)
sql = ('UPDATE job, Locations SET job.Location_Id=locations.Location_Id  WHERE Job.Location = Locations.Location')
cursor.execute(sql)
sql = 'ALTER TABLE Job drop Location'
cursor.execute(sql)


sql = ("""CREATE TABLE Statuses
    (
        Status_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Status VARCHAR(30) NOT NULL
    ) AS
    SELECT Status from Job
    GROUP BY Status
    ORDER BY Status 
    """)
cursor.execute(sql)
sql ='SET FOREIGN_KEY_CHECKS=0'
cursor.execute(sql)
sql = ('ALTER TABLE Job Add constraint Status_Id foreign key (Status_Id) references Statuses(Status_Id)')
cursor.execute(sql)
sql = ('SET SQL_SAFE_UPDATES = 0')
cursor.execute(sql)
sql = ('UPDATE job, Statuses SET job.Status_Id=Statuses.Status_Id  WHERE Job.Status = Statuses.Status')
cursor.execute(sql)
sql = 'ALTER TABLE Job drop Status'
cursor.execute(sql)


sql = ("""CREATE TABLE Categories
    (
        Category_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Category VARCHAR(30) NOT NULL
    ) AS
    SELECT Category from Job
    GROUP BY Category
    ORDER BY Category 
    """)
cursor.execute(sql)
sql ='SET FOREIGN_KEY_CHECKS=0'
cursor.execute(sql)
sql = ('ALTER TABLE Job Add constraint Category_Id foreign key (Category_Id) references Categories(Category_Id)')
cursor.execute(sql)
sql = ('SET SQL_SAFE_UPDATES = 0')
cursor.execute(sql)
sql = ('UPDATE job, Categories SET job.Category_Id=Categories.Category_Id  WHERE Job.Category = Categories.Category')
cursor.execute(sql)
sql = 'ALTER TABLE Job drop Category'
cursor.execute(sql)

sql = ("""CREATE TABLE Job_Titles
    (
        Job_Title_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Job_Title VARCHAR(70) NOT NULL
    ) AS
    SELECT Job_Title from Job
    GROUP BY Job_Title
    ORDER BY Job_Title 
    """)
cursor.execute(sql)
sql ='SET FOREIGN_KEY_CHECKS=0'
cursor.execute(sql)
sql = ('ALTER TABLE Job Add constraint Job_Title_Id foreign key (Job_Title_Id) references Job_Titles(Job_Title_Id)')
cursor.execute(sql)
sql = ('SET SQL_SAFE_UPDATES = 0')
cursor.execute(sql)
sql = ('UPDATE job, Job_Titles SET job.Job_Title_Id=Job_Titles.Job_Title_Id  WHERE Job.Job_Title = Job_Titles.Job_Title')
cursor.execute(sql)
sql = 'ALTER TABLE Job drop Job_Title'
cursor.execute(sql)