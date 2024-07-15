import random
choice = random.randint(1, 100)
print(choice)
print("ehy Lets begin the game.........")
turn=0
lastdiff=0

while(turn<=5):
    num=int(input("entere a number"))
    if(num>100 or num<0):
        print("Out of bound") 
        num=int(input("entere a number"))
    turn+=1
    if(choice==num):
        print(f"hey you have found the number in {turn} th turn ")
        break

    diff=abs(choice-num)
    if(turn==1):
        if(diff<=10):
            print("warm")  
        else:
            print("Cold")
        lasDif=diff
    elif(turn>1):
        if(lasDif>diff):
            print("warmer")
        else:
            print("colder")
    if(turn==5):
        print("do you want to continue?")
        ch=int(input("enter 0 for quit 1 for continnue"))
        if(ch==1):
            turn=0
        else:
            print("thank you")
            break
    
        
