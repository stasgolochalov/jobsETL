from flask import Flask
from flask_restful import Api, Resource
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '112358'
app.config['MYSQL_DB'] = 'jobs'
mysql = MySQL(app)
api = Api(app)


@app.route('/', methods=['GET'])
class Job(Resource):
    def get(self, job_location):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT job_titles.Job_Title, categories.Category, statuses.Status, locations.location from job inner join job_titles on job.Job_Title_Id = job_titles.Job_Title_Id inner join categories on job.Category_Id = categories.Category_Id inner join statuses on job.Status_Id = statuses.Status_Id inner join locations on job.Location_Id = locations.Location_Id where locations.Location="%s" ''' % job_location)
        rv = cur.fetchall()
        return rv


api.add_resource(Job, '/jobs/<job_location>')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
