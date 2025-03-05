import csv 
with open("details.csv","r")as file:
    cread = csv.reader(file)
    list = list(cread)
    for i in range(1,len(list)):
        print(list[i]) 
# another method
import csv 
with open("details.csv","r")as file:
    cread = csv.reader(file)
    next(cread) #skips the first line
    for rows in cread:
        print(rows)
    
