import random

r = input ("type a no.: ")

if r.isdigit():
    r = int(r)
     
    if r <= 0:
        print("plz type a number larger than zero next time")
        quit()
else:
    print ("plz type a number next time ")
    quit()

no = random.randint(0, r)
score = 0

while True:
    score +=1
    you = input("make a guess: ")
    if you.isdigit():
        you = int (you)
    else:
        print("plz type a number next time")
        continue

    if you == no :
        print ("you got it!!!!")
        break
    elif you > no:
        print ("you are above the number!")
    else:
        print ("you are below the number!")

print("you got it in",score,"giesses")

