# #1
# nums = [1,2,3,4,5,6,7]
# x = 0
# def sum1(x,nums):
#     if  x != len(nums):
#         return nums[x]+ sum1(x+1,nums)
#     else:
#         return 0
# y = sum1(x,nums)
# print(y)

# #2
# f = int(input("Give a number(factorial)"))
# def fact(f):
#     if f == 1:
#         return 1
#     else:
#         return f*fact(f-1)
# print(fact(f))

# #3
# nterm= int(input("Which term to find?"))-2
# x = 0
# term0 = 0
# term1 = 1
# def fib(x,term0,term1,nterm):
#     term2 = term0 + term1
#     if x == nterm:
#         return term1
#     else:
#         return fib(x+1,term1,term2,nterm)
# print(fib(x,term0,term1,nterm))
# #3/b
# nterm= int(input("Which term to find?"))-1
# def fib2(nterm):
#     term0 = 0
#     term1 = 1
#     if nterm == 0:
#         return term0
#     if nterm == 1:
#         return term1 + fib2(nterm-1)
#     else:
#         return fib2(nterm-1) + fib2(nterm-2)
# print(fib2(nterm))
    
# #4
# num = input("Input a positive number")
# def sumdig(num):
#     if num[0:] == "":
#         return 0
#     else:
#         return int(num[0]) + int(sumdig(num[1:]))
# print(sumdig(num))
    
# #5
# num1gcd = int(input("Input number 1\n"))
# num2gcd = int(input("Input number 2\n"))
# def gcd(num1gcd,num2gcd):
#     if num1gcd == num2gcd:
#         return num1gcd
#     else:
#         if num1gcd<num2gcd:
#             return gcd(num1gcd,num2gcd-num1gcd)
#         else:
#             return gcd(num2gcd,num1gcd-num2gcd)
# print(gcd(num1gcd,num2gcd))
        
# #6
# lcm1 = int(input("Input numer 1\n"))
# lcm2 = int(input("Input numer 2\n"))
# x = 0
# y = 0
# def lcm(lcm1,lcm2,x,y):
#     if lcm1 == lcm2:
#         return lcm1
#     else:
#         if lcm1<lcm2:
#             x += 1
#             return lcm(lcm1+lcm1/x,lcm2,x,y)
#         else:
#             y += 1
#             return lcm(lcm1,lcm2+lcm2/y,x,y)
# print(lcm(lcm1,lcm2,x,y))
    
# #7
# sumoddinp = int(input("Give a number"))
# sumoddcount = 0
# def sumodd(sumoddinp,sumoddcount):
#     if sumoddinp <= 0:
#         return 0
#     elif sumoddcount == 0:
#         sumoddcount += 1 
#         if sumoddinp%2 == 0:
#             return sumodd(sumoddinp-1,sumoddcount)
#         else:
#             return sumodd(sumoddinp-2,sumoddcount)
#     else:
#         return sumoddinp + sumodd(sumoddinp-2,sumoddcount)
# print(sumodd(sumoddinp,sumoddcount))

# #8
# divdown = int(input("For which positive intiger find the sum of the reciprocal\n"))
# def sumrec(diwdown):
#     if diwdown == 1:
#         return 1
#     else:
#         return 1/diwdown + sumrec(diwdown-1)
# print(sumrec(divdown))

# #9
# pieterm = int(input("How many times approximatiat"))
# piecount = 0
# piediv = 1
# def pieapprox(pieterm,piecount,piediv):
#     if piecount == pieterm-1:
#         return 4/piediv
#     else:
#         if piecount % 2 == 0:
#             return 4/piediv + pieapprox(pieterm,piecount+1,piediv+2)
#         else:
#             return -4/piediv + pieapprox(pieterm,piecount+1,piediv+2)
# print(pieapprox(pieterm,piecount,piediv))
# 
# #10
# 
# def fact(f):
#     if f == 1:
#         return 1
#     else:
#         return f*fact(f-1)
# 
# eulerinp = int(input("How accourate should be eulers constant?"))-1
# def euler(inp):
#     if inp == 0:
#         return 1
#     else:
#         return 1/fact(inp) + euler(inp-1)
# print(euler(eulerinp))

# #11
# collatzinp = int(input("Where to start the sequence"))
# def collatz(inp):
#     while inp <= 0:
#         print("Give a positive number")
#         inp = int(input("Where to start the sequence"))
#     while inp != 1:
#         if inp % 2 == 0:
#             inp = inp/2
#         else:
#             inp = 3*inp +1
#     return inp
# print(collatz(collatzinp))

# #12
# 
# def multipl(inp,sum1,counter,lim,list1):
#     if counter == 0:
#         list1 = []
#         sum1 = 0
#         counter = 1
#     if inp >= lim:
#         return sum1,list1
#     else:
#         list1.append(inp)
#         return multipl(inp + inp/counter,sum1 + inp,counter + 1,lim,list1)
# def both(multinp,sum1,counter,multlim,list1):
#     sumboth = 0
#     bothlist = []
#     for x in multinp:
#         _,listy =  multipl(x,sum1,counter,multlim,list1)
#         for x in listy:
#             bothlist.append(x)
#     for x in bothlist:
#         count = 0
#         for y in bothlist:
#             if x == y:
#                 count += 1
#         if count>1:
#             sumboth += x
#     return sumboth/2
# def multiplsum():
#     addnums = int(input("How many numbers do you want to add its multiples sums"))
#     l = 0
#     allsum = 0
#     multinp = []
#     sum1 = 0
#     counter = 0
#     list1 = []
#     bothlist = []
#     multlim = int(input("Input limit"))
#     while l<addnums:
#         multinp.append(int(input("Number to sum of all multiples")))
#         l += 1
#     for x in multinp: 
#         sum1, _ =  multipl(x,sum1,counter,multlim,list1)
#         allsum += sum1
#     allsum = allsum - both(multinp,sum1,counter,multlim,list1)
#     return allsum
# 
# print(multiplsum())

# #13
# def divid(num1,div,counter):
#     if counter == 0:
#         div = num1
#         counter += 1
#         return 0 + divid(num1,div-1,counter)
#     if div == 1:
#         return 1
#     else:
#         if num1 % div == 0:
#             return div + divid(num1,div-1,counter)
#         else:
#             return 0 + divid(num1,div-1,counter)
# def findperfect():
#     div = 0
#     counter = 0
#     counterfunc = 0
#     num1 = 1
#     found = 0
#     perffact = []
#     perflimit = int(input("How many perfect factors to find"))
#     while perflimit != found:
#         if counter == 0:
#             num1 = 2
#             counter += 1
#         if num1 == divid(num1,div,counterfunc):
#             perffact.append(num1)
#             found += 1
#         num1 += 1
#     return perffact
# print(findperfect())

# #14
# def divid(inpnum,div,counter):
#     if counter == 0:
#         div = inpnum
#         counter += 1
#         return 0 + divid(inpnum,div-1,counter)
#     if div == 1:
#         return 1
#     else:
#         if inpnum % div == 0:
#             return div + divid(inpnum,div-1,counter)
#         else:
#             return 0 + divid(inpnum,div-1,counter)
# def amic():
#     pair1 = int(input("Input number 1 of pair to be checked"))
#     pair2 = int(input("Input number 2 of pair to be checked"))
#     div = 0
#     counterfunc = 0
#     if pair1 == divid(pair2,div,counterfunc) and pair2 == divid(pair1,div,counterfunc):
#         return "true"
#     else:
#         return "false"
# print(amic())
   
    
    
    
    
    
    
    
    
