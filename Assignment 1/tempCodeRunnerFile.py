with open ("numbers.txt","r")as file:
    r = file.read().strip().split()
    num = []
    for words in r:
        if words.isdigit():
            print(words)
            num.append(words)
    print(num)