# binary search algorithm
"""
def binarySearch(list, min, max, sucheZahl):
    if (max >= min):
        average = min + (max - min) // 2
        if (list[average] == sucheZahl):
            return "Deine Zahl ist auf Position: " + str(average)
        elif sucheZahl < list[average]:
            return binarySearch(list, min, average - 1, sucheZahl)
        else:
            return binarySearch(list, average + 1, max, sucheZahl)
    return -1

print(len(liste))
print(binarySearch(liste, 0, len(liste) - 1, 60))
print("erfolgreich!")

"""

"""
def binarerSuchalgo(list, minimum, maximum, searchnumber):
    average = (minimum + maximum) // 2
    if list[average] == searchnumber:
        return average
    elif list[average] < searchnumber:
        return binarerSuchalgo(list, average + 1, maximum, searchnumber)
    elif list[average] > searchnumber:
        return binarerSuchalgo(list, minimum, average - 1, searchnumber)
    return 
"""
liste = [562551, 648089, 339130, 232781, 741380, 318831, 54992, 352816, 473167, 871875, 822883, 769831, 769795, 910486, 262411, 16616, 111308, 855010, 133145, 18471, 233827, 166301, 118410, 41657, 225752, 567000, 743300, 421021, 128901, 2581, 906942, 255479, 719664, 534727, 173262, 810868, 957850, 896822, 740136, 627019, 772771, 893088, 973212, 688083, 757671, 265944, 308961, 992189, 700244, 404376, 343584, 794865, 676782, 572793, 640883, 842154, 612439, 209600, 776112, 774328, 250026, 338578, 700102, 449928, 288668, 674190, 574430, 327560, 631379, 896249, 507176, 913321, 415626, 253597, 493538, 838210, 516806, 94771, 728345, 586015, 337451, 690976, 605421, 534582, 278378, 93158, 412830, 392979, 579541, 673885, 959114, 397658, 764557, 508706, 764384, 505615, 622364, 992458, 730627, 736306]
def binarerSuchAlgoRichtig(list, searchnumber):
    maximum = len(list) - 1
    minimum = 0 
    while True:
        average = (minimum + maximum) // 2
        if list[average] == searchnumber:
            position = average
            break
        elif list[average] < searchnumber:
            minimum = average + 1
        elif list[average] > searchnumber:
            maximum = average - 1
    return position

liste.sort()

def findNumberWhenInList(list, searchnumber):
    NummerDrinnen = False
    if searchnumber in list:
        NummerDrinnen = True
    if not NummerDrinnen:
        print("Nope nichts drinnen")
    else:
        return binarerSuchAlgoRichtig(list, searchnumber)

wantedNumber = input("Welche Zahl suchst du?\n")
positionWantedNumber = findNumberWhenInList(liste, int(wantedNumber))
print(positionWantedNumber)