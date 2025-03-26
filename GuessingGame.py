import random


print('WELCOME TO THE GUESSING GAME')
print('ENTER 1 , 2 or 3 TO CHOOSE ')
IsRunning=True

def level(y,n):
    #y=No. of tries
    #n= biggest no.
    x=random.randrange(1,n)
    for i in range(y):
        ans=int(input(f"GUESS BETWEEN 1 TO {n-1}:"))
        if ans == x:
            print('you win!')
            break
        elif i==2:
            print (f"THE ANSWER IS {x}!")
            print ('better luck next time')
        else:
            print(f"chances left:{y-(i+1)}")
            if ans>x:
                print ('THE ANSWER IS BIGGER THAN THE NO.')
            elif ans<x:
                print('THE ANSWER IS SMALLER THAN THE NO.')
            print ("try again")

            
while IsRunning==True:
    levelchoice=int(input("CHOOSE A LEVEL:"))
    if levelchoice ==1:
        level(3,11)
        
    elif levelchoice == 2:
        level(5,21)

    elif levelchoice == 3:
        level(7,51)
        
    else:
        print('INVALID INPUT')
    cont=input("Do you want to continue playing(y/n):").lower()
    if cont=='y':
        Isrunning=True
    else:
        Isrunning=False
        break



        
