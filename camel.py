#!/usr/bin/python3
#LaneDoyle
#3/21/2020

'''Program to play the game Camel'''

import random as rd

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! \nSurvive your desert trek and out run the natives.")
print(" ")
print(" ")

done = False
miles_traveled = 0
thirst_level = 0
camel_exhaustion = 0
natives_distance = 20
drinks_left  = 5



while done is False:

    print("A. Drink from your canteen.")
    print("B. Move ahead at moderate speed.")
    print("C. Move ahead at full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print(" ")
    
    user_input = input("What would you like to do? ")
    
    if user_input.lower() == "q":
        done = True
        
    elif user_input.lower() == "e":
        print(" ")
        print("Miles traveled:", miles_traveled)
        print("Drinks left in your canteen:", drinks_left)
        print("The natives are", natives_distance, "miles behind you")
        print(" ")
        
    elif user_input.lower() == "d":
        random_miles = rd.randint(7, 15)
        natives_distance -= random_miles
        camel_exhaustion = 0
        print(" ")
        print("Your camel appears well rested!")
        print("The natives are now", natives_distance, "miles behind you")
        print(" ")
        
    elif user_input.lower() == "c":
        random_traveled = rd.randint(10, 15) 
        miles_traveled += random_traveled
        natives_distance += random_traveled
        random_miles = rd.randint(7, 20)
        natives_distance -= random_miles
        thirst_level += 1
        random_exhaustion = rd.randint(1, 3) 
        camel_exhaustion += random_exhaustion
        print(" ")
        print("You traveled", miles_traveled, "miles.")
        print("The natives are now", natives_distance, "miles behind you")
        print(" ")
    
    elif user_input.lower() == "b":
        random_traveled = rd.randint(5, 10) 
        miles_traveled += random_traveled
        natives_distance += random_traveled
        random_miles = rd.randint(7, 20)
        natives_distance -= random_miles
        thirst_level += 2
        camel_exhaustion += 2
        print(" ")
        print("You traveled", miles_traveled, "miles.")
        print("The natives are now", natives_distance, "miles behind you")
        print(" ") 
    
    elif user_input.lower() == "a":
        if drinks_left == 0:    
            print("You have no water left in your canteen.")
        else:
            thirst_level = 0
            drinks_left -= 1
            print(" ")
            print("You feel refreshed.")
            print(" ")
            
    if miles_traveled >= 200:
        print(" ")
        print("You escaped! Congrats!")
        print(" ")
        done = True
            
    if not done and thirst_level > 4:
        print(" ")
        print("You are thirsty!")
        print(" ")
        
    elif not done and thirst_level > 6:
        print(" ")
        print("You have died of thirst.")
        print(" ")
        done = True
    
    if not done and camel_exhaustion > 5:
        print(" ")
        print("Your camel looks exhausted!")
        print(" ")
        
    elif not done and camel_exhaustion > 8:
        print(" ")
        print("Your camel has died.")
        print(" ")
        done = True
        
    if not done and natives_distance <= 0:
        print(" ")
        print("The natives have captured you.")
        print(" ")
        done = True
    
    elif not done and natives_distance < 15:
        print(" ")
        print("The natives are getting close!")
        print(" ")
        
    percentage = rd.randint(1, 100)  
    
    if not done and percentage <= 20:
        print(" ")
        print("You have found an oasis!")
        print("You are able to refill your canteen.")
        print("Your camel has rested.")
        print(" ")
        camel_exhaustion = 0
        thirst_level = 0
        drinks_left += 2
        
        
    
    

