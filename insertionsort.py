def insertsort():
    unsortedlist = []
    limit = int(input("Input how many numbers in the list"))
    for x in range(limit):
        unsortedlist.append(int(input("Input number")))
    sortedlist = []
    sortedlist.append(unsortedlist.pop(0))
    while len(unsortedlist) != 0:
        sortedlist.append(unsortedlist.pop(0))
        x = len(sortedlist)-1
        while sortedlist[x]<sortedlist[x-1]:
            switch1 = sortedlist.pop(x-1)
            sortedlist.insert(x,switch1)
            x -= 1
    return sortedlist
print(insertsort())