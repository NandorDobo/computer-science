n1 = 12
n2 = 24
n3 = 36
n4 = 48
tot = n1+n2+n3+n4
print(tot)

fh = open("daffodils.txt")
length = 0
for line in fh:
    print(line.strip())
    length += 1
print(length)
fh.close

fh1 = open("num_calc_1.txt")
tot1 = 0
leng1 = 0
for line in fh1:
    line = line.strip()
    if line.isdigit():
        tot1 += int(line)
        leng1 += 1
print(tot1)
print(leng1)
mean1 = tot1/leng1
print(mean1)
fh1.close()


fh2 = open("num_calc_2.txt")
tot2 = 0
leng2 = 0
for line in fh2:
    line = line.strip()
    if(line.isdigit()):
        tot2 += int(line)
        leng2 += 1
print(tot2)
print(leng2)
mean2= tot2/leng2
print(mean2)
fh2.close()

# total3 = 0
# l = 0
# while l<20:
#     t = int(input("Give a number"))
#     total3 += t
#     l += 1
# mean3 = total3/20
# print(mean3)

k = 0
f2 = open("f2.txt","w")
while k<10:
    inp = int(input("Give a number"))
    f2.write(str(inp))
    f2.write("\n")
    k += 1
f2.close()
f2 = open("f2.txt","r")
tot5 = 0
leng5 = 0
for line in f2:
    line = line.strip()
    if(line.isdigit()):
        tot5 += int(line.strip())
        leng5 +=1
mean5 = tot5/leng5
print(mean5)
f2.close()





