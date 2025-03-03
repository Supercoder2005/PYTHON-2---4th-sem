with open ("numbers.txt","w")as file:
    file.write("The price of 3 apples is 150 rupees and 2 mangoes cost 80")
with open ("numbers.txt","r")as file:
    r = file.read().strip().split()
    num = []
    for words in r:
        if words.isdigit():
            num.append(words)
    print(num)