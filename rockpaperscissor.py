from random import *
user=input("choose an option \n 1.Rock \n2.Paper \n3.Scissor\nyour option : ")
computer=randint(1,3)
if user=="1" and computer ==2:
    print("YOU LOST!\nyou chose rock , computer chose paper.")
elif user=="1" and computer ==3:
    print("YOU WON!\n you chose rock , computer chose scissor.")
elif user=="1" and computer==1:
    print("IT'S A DRAW\n you chose rock , computer chose rock.")
elif user=="2" and computer ==1:
    print("YOU WON!\n you chose paper , computer chose rock.")
elif user=="2" and computer ==2:
    print("IT'S A DRAW\n you chose paper , computer chose paper.")
elif user=="2" and computer ==3:
    print("YOU LOST! \n you chose paper , computer chose scissor.")
elif user=="3" and computer ==1:
    print("YOU LOST!\n you chose scissor , the computer chose rock.")
elif user=="3" and computer==2:
    print("YOU WON! \n you chose scissor , the computer chose paper.")
elif user=="3" and computer==3:
    print("IT'S A DRAW!\n you chose scissor , the computer chose scissor.")
else :
    print("you entered the wrong option")

  
