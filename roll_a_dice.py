import random

def dice (ask):
    while ask=="y":
            no=random.randint(1,6)
            print(no)
            break
    
    if(no==1):
        print("_ _ _")
        print("_ 0 _")
        print("_ _ _")

    elif(no==2):
        print("0 _ _")
        print("_ _ _")
        print("_ _ 0")
        
    elif(no==3):
        print("0 _ _")
        print("_ 0 _")
        print("_ _ 0")

    elif(no==4):
        print("0 _ 0")
        print("_ _ _")
        print("0 _ 0")

    elif(no==5):
        print("0 _ 0")
        print("_ 0 _")
        print("0 _ 0")

    elif(no==6):
        print("0 _ 0")
        print("0 _ 0")
        print("0 _ 0")
    

    again(ask)

def again(go):
    ask=input("do you want to roll a dice again?input 'y' for yes and 'n' for no.")  
    dice(ask)

go=input("do you want to roll a dice or not? input 'y' for yes and 'n' for no.")
dice(go)
