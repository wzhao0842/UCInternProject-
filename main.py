from openpyxl import Workbook
from openpyxl import load_workbook
from scholarly import scholarly 
import pandas as pd

FILENAME = "Publications_05.22.2023 (1).xlsx"
SHEETNAME = "Full papers"
cols = ["Professor", "Title", "Journal", "Year"]

def process_excel(): 
    max_row = 1; 
    wb = load_workbook(filename=FILENAME)
    ws = wb.active
    while(ws[str('B')+str(max_row)].value!=None): 
        max_row=max_row+1
    return [wb, ws, max_row] 

def clean_duplicates():
    ls = process_excel() 
    wb=ls[0], ws=ls[1], max_row=ls[2]
    #finding duplicates using counter array
    dup = []
    for i in range(0, max_row): 
        dup.append(0)

    for i in range(1, max_row):
        if(dup[i]!=0):
            continue
        title = ws[str('B')+str(i)].value
        journal = ws[str('C')+str(i)].value
        dup[i]=i
        for j in range(i+1, max_row):
            tl = ws[str('B')+str(j)].value
            jl = ws[str('C')+str(j)].value
            if(tl==title and jl==journal): 
                dup[j]=i 

    action_dup_row = []
    #presenting duplciates
    for i in range(1, max_row):  
        dup_row = [i]
        for j in range(i+1, max_row): 
            if(dup[j]==dup[i]): 
                dup_row.append(j)
                action_dup_row.append(j) 
        if(len(dup_row)>1): 
            print("Duplicates Found: ")
            for k in range(len(dup_row)):
                print("ROW "+str(dup_row[k]))
            print("\n")

    action_dup_row.sort(reverse=True)
    option = input("Clean Duplicates(y/n): ")
    if(option=='y'): 
        for i in range(len(action_dup_row)):
            ws.delete_rows(action_dup_row[i], 1)

    wb.save(FILENAME)

def sort_list(filename, sheetname): 
    df = pd.read_excel(filename, sheetname)    
    for i in range(len(cols)):
        print("("+str(i+1)+")", cols[i], " ")  
    opt1 = int(input("Sort By: "))
    while(opt1<1 or opt1>4): 
        print("ERROR")
        opt1 = input("Sort By: ")
    opt2 = input("ascending(a) / descending(d): ")
    while(opt2!='a' and opt2!='d'): 
        print("ERROR")
        opt2 = input("ascending(a) / descending(d): ")
    opt1 -= 1
    opt2 = True if(opt2=='a') else False
    print(opt2, cols[opt1])
    df.sort_values(by=[cols[opt1]], ascending=opt2, inplace=True)
    df.to_excel(filename, sheet_name=sheetname, index=False)

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


def modify_list(): 
    ls = process_excel()
    wb=ls[0], ws=ls[1], max_row=ls[2] 
    author_names = {}
    for i in range(1, max_row): 
        author_names[ws['A'+chr(i)]]=True

def add_author(): 
    pass  

def generate_php(): 
    pass 

    
# if __name__=='__main__': 
    