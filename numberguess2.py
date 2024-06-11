import random
def game():
    a=int(input("Enter the intial number:"))
    b=int(input("Enter the end number:"))
    c=random.randint(a,b)
    guess=int(input("Guess the number:"))
    if(guess>c):
           print("Your too high")
    elif(guess<c):
           print("Your too low!")
    elif(guess==c):
           print("Congratulations you won the game")
    else:
           print("Sorry!,try again!")
game()
while True:
 d=input("Do u want to play:")
 if(d=='yes'):
    game()
 else:
     print("Thank you for playing")
     break
    
