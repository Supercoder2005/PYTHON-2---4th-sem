with open ("INDIA.txt","r") as file:
    r = file.readlines()
    line_num = int(input("Enter the specific number of line you want to see:"))
    if (1<= line_num <= len(r)):
        print(f"line number{line_num}:{r[line_num-1].strip()}")
    else:
        print("Invalid line number.")

                   