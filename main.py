from openpyxl import Workbook
from openpyxl import load_workbook
from scholarly import scholarly 
import pandas as pd

FILENAME = "Publications_05.22.2023 (1).xlsx"
SHEETNAME = "Full papers"
cols = ["Professor", "Title", "Journal", "Year"]

def file_copy_path_generator(file_path=None): 
    cnt=1
    file_path_units = file_path.split('')
    while(True):
        new_file_name = "("+str(cnt)+")"+file
        try: 
            with open(new_file_name, "r"): 
                pass
        except: 
            return new_file_name 

#sheet is defaulted to 1 
def process_excel(file): 
    max_row = 1; 
    wb = load_workbook(filename=file)
    ws = wb.active
    while(ws[str('B')+str(max_row)].value!=None): 
        max_row=max_row+1
    return [wb, ws, max_row] 

def clean_duplicates(file=None):
    if file is None: 
        file = input("Enter File Path: ")
    try: 
        with open(file, 'r') as file: 
            print("Read Successfully")
    except FileNotFoundError: 
        print("File Not Found") 
        return
    ls = process_excel(file) 
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

    #
    wb.save(file+"")

def sort_list(file=None): 
    if file is None: 
        file = input("Enter File Path: ")
    try: 
        with open(file, 'r') as file: 
            print("Read Successfully")
    except FileNotFoundError: 
        print("File Not Found")
        return 
    try: 
        df = pd.read_excel(file, sheet=0)
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
        df.to_excel(file, sheet_name=0, index=False)
    except:    
        print("Sheet Error") 

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


def modify_list(file_path=None): 
    if file_path is None: 
        file_path = input("Enter File Path: ")
    try: 
        with open(file_path, 'r') as file: 
            print("Read Successfully")
    except FileNotFoundError: 
        print("File Not Found")
        return 
    ls = process_excel(file_path)
    wb=ls[0], ws=ls[1], max_row=ls[2] 
    author_names = {}
    for i in range(1, max_row): 
        author_names[ws['A'+chr(i)]]=True
    #check to see if author name exists
    author_name_input = input("Enter Author Name: ")
    if author_names[author_name_input] is True: 
        year_l_bound = int(input("Year(left bound): "))
        year_r_bound = int(input("Year(right bound): "))
        search_result = []
        for i in range(1, max_row): 
            if ws['A'+chr(i)]==author_names:
                if(ws['D'+chr(i)]>=year_l_bound and ws['D'+chr(i)]<=year_r_bound): 
                    search_result.append(i)
        if(len(search_result)==0): 
            print("No Result")
            return
        print("INDEX    ROW")
        for i in range(len(search_result)):
            print(i+1,"       ",search_result[i])
        opt = int(input("Enter INDEX to delete (0 to quit): "))
        while(opt!=0 and len(search_result)!=0):
            opt = int(input("Enter INDEX to delete (0 to quit): "))
            try: 
                ws.delete_rows(search_result[opt-1], 1)
            except: 
                print("Error")
        wb.save(file_path)
    else: 
        print("Author not Found")


def add_author(): 
    pass  

def generate_php(): 
    pass 

def ui(): 
    funct=[clean_duplicates,sort_list,update_list,modify_list,add_author,generate_php]
    file_path=input("Enter File Path: ")
    try: 
        with open(file_path, 'r') as file: 
            print("Read Successfully")
    except FileNotFoundError: 
        print("File Not Found")
        return    
    
    #) path may not be in current directory
    file_copy_path = file_name_generator(file_path)
    while(True): 
        print("1)clean duplicates  2)sort entries  3)update author")
        print("4)modify entries  5)add author  6)generate php file")
        opt = int(input("Enter Operation: "))
        while(opt<1 or opt>6): 
            print("Error")
            opt = int(input("Enter Operation: "))
        funct[opt-1](file_copy_path)

if __name__=="__main__":
    ui()