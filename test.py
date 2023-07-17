from scholarly import scholarly 
from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd 

FILENAME = "TST.xlsx"
SHEETNAME = "test"
cols = ["Professor", "Title", "Journal", "Year"]

def update_list(AUTHOR_NAME):
    search_query = scholarly.search_author(AUTHOR_NAME)
    first_author_result = next(search_query)
    author = scholarly.fill(first_author_result) 
    for pub in author['publications']:
        try:
            #scholarly.bibtext(pub)
            pub_title = pub['bib']['title']
            #search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
            #newpub = next(search_query)
            #print(newpub)
            pub_date = pub['bib']['pub_year']
            pub_journal = pub['bib']['citation']
            pub_citation = pub['num_citations']
            print(pub_title,pub_date,pub_citation,pub_journal)
        except:
            print("Invalid Publication")

# update_list("Hamid Jafarkhani")

# search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
# scholarly.pprint(scholarly.fill(next(search_query)))

def modify_list():

    name = input("Enter Author Name: ")
    

MAX_ROW = 1; 
FILENAME = "Publications_05.22.2023 (1).xlsx"
SHEETNAME = "Full papers"
cols = ["Professor", "Title", "Journal", "Year"]

wb = load_workbook(filename=FILENAME)
ws = wb.active

while(ws[str('B')+str(MAX_ROW)].value!=None): 
    MAX_ROW=MAX_ROW+1

def modify_list(): 
    