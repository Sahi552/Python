#rock paper scissor

import random 

print("Welcome to rock paper scissor game")
print("Are you ready to play the game?")
yn = input("enter y / n :")         #getting choice from user

def ans(player):        #assiging rps to players
    
    l = ["ROCK","PAPPER","SCISSOR"]
    
    game = random.randint(1,3)

    if(game == 1):
        ans = l[game-1]
        print(player + " is " + ans)
            
    elif(game == 2):
        ans = l[game-1]
        print(player + " is " + ans)
            
    else:
        ans = l[2]
        print(player + " is " + ans)
        
    s = []
    s.append(ans)
    return ans      #getting ans


def game(player_1,player_2):    #game function
    
    pl1 = input(player_1 + " press any keys...")
    while True:
        p1 = ans(player_1)
        break
    pl2 = input(player_2 + " press any keys...")
    while True:
        p2 = ans(player_2)
        break
    
    #logic
    
    if(p1 == p2):
        print("Match draw ")
        
    elif(p1 == 'PAPPER' and p2 == 'SCISSOR' ):
        print("Scissor can cut paper" + player_2 + "wins")
        
    elif(p1 == 'SCISSOR' and p2 == 'PAPPER'):
        print("Scissor can cut paper" + player_1 + "wins")

    elif(p1 == 'PAPPER' and p2 == 'ROCK'):
        print("papper can cover rock" + player_1 + "wins")
        
    elif(p1 == 'ROCK' and p2 == 'PAPPER'):
        print("papper can cover rock" + player_2 + "wins")

    elif(p1 == 'SCISSOR' and p2 == 'ROCK'):
        print("rock can break scissor" + player_2 + "wins")
        
    elif(p1 == 'ROCK' and p2 == 'SCISSOR'):
        print("rock can break scissor \n" + player_1 + " wins")
        
    inp = input("Retry!..y/n ")
    if(inp == "y"):
        game(player_1,player_2)
    else:
        print("The End")

def player():   #players details function
    
    player_1 = input("Enter player1 name : ")   #player1 name
    player_2 = input("Enter player2 name : ")   #player2 name

    
    
    while(player_1 and player_2):    #after getting player names
        
        if(player_1 == player_2):
            print("This is Two player game \n You need an opponent")
            break
            
        else:
            print("Hello {} and {} \nPlease enjoy the game".format(player_1 , player_2))
            game(player_1,player_2)  #choice
            break
        
    else:
        print("This is Two player game \n Please Enter Both of Your name")
    
    
    
if(yn == 'y'):  #conditions
    player()
else:
    print("Come back when you are ready!")
