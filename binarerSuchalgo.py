# binary search algorithm

liste = [1,7,10,20,48,50,60,100]

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

