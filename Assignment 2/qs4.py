import csv 
d={}
with open("details.csv","r")as file:
    cread = csv.reader(file)
    dict = csv.DictReader(file)
    for row in dict:
        print(row)