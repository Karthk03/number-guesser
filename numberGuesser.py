guess  = int(input("guess a number between 1 and 10: "))

while(guess!=7):
    if(guess> 7):
        print("too high")
    if(guess<7):
        print("too low")

    guess  = int(input("try again: "))

print("you got it!")