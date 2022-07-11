zuSuchendesWort = input("Welches Wort soll erraten werden?\n")
gewahlteBuchstaben = []
darstellungDesWorts = []
# Darstellung des Worts
for buchstabe in zuSuchendesWort:
    if buchstabe in gewahlteBuchstaben:
        darstellungDesWorts.append(buchstabe)
    else:
        darstellungDesWorts.append("_")
print(*darstellungDesWorts, end="\n\n")

falschAnzahl = 5
anzahl = 0

# Spiel indem man die ganze Zeit weiterrät bis man das Wort gefunden hat!
while True:
    darstellungDesWorts = []
    rateBuchstabe = input("Welcher Buchstabe soll es sein?\n")
    
    if len(rateBuchstabe) > 1:
        print("ZUUUU VIEEEELEEEE BUUUCHSSTTAAAABEEEEEN!\n\n")
        continue

    elif rateBuchstabe in gewahlteBuchstaben:
        print("Kiddin? Hast du doch schon mal gesagt!\n\n")
        continue
    elif rateBuchstabe not in zuSuchendesWort:
        gewahlteBuchstaben.append(rateBuchstabe)
        anzahl += 1
        print("Du hast schon " + str(anzahl) + " Fehler. du darfst nur " + str(falschAnzahl) + " machen.\n\n")
    else:
        gewahlteBuchstaben.append(rateBuchstabe)


    for buchstabe in zuSuchendesWort:
        if buchstabe in gewahlteBuchstaben:
            darstellungDesWorts.append(buchstabe)
        else:
            darstellungDesWorts.append("_")

    print(*darstellungDesWorts, end="\n\n")
    if anzahl == falschAnzahl:
        print("gameOver")
        break
    if "_" not in darstellungDesWorts:
        print("gewonnnen")
        break


#print(type("".join(darstellungDesWorts)))