from scholarly import scholarly, ProxyGenerator
import pandas as pd
from openpyxl import load_workbook
import requests
from proxy import Proxy
from bs4 import BeautifulSoup

# Define the columns of the CSV file
columns = ['Professor', 'Title', 'Journal', 'Year', 'Citations', 'php1', 'php2']
cols = ["Professor", "Title", "Journal", "Year"]

# Define the path of the CSV file to store the new papers
csv_file = 'new_papers.csv'

min_pub_date = 2012

# Create an empty DataFrame
df = pd.DataFrame(columns=columns)

# Define the list of professors
#professors = ['Ender Ayanoglu', 'Nader Bagherzadeh', 'Payam Heydari', 'Syed A. Jafar', 'Hamid Jafarkhani', 'Yanning Shen', 'A. Lee Swindlehurst', 'Zhiying Wang', 'Homayoun Yousefi''zadeh', 'Michael Green UCI']
professor = 'Ahmed Eltawil'
# Loop over the professors
# Get an iterator for the author results
search_query = scholarly.search_author(professor)
# Retrieve the first result from the iterator
first_author_result = next(search_query)
#scholarly.pprint(first_author_result)
# Retrieve all the details for the author
author = scholarly.fill(first_author_result )
# scholarly.pprint(author)

# Print the titles of the author's publications
# for pub in author['publications']: 
#     print(scholarly.fill(pub))

proxies = {
  'http': 'http://210.230.238.153:443',
  'https': 'http://210.230.238.153:443',
}
link = "http://scholar.google.com/scholar?hl=en&q=info:MJ4i-QZfzPUJ:scholar.google.com/&output=cite&scirp=0&hl=en"
html = requests.get(link, proxies=proxies).text
soup = BeautifulSoup(html, "lxml")
print(soup.text)
apa_cit = soup.find('th', scope_='row',string="APA")
print(apa_cit)
