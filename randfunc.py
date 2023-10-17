import random

# #52
# print(random.randrange(1,100))

# #53
# def randfruit():
#     counter = 0
#     fruitlist = []
#     while counter<5:
#         fruitlist.append(input("Input a fruit"))
#         counter += 1
#     fruitindex = random.randrange(0,4)
#     print(fruitlist[fruitindex])
# randfruit()

# #54
# def coinflip():
#     options =["h","t"]
#     guess = input("Is it heads or tails?")
#     true = random.choice(options)
#     if guess == "t" or guess == "h":
#         if guess ==  true:
#             print("You win")
#         else:
#             print("Bad luck")
#     else:
#         print("Input h or t")
#         coinflip()
# coinflip()

# #55
# def guessnumber():
#     limit = int(input("How many guesses do you have"))
#     randomnum = random.randrange(1,5)
#     print(randomnum)
#     guessed = 0
#     while guessed != limit:
#         guess = int(input("Input your guess"))
#         if guess == randomnum:
#             print("Well done")
#             break
#         elif guess < randomnum:
#             print("Your guess is to low")
#             guessed += 1
#         else:
#             print("Your guess is to high")
#             guessed += 1
#     if guessed == limit:
#         print("You lose")
# guessnumber()

# #56
# def guessnumber():
#     randomnum = random.randrange(1,10)
#     print(randomnum)
#     guess = ""
#     while guess != randomnum:
#         guess = int(input("Input your guess"))
#         if guess == randomnum:
#             print("Well done")
#             break
#         elif guess < randomnum:
#             print("Your guess is to low")
#         else:
#             print("Your guess is to high")
# guessnumber()

# #58
# def mathquiz():
#     turn = 0
#     score = 0
#     while turn != 5:
#         randnum1 = random.randrange(1,100)
#         randnum2 = random.randrange(1,100)
#         randsum = randnum1 + randnum2
#         print(randnum1,"+",randnum2)
#         answer = int(input(("What is you answer")))
#         if answer == randsum:
#             score += 1
#         turn += 1
#     print("You got ",score,"right out of 5")
# mathquiz()

# #59
# def pickcolors():
#     colors = ["red","green","blue","yellow","black"]
#     rightone = random.choice(colors)
#     guess = ""
#     counter = 0
#     
#     print("Available colors:")
#     print(", ".join(colors))
#     while guess != rightone:
#         if counter == 0:
#             guess = input("Guess a color")
#             counter += 1
#         else:
#             print(rightone)
#             guess = input("Guess a color")
#     print("Well done")
# pickcolors()























