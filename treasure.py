print("WELCOME TO TREASURE ISLAND ^__^")
initial=input("Choose the direction: left or right..\n")
if(initial == "left"):
    print("GO TO THE NEXT STEP...")
else:
    print("GAME OVER")
second_level=input("How to go the next level? swim or boat\n")
if(second_level == "swim"):
    print("Go to the next level....\n")
else:
    print("GAME OVER")
third_level=input("Which color door ? red blue yellow...\n")
if(third_level == "blue" or third_level == "red"):
    print("Game Over")
else:
    print("You Win")
