import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/list/show/168719.2023_Contemporary_Romance_Releases'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

books = soup.find_all('tr', itemtype='http://schema.org/Book')

with open('goodreads_books.csv', mode='w') as csv_file:
    fieldnames = ['Book Title', 'Author', 'Avg Rating']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for book in books:
        title = book.find('a', class_='bookTitle').text.strip()
        author = book.find('a', class_='authorName').text.strip()
        avg_rating = book.find('span', class_='minirating').text.strip().split()[0]
        writer.writerow({'Book Title': title, 'Author': author, 'Avg Rating': avg_rating})