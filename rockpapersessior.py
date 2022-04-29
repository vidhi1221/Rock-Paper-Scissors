from random import randint

name=input("Enter your name")

game="Rock-Paper-Sessior"
print(game)
start="Game Begin"
print(start)

computer_win=0
user_win=0
while True:
    choice=int(input("1 For Rock: : 2 For Paper: : 3 For Scissiors: : 4 For Exit"))
    computer=[1,2,3]
    computer_choice=computer[randint(0,2)]
    if choice==computer_choice:
        print("Its tie!....\n")
        print("user score",user_win)
        print("computer score",computer_win)
        print("____________________________XXX______________________________")
    elif choice==1:
        if computer_choice==3:
            print("Scissors Break!..... You Win\n")
            user_win=user_win+1
        else:
            print("Paper covers Rock!....You Lose\n")
            computer_win=computer_win+1
        print("user score",user_win)
        print("computer score",computer_win)
        print("____________________________XXX______________________________")
    elif choice==2:
        if computer_choice==1:
            print("____________________________XXX______________________________")
            print("Paper covers Rock!....You Win\n")
            user_win=user_win+1
        else:
            print("Scissors cuts Paper!.....You Lose\n")
            computer_win=computer_win+1
        print("user score",user_win)
        print("computer score",computer_win)
        print("____________________________XXX______________________________")
    elif choice==3:
        if computer_choice==1:
            print("Scissors Break!..... You Win\n")
            user_win=user_win+1
        else:
            print("Paper covers Rock!....You Lose\n")
            computer_win=computer_win+1
        print("user score",user_win)
        print("computer score",computer_win)
        print("____________________________XXX______________________________")
    elif choice==4:
            print("===============================================")
            print("-------------------------Thank you For playing----------------------------")
            print("===============================================")
            break
    else:
        print("Invalid choice")
print("user score",user_win)
print("computer score",computer_win)
if user_win>computer_win:
    print(f'User Win  {name} =',user_win)
elif user_win==computer_win:
    print("Game is tie")
else :
    print("Computer Win=",computer_win)
    
            
    

    
