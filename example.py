from openpyxl import Workbook
from openpyxl import load_workbook
from scholarly import scholarly, ProxyGenerator 
import pandas as pd
from bs4 import BeautifulSoup
import requests, Proxy

cols = ["Professor", "Title", "Journal", "Year"]

#task 2
def sort_list(file_path=None, sheet="Full papers", opt1=None, opt2=None): 
    if file_path is None: 
        file_path = input("Enter File Path: ") 
    df = pd.read_excel(file_path)
    for i in range(len(cols)):
        print("("+str(i+1)+")", cols[i], " ")  
    if(opt1 is None):
        opt1 = int(input("Sort By: "))
    while(opt1<1 or opt1>4): 
        print("ERROR")
        opt1 = input("Sort By: ")
    if(opt2 is None): 
        opt2 = input("ascending(a) / descending(d): ")
    while(opt2!='a' and opt2!='d'): 
        print("ERROR")
        opt2 = input("ascending(a) / descending(d): ")
    opt1 -= 1
    opt2 = True if(opt2=='a') else False
    print(opt2, cols[opt1])

    df.sort_values(by=[cols[opt1]], ascending=opt2, inplace=True)
    df.to_excel("out.xlsx", sheet_name=sheet, index=False)
    print("SUCCESSED")

sort_list("s.xlsx")