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

while i < 840: #while it doesn't put all the 840 combinations in the array, it will continue adding combinations

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

print(combinations) #print all the combinations
print(len(combinations)) #print the lenght of the list
#meaning it has this quantity of combinations
