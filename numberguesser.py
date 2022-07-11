import random

print("Sag uns die Range der Zahl")
beginRange = int(input("AnfangsRange eingeben:"))
endRange = int(input("EndRange eingeben:"))

zuRatendeZahl = random.randint(beginRange, endRange)

print("Nun rate mal welche Zahl ich gewählt habe!")

while True:
    gerateneNummer = int(input('Nun Rate:')) 
    
    if gerateneNummer != zuRatendeZahl and gerateneNummer < zuRatendeZahl:
        print("Meine Zahl ist grösser!", end="\n\n\n")
    elif gerateneNummer != zuRatendeZahl and gerateneNummer > zuRatendeZahl:
        print("Meine Zahl ist kleiner!", end="\n\n\n")
    else:
        print("Du hast gewonnen! Ich habe wirklich " + str(zuRatendeZahl) + " gewählt")
        break

