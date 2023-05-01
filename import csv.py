import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/q-Python-Data-Analyst-jobs.html?vjk=8030c87e4e81e9f9'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

with open('indeed_jobs.csv', mode='w') as csv_file:
    fieldnames = ['Job Title', 'Company', 'Salary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for job in jobs:
        title = job.find('a', class_='jobtitle').text.strip()
        company = job.find('span', class_='company').text.strip()
        salary_tag = job.find('span', class_='salaryText')
        salary = salary_tag.text.strip() if salary_tag else 'N/A'
        writer.writerow({'Job Title': title, 'Company': company, 'Salary': salary})