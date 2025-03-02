file1 = open("second.txt","a")
with open ("first.txt","w") as file:
    file.writelines("Carry umbrella and overcoat when it rains.")

with open ("first.txt","r") as file:  
    r = file.read().split() # it will break the line from white spaces and help to seperate each words
    print(r)
    for word in r:
        if word[0] in "aeiou":
            file1.write(word+" ")

file1.close()  