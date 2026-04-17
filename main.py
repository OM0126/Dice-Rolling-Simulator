import random 


print("Welcome to Dice rolling simulator")

score = 0
no_times = 0

while True:

    user = input("press r to roll the dice and q to quit:").lower()

    if user == "r":
        dice = random.randint(1,6)
        print("u rolled a dice:", dice)

        if dice == 6:
            print("congrats you rolled and u got a 6")
            score += 1
            no_times += 1
            print("u scored", score, "points")
            print("u have rolled the dice", no_times, "times")

        else:
            print("u did not got 6, try again")
            no_times += 1
            print("u have rolled the dice", no_times, "times")
        
        if no_times % 3 == 0:
            choice = input("\nYou've played 3 rounds! Want to keep playing? (yes/no): ").lower()
            if choice != "yes":
                print("game is over final score:", score , "and u have rolled the dice", no_times, "times")
                break
    elif user == "q":
        print("thanks for playing")
        print("u scored", score, "points")
        print("u have rolled the dice", no_times, "times")
        break
    else:
        print("invalid input, try again")
        
    
    

    
