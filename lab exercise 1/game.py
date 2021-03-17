#game finding a number within 3 attempts using while loop
secret_number=15
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Enter the number"))
    guess_count +=1
    if guess==secret_number:
        print("you Won")
        break
    else:
        print("Try again")
else:
    print("you cannot guess more sorry")
