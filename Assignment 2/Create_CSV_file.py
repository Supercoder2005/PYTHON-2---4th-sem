import csv 

header =["Country","Played","Won","Lost","Tied","No","Result"]
data=[
    ["England",746,375,334,9,28],
    ["Australia",949,575,331,9,34],
    ["India",987,513,424,9,41]
]
with open('details.csv',"w",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
           