import random
import os
# #118
# def entern():
#     num = int(input("Enter a number"))
#     return num
# 
# def count(num):
#     x = 1
#     while not x>num:
#         print(x)
#         x += 1
# 
# x = entern()
# y = count(x)

# #119
# def rand():
#     lown = int(input("Enter a low number"))
#     highn = int(input("Enter a high number"))
#     comp_num = random.randrange(lown,highn)
#     return comp_num
# 
# def guess():
#     print("I am thinking of a number...")
#     inpguess = int(input("Guess a number"))
#     return inpguess
#     
# def check(comp_num,inpguess):
#     while not comp_num == inpguess:
#         if comp_num < inpguess:
#             print("Your number is too high")
#             inpguess = int(input("guess again"))
#         else:
#             print("Your number is too low")
#             inpguess = int(input("guess again"))
#     print("Correct, you win")
# 
# comp_num = rand()
# inpguess = guess()
# k = check(comp_num,inpguess)

# #120 
# def add():
#     rnum1 = random.randrange(5,20)
#     rnum2 = random.randrange(5,20)
#     print(rnum1)
#     print(rnum2)
#     userans = int(input("Add the numbers together"))
#     corrans = rnum1 + rnum2
#     print(userans,corrans)
#     ans = [userans,corrans]
#     return ans
# def sub():
#     rnum1 = random.randrange(25,50)
#     rnum2 = random.randrange(1,25)
#     print(rnum1)
#     print(rnum2)
#     userans = int(input("Minus the second number from the first"))
#     corrans = rnum1 - rnum2
#     ans = [userans,corrans]
#     print(ans)
#     return ans
# def checkans(ans):
#     if ans[0] == ans[1]:
#         print("Correct")
#     else:
#         print("Incorrect, the answer is", ans[1])
# 
# print("1) Addition")
# print("2) Subtraction")
# choiche = int(input("Enter 1 or 2:"))
# if choiche == 1:
#     addans =  add()
#     check = checkans(addans)
# elif choiche == 2:
#     subans = sub()
#     check = checkans(subans)
# else:
#     print("You did not select a relevant option, run the program again")

# #121
# names = []
# def addn(names):
#     newname = input("Give the name you want to add\n")
#     names = names.append(newname)
# 
# def changn(names):
#     x = 0
#     changename = input("Input what name you want to change\n")
#     while x<len(names):
#         if names[x] == changename:
#             pos = x
#             names.pop(x)
#         else:
#             x += 1
#     changedname = input("Input what do you want to change it to\n")
#     names.insert(pos,changedname)
#     
# def deln(names):
#     x = 0
#     delname = input("Input what name you want to delete\n")
#     while x<len(names):
#         if names[x] == delname:
#             names.pop(x)
#             break
# def alln(names):
#     print("\n")
#     for x in names:
#         print(x)
#         
# menu = 0
# while menu != 5:
#     print("1) Add name to a list\n2) change a name on the list\n3) deleta a name from the list\n4) view all names in the list\n5) end the program")
#     menu = int(input("Enter 1 or 2 or 3 or 4 or 5:"))
#     if  menu == 1:
#         addname = addn(names)
#     elif menu == 2:
#         changename = changn(names)
#     elif menu == 3:
#         delname = deln(names)
#     elif menu == 4:
#         allnames = alln(names)
#     else:
#         print("You did not select a relevant option")
    

#122/123

def addf():
    f = open("Salaries.csv","a")
    addn = input("Input your name")
    adds = input("Input your salary\n")
    addboth = addn + "," + adds
    f.write(addboth+"\n")
    f.close()
def viewf():
    f = open("Salaries.csv","r")
    for line in f:
        print(line)
    f.close()
def delf():
    templ = []
    f = open("Salaries.csv","r")
    for line in f:
        templ.append(line)
    f.close()
    f = open("Salaries.csv","w")
    deln = input("Input the name you want to delete")
    dels = input("Input the salary that is associated with the name")
    delboth = deln + "," + dels
    x = 0
    while x<len(templ):
        if templ[x] == delboth + "\n":
            templ.pop(x)
            break
        else:
            x += 1
    l = 0
    while l< len(templ):
        f.write(templ[l]+"\n")
        l += 1
    f.close()



menu = 0
while menu != 4:
    print("1) Add to file\n2) View all records\n3) Delete a file\n4) Quit program")
    menu = int(input("Enter the number of your selection"))
    if menu == 1:
        addfile = addf()
    elif menu == 2:
        viewfile = viewf()
    elif menu == 3:
        delfile = delf()
    else:
        print("You did not select a relevant option")
    




























