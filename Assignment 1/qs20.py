with open ("f1.txt","r")as file:
    r = file.readlines()
    modified_lines = []

    for line in r:
        words = line.strip().split()
        filtered_words=[] 

        for i in range(len(words)):
            if i%2 == 0:
                filtered_words.append(words[i])
        
        modified_lines.append(" ".join(filtered_words))

print(modified_lines)

with open("f1.txt","a")as file:
    for lines in modified_lines:
        file.write(lines+"\n")