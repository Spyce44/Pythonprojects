import random

story = "Pizza wurde von einem ADJECTIVE NATION Koch erfunden, der NAME hieß.\n Um Pizza zu machen, fängt man einen Klumpen ein NOMEN an und rollt ihn in dünnen, runden, ADJECTIVE Scheiben.\n Darauf verteilt man ADJECTIVE Sauce sowie ADJECTIVE Käse und frisch geschnitten NOMEN.\n Danach muss man die Pizza in ein sehr heiß NOMEN backen.\n Wenn sie fertig ist, schneidet man sie in ZAHL FORM.\n Manchen Kindern schmeckt ESSEN Pizza am besten, aber meine Lieblingspizza ist ESSEN-Pizza.\n Wenn ich könnte, würde ich ZAHL Mal am Tag Pizza essen."
words =  {
    "adjectiv": ["achtsam","baff","chemisch","dankbar","dazugehörig"],
    "name": ["Allessandro","Antke","Ben","Bela","Aini"],
    "nation": ["deutsch","arabisch","kurdisch","albanisch","frankzösisch"],
    "nomen": ["Tisch","Zeitung","Auto","Mutter","Vater"],
    "zahl": [random.randint(1,100)],
    "essen": ["Kartoffeln","Fleisch","Hund","Pferd","Döner"],
    "form": ["Feld","Viereck","Kreis","Rechteck","Ellipse"],
}

listenStory = story.split(" ")

lengthAdj = len(words["adjectiv"])
lengthName = len(words["name"])
lengthNation = len(words["nation"])
lengthNomen = len(words["nomen"])
lengthZahl = len(words["zahl"])
lengthEssen = len(words["essen"])
lengthForm = len(words["form"])


for elementPosition in range(len(listenStory)):
    if listenStory[elementPosition] == "ADJECTIVE":
        listenStory[elementPosition] = words["adjectiv"][random.randint(0,lengthAdj-1)]

    elif listenStory[elementPosition] == "NAME":
        listenStory[elementPosition] = words["name"][random.randint(0,lengthName-1)]

    elif listenStory[elementPosition] == "NATION":
        listenStory[elementPosition] = words["nation"][random.randint(0,lengthNation-1)]

    elif listenStory[elementPosition] == "NOMEN":
        listenStory[elementPosition] = words["nomen"][random.randint(0,lengthNomen-1)]

    elif listenStory[elementPosition] == "ZAHL":
        listenStory[elementPosition] = str(words["zahl"][random.randint(0,lengthZahl-1)])

    elif listenStory[elementPosition] == "ESSEN":
        listenStory[elementPosition] = words["essen"][random.randint(0,lengthEssen-1)]

    elif listenStory[elementPosition] == "FORM":
        listenStory[elementPosition] = words["form"][random.randint(0,lengthForm-1)]
    else:
        continue

print(" ".join(listenStory))