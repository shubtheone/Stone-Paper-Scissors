import random 


timeswin=0
timeslose=0
while True:

    user=input("Enter Your Choice -> Stone or Paper or Scissors: ").lower()
    Chdict={"stone":1,"scissors":-1,"paper":0}
    userChoice=Chdict[user]

    computerCh=random.choice([-1,0,1])
    reversedict={1:"stone",-1:"scissors",0:"paper"}

    print(f"You have chosen {reversedict[userChoice]} and computer has chosen {reversedict[computerCh]} \n")


    if(userChoice==computerCh):
        print("It's a Draw!")

    else:
        if(userChoice==1 and computerCh==-1):
            print("You Win!")
            timeswin+=1
        elif(userChoice==1 and computerCh==0):
            print("Computer Wins! Better Luck Next Time")
            timeslose+=1
        elif(userChoice==-1 and computerCh==0):
            print("You Win!")
            timeswin+=1
        elif(userChoice==-1 and computerCh==1):
            print("Computer Wins! Better Luck Next Time")
            timeslose+=1
        elif(userChoice==0 and computerCh==1):
            print("You Win!")
            timeswin+=1
        elif(userChoice==0 and computerCh==-1):
            print("Computer Wins! Better Luck Next Time")
            timeslose+=1
    
    play_again=input("Would you like to play again? YES OR NO").lower()
    if(play_again!="yes"):
        break




f=open("gamefile.txt","w")
f.write(f"You have lost {timeslose} times and won {timeswin} times")
f.close()