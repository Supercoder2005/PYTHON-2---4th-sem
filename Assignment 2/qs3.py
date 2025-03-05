import csv 
new_data = [
    ["Pakistan",948,498,412,8,23],
    ["South Africa",638,393,218,6,21]
]
with open("details.csv","a",newline="")as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
    