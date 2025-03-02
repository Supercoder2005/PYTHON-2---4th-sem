with open ("INDIA.txt","r") as file:
    count = 0
    r = file.read().strip().split()
    print(r) 
    for word in r:
        for letter in word:
            if letter in "aeiouAEIOU":
                count += 1
    print("Total no of vowels=",count)