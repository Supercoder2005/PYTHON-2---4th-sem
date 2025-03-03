with open ("f1.txt","w")as file:
    text = input("Enter the lines you want to write in the file(give comma between each line):")
    text = text.split(",")
    for lines in  text:
        file.write(lines+"\n")

with open ("f1.txt","r")as file:
    capitalized_words = []
    r = file.read().strip().split()
    for words in r:
        words = words.capitalize()
        capitalized_words.append(words)

capitalized_text = " ".join(capitalized_words)
with open("f1.txt","a")as file:
    file.write(capitalized_text)
   