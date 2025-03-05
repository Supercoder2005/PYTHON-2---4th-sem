import csv 
with open("details.csv","r")as file:
    cread = csv.reader(file)
    for rows in cread:
        print (rows) 