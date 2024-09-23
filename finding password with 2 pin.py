import random


combinations = [] #creating the array that will contain all the combinations

print("Catalog") # printing the catalog of colors it will be used
print("Y - Yellow")
print("R - Red")
print("B - Blue")
print("G - Green")
print("O - Orange")
print("P - Purple")
print("k - Pink")


i = 0 #defining the variable that will tell the programm when it reached all the possibilities

while i < 42: #while it doesn't put all the 840 combinations in the array, it will continue adding combinations

    list = [0,1,2,3,4,5,6] #creating the list to randomly pick one color in the variable colors
    repeated = 0 #defining the variable that will say to the program if it repeated or not
    Colors = "YRBGOPK" #defining the colors based on the catalog

    First = random.choice(list) #randomly selecting the color that will be in the first position
    list.remove(First) #deleting it from the list, so it cannot repeat
    Second = random.choice(list) #randomly selecting the color that will be in the second position
    #list.remove(Second) #deleting it from the list, so it cannot repeat
    #Third = random.choice(list) #randomly selecting the color that will be in the third position
    #list.remove(Third) #deleting it from the list, so it cannot repeat
    #Fourth  = random.choice(list) #randomly selecting the color that will be in the fourth position


    #combining all the colors with their position in one single string variable "Password"
    Password = Colors[First] + Colors[Second] #+ Colors[Third] + Colors[Fourth]
    
    t = 0 #defining the variable that will tell the program when it reached all 
    #combinations that were already created and added in the "combinations" list

    while t < i: #it will work until it has checked all the elements from the list

        if Password == combinations[t]: #if there is an element in the list that 
            #is equal to the Password, it will not be added 
            repeated = 1 #saying to the program that it repeated
            t = i #with this it will break the condition "while t < 1"

        else: #if the "password" not equal to the t element from the list
            #it will see if it is equal to the t + 1 element

            t = t + 1


    if repeated == 0: #if it didn't repeat with any of the elements from the list
        combinations.append(Password) #it will add the password to the list "combinations"
        i = i + 1 #it will tell the condition "while i< 840" that it added one element

print(combinations) #print all the combinations
print(len(combinations)) #print the lenght of the list
#meaning it has this quantity of combinations


i = 0
while i < 7:
    guess = random.choice(combinations)
    print(guess)
    print("How many white Pins I got?")
    whitePins = int(input())
    print("How many Black Pins I got?")
    blackPins = int(input())
    t = 0
    i = i + 1
    lenght = len(combinations) #defining the lenght of the list ofcombinations
    #The condition if it is right with 2 Black pins

    if blackPins == 2:
        print("WOw, I got it!")
        i = 12

    #The condition for NO black pins and NO White pin 

    if blackPins == 0 and whitePins == 0:
        print(" NO Pins")
        while t < lenght:
                
            if guess[0] == combinations[t][1] or guess[0] == combinations[t][0] or guess[1] == combinations[t][0] or guess[1] == combinations[t][1]:
            
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    


    #The condition for NO black pin and for 1 White pin
 
    if blackPins == 0 and whitePins == 1:
        while t < lenght:
            if  guess[0] == combinations[t][0] or guess[1] == combinations[t][1] or (guess[0] != combinations[t][1] and guess[1] != combinations[t][0]) or (guess[0] == combinations[t][1] and guess[1] == combinations[t][0]):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1
        
       
        


    #The condition for 1 black pin and for NO White pin

    if blackPins == 1 and whitePins == 0:
        while t < lenght:
            if  guess[0] == combinations[t][1] or guess[1] == combinations[t][0] or (guess[0] != combinations[t][0] and guess[1] != combinations[t][1]) or (guess[0] == combinations[t][0] and guess[1] == combinations[t][1]):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1
        
       


    #The condition for NO black pin and for 2 White pins

    if blackPins == 0 and whitePins == 2:
        while t < lenght:
            if  guess[0] != combinations[t][1] or guess[1] != combinations[t][0] or guess[1] == combinations[t][1] or guess[0] == combinations[t][0]:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1
    
    
print(guess)
print(combinations)