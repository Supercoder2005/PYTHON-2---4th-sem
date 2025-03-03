with open("INDIA.txt","r")as file:
    r = file.readlines()
    r1=[]
    
    for lines in r:
        lines = lines.strip()
        r1.append(lines)
    
    print("The content of the file in reversed order ----- \n")
    
    for i in range((len(r1)-1),-1,-1):
        print(r1[i])