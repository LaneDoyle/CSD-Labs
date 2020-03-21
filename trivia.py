#!/usr/bin/python3
#LaneDoyle
#3/20/2020

'''Program to create a trivia game'''

score = 0

print("******* TRIVIA GAME *******")
print(" ")


print("1. What was the first LifeSaver flavor? \n a. Grape \n b. Peppermint \n c. Cherry \n d. Pineapple")

answer_one = input("Your answer: ")

if answer_one.lower() == "b":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
print(" ")


print("2. The city known as Hot Coffee is located in what US state? \n a. Missouri \n b. California \n c. New York \n d. Mississippi")

answer_two = input("Your answer: ")

if answer_two.lower() == "d":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
print(" ")    

    
print("3. What snack is Tallahassee searching for in the 2009 film Zombieland? \n a. Twinkies \n b. Little Debbie's \n c. Unicorn Cakes \n d. Chips")

answer_three = input("Your answer: ")

if answer_three.lower() == "a":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
print(" ")    

    
print("4. What is Shakespeares shortest tragedy? \n a. Macbeth \n b. Othello \n c. Hamlet \n d. Julius Ceasar")

answer_four = input("Your answer: ")

if answer_four.lower() == "a":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
print(" ")  
    
    
print("5. In what decade was the voting age in the US lowered to 18? \n a. 1920s \n b. 1980s \n c. 1970s \n d. 1940s")

answer_five = input("Your answer: ")

if answer_five.lower() == "c":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
print(" ")
    
percentage = (score / 5) * 100

print("Your percentage: ", percentage)
print("You got: ", score, "out of 5 correct!")