from bs4 import BeautifulSoup
import csv

f = open('snap.html', 'r')
soup = BeautifulSoup(f,'html.parser')
table = soup.find('section', {'class': 'roles-results'})

jobs = []
for row in table.find_all('tr'):
        cols = row.find_all('td')
        colsJT = row.find_all('th')
        jobs.append({
            'Job Title': colsJT[0].a.text,
            'Category': cols[0].span.text,
            'Status': cols[1].span.text,
            'Location': cols[2].span.text
        })


def save(jobs, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Job Title', 'Category', 'Status', 'Location'))

        for job in jobs:
            writer.writerow((job['Job Title'], job['Category'], job['Status'], job['Location']))

save(jobs,'snap.csv')