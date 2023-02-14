from datetime import datetime
from datetime import date
import pandas as pd

def inserrt(fname,list):
    keydate = datetime.strptime(list[-1], "%Y-%m-%d")
    file = open(fname, 'r')
    l = file.readlines()
    mat = []
    for i in range(len(l)):
        l[i] = l[i].split(',')
    i = 1
    st = str(l[i][-1])
    print(l[i][-1])
    while(i<len(l)):
        tempdate = datetime.strptime(st, "%Y-%m-%d")
        diff = (keydate-tempdate).days
        print(diff)
        i+=1

f = 'db.csv'
l = ['2003-06-20','f','f','f','f','f','2003-06-22']
inserrt(f,l)
# td = date.today()
# print(td)
