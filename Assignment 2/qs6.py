import csv 
num_records = 3
data =[]
for i in range(num_records):
    entry = eval(input(f"Enter details for user{i+1}as dictionary:"))
    data.append(entry)
header = ["Username","Password"]
with open("login_credentials.csv","w",newline="")as file:
    writer = csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
with open('login_credential.csv',"r")as file:
    reader = csv.freader(file)
    for rows in reader:
        print(" ".join(rows))
