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
#print("E - Empty")


i = 0 #defining the variable that will tell the programm when it reached all the possibilities

while i < 840: #while it doesn't put all the (840 combinations for 7 colors and 1680 for 8 colors) in the array, it will continue adding combinations

    list = [0,1,2,3,4,5,6] #creating the list to randomly pick one color in the variable colors
    repeated = 0 #defining the variable that will say to the program if it repeated or not
    Colors = "YRBGOPK" #defining the colors based on the catalog

    First = random.choice(list) #randomly selecting the color that will be in the first position
    list.remove(First) #deleting it from the list, so it cannot repeat
    Second = random.choice(list) #randomly selecting the color that will be in the second position
    list.remove(Second) #deleting it from the list, so it cannot repeat
    Third = random.choice(list) #randomly selecting the color that will be in the third position
    list.remove(Third) #deleting it from the list, so it cannot repeat
    Fourth  = random.choice(list) #randomly selecting the color that will be in the fourth position


    #combining all the colors with their position in one single string variable "Password"
    Password = Colors[First] + Colors[Second] + Colors[Third] + Colors[Fourth]
    
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

#print(combinations) #print all the combinations


i = 0 #redefing variable i for another purpose, now it's to count the tentatives
while i < 10: #He has 10 tries
    t = 0
    lenght = len(combinations) #defining the lenght of the list ofcombinations
    #print(lenght) #print the lenght of the list
    #meaning it has this quantity of combinations


    guess = random.choice(combinations)
    print(guess)

    print("How many white Pins I got?")
    whitePins = int(input())

    print("How many Black Pins I got?")
    blackPins = int(input())
    
    i = i + 1
    
    
    #The condition if it is right with 2 Black pins

    if blackPins == 4:
        print("WOw, I got it in",i,"tentatives!")
        i = 12

    #The condition for 0 white pins and 0 black pin 
    
    if whitePins == 0 and blackPins == 0:

        while t < lenght:
            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])

            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            
            if  setivertodasascores:
                t=t
            else:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #The condition for 1 white pins and 0 black pin 
    
    if whitePins == 1 and blackPins == 0:

        while t < lenght:
            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])

            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores012 = (setiveressacor0 and setiveressacor1 and setiveressacor2)
            setiverascores123 = (setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores013 = (setiveressacor0 and setiveressacor1 and setiveressacor3)
            setiverascores023 = (setiveressacor0 and setiveressacor2 and setiveressacor3)
            setiverascores01 = (setiveressacor0 and setiveressacor1)
            setiverascores02 = (setiveressacor0 and setiveressacor2)
            setiverascores03 = (setiveressacor0 and setiveressacor3)
            setiverascores12 = (setiveressacor1 and setiveressacor2)
            setiverascores13 = (setiveressacor1 and setiveressacor3)
            setiverascores23 = (setiveressacor2 and setiveressacor3)
            seestiveremnamesmaspos = (guess[0] == combinations[t][0] or guess[1] == combinations[t][1] or guess[2] == combinations[t][2] or guess[3] == combinations[t][3])
    
            ifitsthesamething = (guess == combinations[t])

            if  ifitsthesamething or seestiveremnamesmaspos or setivertodasascores or setiverascores013 or setiverascores023 or setiverascores123 or setiverascores012 or setiverascores01 or setiverascores02 or setiverascores03 or setiverascores12 or setiverascores13 or setiverascores23:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1


    #the condition for 2 white pins and 0 Black pins

    if whitePins == 2 and blackPins == 0:

        while t < lenght:
            setiveressacor0 = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores012 = (setiveressacor0 and setiveressacor1 and setiveressacor2)
            setiverascores123 = (setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores013 = (setiveressacor0 and setiveressacor1 and setiveressacor3)
            setiverascores023 = (setiveressacor0 and setiveressacor2 and setiveressacor3)
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)

            seestiveremnamesmaspos = (guess[0] == combinations[t][0] or guess[1] == combinations[t][1] or guess[2] == combinations[t][2] or guess[3] == combinations[t][3])

            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or seestiveremnamesmaspos or setivertodasascores or setiverascores013 or setiverascores023 or setiverascores012 or setiverascores123 or ((senaotiverascores01 or senaotiverascores23) and (senaotiverascores03 or senaotiverascores12) and (senaotiverascores13 or senaotiverascores02)):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1


    #the condition for 3 white pins and 0 Black pins

    if whitePins == 3 and blackPins == 0:

        while t < lenght:
            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            senaotiverascores012 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores123 = (senaotiveressacor1 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores013 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores023 = (senaotiveressacor0 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)

            seestiveremnamesmaspos = (guess[0] == combinations[t][0] or guess[1] == combinations[t][1] or guess[2] == combinations[t][2] or guess[3] == combinations[t][3])

            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or seestiveremnamesmaspos or setivertodasascores or (senaotiverascores013 and senaotiverascores023 and senaotiverascores012 and senaotiverascores123) or (senaotiverascores01 or senaotiverascores02 or senaotiverascores03 or senaotiverascores12 or senaotiverascores13 or senaotiverascores23):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1


    #the condition for 4 white pins and 0 Black pins

    if whitePins == 4 and blackPins == 0:

        while t < lenght:

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])

            seestiveremnamesmaspos = (guess[0] == combinations[t][0] or guess[1] == combinations[t][1] or guess[2] == combinations[t][2] or guess[3] == combinations[t][3])
            
            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or seestiveremnamesmaspos or senaotiveressacor0 or senaotiveressacor1 or senaotiveressacor2 or senaotiveressacor3:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 0 white pins and 1 Black pins

    if whitePins == 0 and blackPins == 1:
    
        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])
            
            
            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])


            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores012 = (setiveressacor0 and setiveressacor1 and setiveressacor2)
            setiverascores123 = (setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores013 = (setiveressacor0 and setiveressacor1 and setiveressacor3)
            setiverascores023 = (setiveressacor0 and setiveressacor2 and setiveressacor3)
            setiverascores01 = (setiveressacor0 and setiveressacor1)
            setiverascores02 = (setiveressacor0 and setiveressacor2)
            setiverascores03 = (setiveressacor0 and setiveressacor3)
            setiverascores12 = (setiveressacor1 and setiveressacor2)
            setiverascores13 = (setiveressacor1 and setiveressacor3)
            setiverascores23 = (setiveressacor2 and setiveressacor3)
            senaoestiveremnamesmaspos = (setiveressacor0foradapos or setiveressacor1foradapos or setiveressacor2foradapos or setiveressacor3foradapos)
    
            ifitsthesamething = (guess == combinations[t])

            if  ifitsthesamething or senaoestiveremnamesmaspos or setivertodasascores or setiverascores013 or setiverascores023 or setiverascores123 or setiverascores012 or setiverascores01 or setiverascores02 or setiverascores03 or setiverascores12 or setiverascores13 or setiverascores23:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1


    #the condition for 0 white pins and 2 Black pins

    if whitePins == 0 and blackPins == 2:
    
        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])
            
            
            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])


            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores012 = (setiveressacor0 and setiveressacor1 and setiveressacor2)
            setiverascores123 = (setiveressacor1 and setiveressacor2 and setiveressacor3)
            setiverascores013 = (setiveressacor0 and setiveressacor1 and setiveressacor3)
            setiverascores023 = (setiveressacor0 and setiveressacor2 and setiveressacor3)
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)
            senaoestiveremnamesmaspos = (setiveressacor0foradapos or setiveressacor1foradapos or setiveressacor2foradapos or setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if  ifitsthesamething or senaoestiveremnamesmaspos or setivertodasascores or setiverascores013 or setiverascores023 or setiverascores012 or setiverascores123 or (senaotiverascores01 and senaotiverascores02 and senaotiverascores03 and senaotiverascores12 and senaotiverascores13 and senaotiverascores23):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 0 white pins and 3 Black pins

    if whitePins == 0 and blackPins == 3:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])
            

            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setivertodasascores = (setiveressacor0 and setiveressacor1 and setiveressacor2 and setiveressacor3)
            senaotiverascores012 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores123 = (senaotiveressacor1 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores013 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores023 = (senaotiveressacor0 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)

            senaoestiveremnamesmaspos = (setiveressacor0foradapos or setiveressacor1foradapos or setiveressacor2foradapos or setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or senaoestiveremnamesmaspos or setivertodasascores or (senaotiverascores013 and senaotiverascores023 and senaotiverascores012 and senaotiverascores123) or (senaotiverascores01 or senaotiverascores02 or senaotiverascores03 or senaotiverascores12 or senaotiverascores13 or senaotiverascores23):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 2 white pins and 2 Black pins

    if whitePins == 2 and blackPins == 2:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])
            

            setiveressacor0 = (guess[0] == combinations[t][0] or guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1 = (guess[1] == combinations[t][0] or guess[1] == combinations[t][1] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2 = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][2] or guess[2] == combinations[t][3])
            setiveressacor3 = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2] or guess[3] == combinations[t][3])

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            senaotiverascores012 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores123 = (senaotiveressacor1 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores013 = (senaotiveressacor0 and senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores023 = (senaotiveressacor0 and senaotiveressacor2 and senaotiveressacor3)
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)

            senaoestiveremnamesmaspos = (setiveressacor0foradapos or setiveressacor1foradapos or setiveressacor2foradapos or setiveressacor3foradapos)
            
            setiverascores012forapos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor2foradapos)
            setiverascores123forapos = (setiveressacor1foradapos and setiveressacor2foradapos and setiveressacor3foradapos)
            setiverascores013forapos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor3foradapos)
            setiverascores023forapos = (setiveressacor0foradapos and setiveressacor2foradapos and setiveressacor3foradapos)
            setiverascores01forapos = (setiveressacor0foradapos and setiveressacor1foradapos)
            setiverascores02forapos = (setiveressacor0foradapos and setiveressacor2foradapos)
            setiverascores03forapos = (setiveressacor0foradapos and setiveressacor3foradapos)
            setiverascores12forapos = (setiveressacor1foradapos and setiveressacor2foradapos)
            setiverascores13forapos = (setiveressacor1foradapos and setiveressacor3foradapos)
            setiverascores23forapos = (setiveressacor2foradapos and setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or senaotiveressacor0 or senaotiveressacor1 or senaotiveressacor2 or senaotiveressacor3 or (setiverascores123forapos and setiveressacor0) or (setiverascores023forapos and setiveressacor1) or (setiverascores013forapos and setiveressacor2) or (setiverascores012forapos and setiveressacor3) or (setiverascores01forapos and senaotiverascores23) or (setiverascores02forapos and senaotiverascores13) or (setiverascores03forapos and senaotiverascores12) or (setiverascores12forapos and senaotiverascores03) or (setiverascores13forapos and senaotiverascores02) or (setiverascores23forapos and senaotiverascores01):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 3 white pins and 1 Black pins

    if whitePins == 3 and blackPins == 1:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])

            setiveressacor0napos = (guess[0] == combinations[t][0] )
            setiveressacor1napos = (guess[1] == combinations[t][1] )
            setiveressacor2napos = (guess[2] == combinations[t][2] )
            setiveressacor3napos = (guess[3] == combinations[t][3] )
            

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            
            setiverascores012napos = (setiveressacor0napos or setiveressacor1napos or setiveressacor2napos)
            setiverascores123napos = (setiveressacor1napos or setiveressacor2napos or setiveressacor3napos)
            setiverascores013napos = (setiveressacor0napos or setiveressacor1napos or setiveressacor3napos)
            setiverascores023napos = (setiveressacor0napos or setiveressacor2napos or setiveressacor3napos)

            senaoestiveremnamesmaspos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor2foradapos and setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if ifitsthesamething or senaoestiveremnamesmaspos or senaotiveressacor0 or senaotiveressacor1 or senaotiveressacor2 or senaotiveressacor3 or (setiverascores123napos and guess[0] == combinations[t][0]) or (setiverascores023napos and guess[1] == combinations[t][1]) or (setiverascores013napos and guess[2] == combinations[t][2]) or (setiverascores012napos and guess[3] == combinations[t][3]):
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 1 white pins and 1 Black pins

    if whitePins == 1 and blackPins == 1:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])

            setiveressacor0napos = (guess[0] == combinations[t][0] )
            setiveressacor1napos = (guess[1] == combinations[t][1] )
            setiveressacor2napos = (guess[2] == combinations[t][2] )
            setiveressacor3napos = (guess[3] == combinations[t][3] )
            

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            senaotiverascores01 = (senaotiveressacor0 and senaotiveressacor1)
            senaotiverascores02 = (senaotiveressacor0 and senaotiveressacor2)
            senaotiverascores03 = (senaotiveressacor0 and senaotiveressacor3)
            senaotiverascores12 = (senaotiveressacor1 and senaotiveressacor2)
            senaotiverascores13 = (senaotiveressacor1 and senaotiveressacor3)
            senaotiverascores23 = (senaotiveressacor2 and senaotiveressacor3)

            senaoestiveremnamesmaspos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor2foradapos and setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if (setiveressacor0napos and setiveressacor1foradapos and senaotiverascores23) or (setiveressacor0napos and setiveressacor2foradapos and senaotiverascores13) or (setiveressacor0napos and setiveressacor3foradapos and senaotiverascores12) or (setiveressacor1napos and setiveressacor0foradapos and senaotiverascores23) or (setiveressacor1napos and setiveressacor2foradapos and senaotiverascores03) or (setiveressacor1napos and setiveressacor3foradapos and senaotiverascores02) or (setiveressacor2napos and setiveressacor0foradapos and senaotiverascores13) or (setiveressacor2napos and setiveressacor1foradapos and senaotiverascores03) or (setiveressacor2napos and setiveressacor3foradapos and senaotiverascores01) or (setiveressacor3napos and setiveressacor0foradapos and senaotiverascores12) or (setiveressacor3napos and setiveressacor1foradapos and senaotiverascores02) or (setiveressacor3napos and setiveressacor2foradapos and senaotiverascores01):
                t = t
            else:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 2 white pins and 1 Black pins

    if whitePins == 2 and blackPins == 1:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])

            setiveressacor0napos = (guess[0] == combinations[t][0] )
            setiveressacor1napos = (guess[1] == combinations[t][1] )
            setiveressacor2napos = (guess[2] == combinations[t][2] )
            setiveressacor3napos = (guess[3] == combinations[t][3] )
            

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setiverascores01forapos = (setiveressacor0foradapos and setiveressacor1foradapos)
            setiverascores02forapos = (setiveressacor0foradapos and setiveressacor2foradapos)
            setiverascores03forapos = (setiveressacor0foradapos and setiveressacor3foradapos)
            setiverascores12forapos = (setiveressacor1foradapos and setiveressacor2foradapos)
            setiverascores13forapos = (setiveressacor1foradapos and setiveressacor3foradapos)
            setiverascores23forapos = (setiveressacor2foradapos and setiveressacor3foradapos)

            senaoestiveremnamesmaspos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor2foradapos and setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if (setiveressacor0napos and setiverascores12forapos and senaotiveressacor3) or (setiveressacor0napos and setiverascores13forapos and senaotiveressacor2) or(setiveressacor0napos and setiverascores23forapos and senaotiveressacor1) or(setiveressacor1napos and setiverascores02forapos and senaotiveressacor3) or(setiveressacor1napos and setiverascores03forapos and senaotiveressacor2) or(setiveressacor1napos and setiverascores23forapos and senaotiveressacor0) or(setiveressacor2napos and setiverascores01forapos and senaotiveressacor3) or(setiveressacor2napos and setiverascores03forapos and senaotiveressacor1) or(setiveressacor2napos and setiverascores13forapos and senaotiveressacor0) or(setiveressacor3napos and setiverascores01forapos and senaotiveressacor2) or(setiveressacor3napos and setiverascores02forapos and senaotiveressacor1) or(setiveressacor3napos and setiverascores12forapos and senaotiveressacor0):
                t = t
            else:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1

    #the condition for 1 white pins and 2 Black pins

    if whitePins == 1 and blackPins == 2:

        while t < lenght:
            setiveressacor0foradapos = (guess[0] == combinations[t][1] or guess[0] == combinations[t][2] or guess[0] == combinations[t][3])
            setiveressacor1foradapos = (guess[1] == combinations[t][0] or guess[1] == combinations[t][2] or guess[1] == combinations[t][3])
            setiveressacor2foradapos = (guess[2] == combinations[t][0] or guess[2] == combinations[t][1] or guess[2] == combinations[t][3])
            setiveressacor3foradapos = (guess[3] == combinations[t][0] or guess[3] == combinations[t][1] or guess[3] == combinations[t][2])

            setiveressacor0napos = (guess[0] == combinations[t][0] )
            setiveressacor1napos = (guess[1] == combinations[t][1] )
            setiveressacor2napos = (guess[2] == combinations[t][2] )
            setiveressacor3napos = (guess[3] == combinations[t][3] )
            

            senaotiveressacor0 = (guess[0] != combinations[t][0] and guess[0] != combinations[t][1] and guess[0] != combinations[t][2] and guess[0] != combinations[t][3])
            senaotiveressacor1 = (guess[1] != combinations[t][0] and guess[1] != combinations[t][1] and guess[1] != combinations[t][2] and guess[1] != combinations[t][3])
            senaotiveressacor2 = (guess[2] != combinations[t][0] and guess[2] != combinations[t][1] and guess[2] != combinations[t][2] and guess[2] != combinations[t][3])
            senaotiveressacor3 = (guess[3] != combinations[t][0] and guess[3] != combinations[t][1] and guess[3] != combinations[t][2] and guess[3] != combinations[t][3])
            
            setiverascores01napos = (setiveressacor0napos and setiveressacor1napos)
            setiverascores02napos = (setiveressacor0napos and setiveressacor2napos)
            setiverascores03napos = (setiveressacor0napos and setiveressacor3napos)
            setiverascores12napos = (setiveressacor1napos and setiveressacor2napos)
            setiverascores13napos = (setiveressacor1napos and setiveressacor3napos)
            setiverascores23napos = (setiveressacor2napos and setiveressacor3napos)


            senaoestiveremnamesmaspos = (setiveressacor0foradapos and setiveressacor1foradapos and setiveressacor2foradapos and setiveressacor3foradapos)

            ifitsthesamething = (guess == combinations[t])

            if (setiveressacor0foradapos and setiverascores12napos and senaotiveressacor3) or (setiveressacor0foradapos and setiverascores13napos and senaotiveressacor2) or(setiveressacor0foradapos and setiverascores23napos and senaotiveressacor1) or(setiveressacor1foradapos and setiverascores02napos and senaotiveressacor3) or(setiveressacor1foradapos and setiverascores03napos and senaotiveressacor2) or(setiveressacor1foradapos and setiverascores23napos and senaotiveressacor0) or(setiveressacor2foradapos and setiverascores01napos and senaotiveressacor3) or(setiveressacor2foradapos and setiverascores03napos and senaotiveressacor1) or(setiveressacor2foradapos and setiverascores13napos and senaotiveressacor0) or(setiveressacor3foradapos and setiverascores01napos and senaotiveressacor2) or(setiveressacor3foradapos and setiverascores02napos and senaotiveressacor1) or(setiveressacor3foradapos and setiverascores12napos and senaotiveressacor0):
                t = t
            else:
                combinations.remove(combinations[t])
                t = t - 1
                lenght = lenght - 1
            t = t + 1


    #print(combinations) #print all the combinations
