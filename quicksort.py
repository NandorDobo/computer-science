def main():
    unsortedlist = []
    limit = int(input("How many numbers in the list"))
    for x in range(limit):
        unsortedlist.append(int(input("Input number")))
    print(quicksort(unsortedlist))    

def quicksort(unsortedlist):
    if len(unsortedlist) <= 1:
        return unsortedlist
    else:
        pivot = unsortedlist.pop(len(unsortedlist)-1)
        leftlist = []
        middlelist = []
        rightlist = []
        middlelist.append(pivot)
        while len(unsortedlist) != 0:
            if unsortedlist[0]<pivot:
                leftlist.append(unsortedlist.pop(0))
            elif unsortedlist[0] == pivot:
                middlelist.append(unsortedlist.pop(0))
            else:
                rightlist.append(unsortedlist.pop(0))
        return quicksort(leftlist) + middlelist + quicksort(rightlist)
main()