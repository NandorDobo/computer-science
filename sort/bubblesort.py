def bubblesort(inplist,limit):
    if limit == -2:
        numslen =int(input("How many numbers are in the list?"))
        limit = numslen - 1
        for x in range(numslen):
            inplist.append(int(input("Input number\n")))
            x += 1
    if limit == 0:
        return inplist
    else:
        counter = 0
        print(inplist)
        for x in range(len(inplist[:limit])):
            if inplist[x] > inplist[x+1]:
                value1 =  inplist.pop(x)
                inplist.insert(x+1,value1)
                counter += 1
        if counter == 0:
            return inplist
        return bubblesort(inplist,limit-1)
print(bubblesort([],-2))