file = open("mean-median-mode-frequency.csv","r")
x = 0
lin0 = []
lin1 = []
lin2 = []
for line in file:
    data = line.strip()
    data = data.split(",")
    if len(data) != 1:
        if x == 0:
            lin0 = data
        if x == 1:
            lin1 = data
        if x == 2:
            lin2 = data
        x += 1 
print(lin0)
print(lin1)
print(lin2)

def convert(inplist):
    return[int(item) for item in inplist]
lin0 = convert(lin0)
lin1 = convert(lin1)
lin2 = convert(lin2)

def mean(numbers):
    add = sum(numbers)
    mean1 = add/len(numbers)
    return mean1

def median(numbers):
    numbers.sort()
    half = len(numbers)/2
    if len(numbers)%2 == 0:
        half = int(half)
        median1 = (numbers[half]+numbers[half+1])/2
    else:
        median1 = numbers[int(half-0.5)]
    return median1

def dicti(numbers):
    nums = {}
    for x in numbers:
        nums[x] = nums.get(x, 0) + 1
    return nums

def mode(nums):
    big = {"base":-999999999}
    k, = big.keys()
    for key0 in nums:
        if big[k] < nums[key0]:
            big.clear()
            big[key0] = nums[key0]
            k, = big.keys()
        elif big[k]== nums[key0]:
            big[key0] = nums[key0]
            k, = big.keys()
    return big
                
    




lin0mea = mean(lin0)
lin1mea = mean(lin1)
lin2mea = mean(lin2)

print (lin0mea)
print (lin1mea)
print (lin2mea)


lin0med = int(median(lin0))
lin1med = int(median(lin1))
lin2med = int(median(lin2))

print (lin0med)
print (lin1med)
print (lin2med)

lin0dicti = dicti(lin0)
lin1dicti = dicti(lin1)
lin2dicti = dicti(lin2)

print(lin0dicti)
print(lin1dicti)
print(lin2dicti)

lin0mod = mode(lin0dicti)
lin1mod = mode(lin1dicti)
lin2mod = mode(lin2dicti)
print(lin0mod)
print(lin1mod)
print(lin2mod)

file.close()    