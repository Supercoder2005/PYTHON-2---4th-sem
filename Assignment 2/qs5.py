import csv 
header = ["Country", "Played", "Won", "Lost", "Tied", "No Result"]
data = [
    {"Country": "England", "Played": 746, "Won": 375, "Lost": 334, "Tied": 9, "No Result": 28},
    {"Country": "Australia", "Played": 949, "Won": 575, "Lost": 331, "Tied": 9, "No Result": 34},
    {"Country": "India", "Played": 987, "Won": 513, "Lost": 424, "Tied": 9, "No Result": 41}
]
with open("details1.csv","w",newline="")as file:
    writer = csv.DictWriter(file,fieldnames = header)
    writer.writeheader()
    writer.writerows(data)

