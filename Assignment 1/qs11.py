with open ("INDIA.txt","w") as file:
    file.write("India  is  the fastest-growing  economy.\n")
    file.write("India  is  looking  for  more  investments  around  the  globe.\n")
    file.write("The whole  world  is  looking  at  India  as  a  great  market.\n")
    file.write("Most  of  the  Indians  can  foresee  the heights that India is capable of reaching.\n")

with open("INDIA.txt","r") as file:
    r=file.readlines()
    count = 0
    for line in r:
        if "India" in line:
            count += 1 
    print("The occurance of the word 'India' is = ",count)

