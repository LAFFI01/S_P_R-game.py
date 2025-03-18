import random
   
name = input("Enter the name: ").capitalize()
round = 1
win = 0
print(f"Welcome to the Game {name}")
print("PLease follow the instruction:\nScissor:1\nPaper:2\nRock:3\n")
while round<4:
    try:
        player = int(input("Enter the number: "))
    except ValueError:
        print("Value Error")
        continue
    
    computer = random.randint(1,3)
    
    if player<0 or player>3:
        print("Follow the rule")
        continue
    
    if player == 1 and computer ==3:
        print(f"{name} loss the round {round} ")
        round +=1
        
    elif player == 3 and computer == 1:
        print(f"{name} win the round {round} ")
        round +=1
        win +=1
        
    elif player == 2 and computer == 1:
        print(f"{name} loss the round {round} ")
        round +=1
        
    elif player == 1 and computer == 2:
        print(f"{name} win the round {round} ")
        round +=1
        win +=1
        
    elif player == 3 and computer == 2:
        print(f"{name} loss the round {round} ")
        round +=1

        
    elif player == 2 and computer == 3:
        print(f"{name} win the round {round} ")
        round +=1
        win +=1
    
    elif player == computer:
        print(f"Draw {round} ")
        continue

if win>1:
    print(f"{name} win")
else:
    print(f"{name} lose")
    
with open('SPRgamelogs.txt','a')as f:
    if win>1:
        f.write(f"{name} win the game \n")
    else:
        f.write(f"{name} loss the game\n")