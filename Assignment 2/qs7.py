import csv 

data=[
    ['Rno','Name','Score','Class'],
    [101,'Alex',80,12],
    [102,'Monica',84,12],
    [103,'Ajay',72,12],
    [104,'Irfan',82,11]
]
with open("student.csv",'w',newline="")as file:
    writer = csv.writer(file)
    writer.writerows(data)

filename = "student.csv"
def count_rec(filename):
    count = 0
    with open(filename,"r")as file:
        reader = csv.DictReader(file)
        for row in reader:
            if((row["Score"])>80):
                count += 1 
    print(count)
count_rec("student.csv")