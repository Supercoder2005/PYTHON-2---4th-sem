file1 = open("second.txt","a")
with open ("first.txt","w") as file:
    file.writelines("Carry umbrella and overcoat when it rains.")

with open ("first.txt","r") as file:  
    r = file.readlines()
    for word in r:
        if word[0] in "aeiou":
            file1.write(word)
    