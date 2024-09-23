import random


list = [0,1,2,3,4,5,6]
Colors = "YRBGOPK"
First = random.choice(list)
list.remove(First)
Second = random.choice(list)
list.remove(Second)
Third = random.choice(list)
list.remove(Third)
Fourth  = random.choice(list)

Password = Colors[First] + Colors[Second] + Colors[Third] + Colors[Fourth]



i = 1


print("Catalog")
print("Y - Yellow")
print("R - Red")
print("B - Blue")
print("G - Green")
print("O - Orange")
print("P - Purple")
print("K - Pink")


while i < 11 :
    print(i,"try")
    print('what is your try? _ _ _ _')
    tentativa = str(input()) 
    i = i + 1
    t = 0
    whitePins = 0
    blackPins = 0
    while t < 4:
        list2= [0,1,2,3]
        list2.remove(t)

        if tentativa[t] == Password[t]:
            blackPins = blackPins + 1
        elif tentativa[t] in Password:
            whitePins = whitePins + 1
            
        
        t = t + 1
    if blackPins == 4:
        print("You got it!")
        i = 11
    else:
        print(whitePins,"White pins", "(showing that you got the exact color but it's in a different position for",whitePins,"pins)")
        print(blackPins,"Black pins", "(showing that you got the exact color and position for",blackPins,"pins)")
    
