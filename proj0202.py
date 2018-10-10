#CSE 231 Project #2

#while true game will play, false will end game
#while true player's turn, false will run computer's turn
#will input which pile to take from and how many stones to take
#check for game over
#change player's turn to false
#computer will take 1 stone from pile opposite of player's choice
#check for gameover
#change player's turn to true

#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")
while int(play_str) != 0:
    #variables
    pile_1, pile_2 = 5, 5 #starting number of stones
    players_turn = True #use to switch from players turn to computers turn
    game_over = False
    print("Start --> Pile 1:", pile_1, "   Pile 2:", pile_2)
    while not game_over:
        
        #Player's turn
        if players_turn == True:
            #input pile to take from
            choose_pile = int(input("Choose a pile (1 or 2): ")) 
            #error message with constraints
            if choose_pile not in [1,2]:
                print("Pile must be 1 or 2 and non-empty. Please try again.")
                continue
            #error message with other constraints
            if choose_pile == 1:
                if pile_1 == 0:
                    print("Pile must be 1 or 2 and non-empty. Please try again.")
                    continue
                
                #input pile number was correct, now input stones to remove
                else:
                    #input number of stones to remove
                    player_remove = int(input("Choose stones to remove from pile: ")) 
                    #number of stones allowed to take
                    if player_remove in range(1,4) and player_remove <= pile_1:
                        #remove number of stones from pile 1
                        pile_1 = pile_1 - player_remove
                        print("Player -> Remove", player_remove, "stones from pile 1")
                        print("Pile 1:", pile_1, "   Pile 2:", pile_2)
                    
                    #error if player removes less than 1 or more than 3 stones
                    else:
                        print("Invalid number of stones. Please try again.")
                        continue
           
            #player chooses pile 2    
            if choose_pile == 2:
                #input number of stones to remove
                player_remove = int(input("Choose stones to remove from pile: "))
                #number of stones allowed to take
                if player_remove in range(1,4) and player_remove <= pile_2:
                    #remove number of stones from pile 2
                    pile_2 = pile_2 - player_remove
                    print("Player -> Remove", player_remove, "stones from pile 2")
                    print("Pile 1:", pile_1, "   Pile 2:", pile_2)
                
                #error if player removes less than 1 or more than 3 stones
                else:
                    print("Invalid number of stones. Please try again.")
                    continue
            
            #condition of winning    
            if pile_1 == 0 and pile_2 == 0:
                print("\nPlayer wins!")
            
            #switch turns
            players_turn = False
            #changes values to allow computer to take from opposite pile than what player chose
            tmp = [1,2]
            tmp.remove(choose_pile)
         
        #computer's turn    
        elif players_turn == False:
            print("Computer -> Remove 1 stones from pile", tmp[0])
            
            #computer chooses pile 2 if player chooses 1
            if choose_pile == 1 and pile_2 != 0:
                #computer removes 1 stone
                pile_2 -= 1 
            #computer chooses pile 1 is player chooses 2
            elif choose_pile == 2 and pile_1 != 0:
                #computer removes 1 stone
                pile_1 -= 1
            
            #if the pile the player did not choose is empty, computer takes from the same pile the player took from
            elif choose_pile == 1 and pile_2 == 0 and pile_1 != 0:
                #computer removes 1 stone
                pile_1 -= 1
            elif choose_pile == 2 and pile_1 == 0 and pile_2 != 0:
                #computer removes 1 stone
                pile_2 -= 1
            
            #print score
            print("Pile 1:", pile_1, "   Pile 2:", pile_2)
            
            #condition of winning
            if pile_1 == 0 and pile_2 == 0:
                print("\nComputer wins!")
             
            #if game did not end, loops back to player  
            players_turn = True
        
        #ends game
        if pile_1 == 0 and pile_2 == 0:
            game_over = True

    print("Score -> human: 0 ; computer:",play_str)
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")

