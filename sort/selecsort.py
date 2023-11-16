def selecsort(inplist,marker):
    if marker == 0:
        limit = int(input("How many numbers in list"))
        for x in range(limit):
            inplist.append(int(input("Input number\n")))
            x += 1    
    if marker == len(inplist):
        return inplist
    else:
        smallestindex = marker
        c = marker
        smallest = inplist[marker]
        while c != len(inplist):
            if inplist[c] < smallest:
                smallest = inplist[c]
                smallestindex = c
                print(smallestindex)
            c += 1
        if smallestindex == marker:
            return selecsort(inplist,marker+1)
        else:
            org = inplist.pop(marker)
            inplist.insert(marker,inplist.pop(smallestindex-1))
            inplist.insert(smallestindex,org)
        return selecsort(inplist,marker+1)
print(selecsort([],0))

    
    
    
    
    
    
    
        