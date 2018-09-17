#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")
while int(play_str) != 0:
    pile_1, pile_2 = 5, 5 #starting number of stones
    players_turn = True #use to switch from players turn to computers turn
    game_over = False
    print("Start --> Pile 1:", pile_1, "   Pile 2:", pile_2)
    while not game_over:
        if players_turn == True: #do i use elif
            #print("Pile 1:", pile_1, "   Pile 2:", pile_2) #int(pile_1) >= 0 and int(pile_2) >= 0: #condition to keep game playing, maybe unnecessay considering other while statement
            choose_pile = int(input("Choose a pile (1 or 2): ")) 
            if choose_pile not in [1,2]:
                print("Pile must be 1 or 2 and non-empty. Please try again.")
                continue
            if choose_pile == 1: 
                player_remove = int(input("Choose stones to remove from pile: ")) #input number of stones to remove
                if player_remove in range(1,4) and player_remove <= pile_1: #and pile_1 != 0:(unnecessary because statement just to left) #player_remove in range(1,3) and
                    #if pile_1 != 0:
                    pile_1 = pile_1 - player_remove #remove number of stones from pile 1
                    print("Player -> Remove", player_remove, "stones from pile 1")
                    print("Pile 1:", pile_1, "   Pile 2:", pile_2)
                else: #if player_remove <= 0 and player_remove >=4:
                    print("Invalid number of stones. Please try again.")
                    continue
            if choose_pile == 2: #if player chooses pile 2 pile_1 == 0 and pile_2 == 0:
                player_remove = int(input("Choose stones to remove from pile: ")) #input number of stones to remove
                if player_remove in range(1,4) and player_remove <= pile_2:
                    #if pile_2 != 0:
                    pile_2 = pile_2 - player_remove
                    print("Player -> Remove", player_remove, "stones from pile 2")
                    print("Pile 1:", pile_1, "   Pile 2:", pile_2)
                else: #if player_remove <= 0 and player_remove >=4:
                    print("Invalid number of stones. Please try again.")
                    continue
            if pile_1 == 0 and pile_2 == 0:
                print("\nPlayer wins!")
            #didnt need an else #switch turns
            players_turn = False
        elif players_turn == False: #computer's turn ##do i use elif
            print("Computer -> Remove 1 stones from pile ", not choose_pile)
            print("Pile 1:", pile_1, "   Pile 2:", pile_2)
            if choose_pile == 1 and pile_2 != 0: #choose_pile == and 2 #computer chooses pile 2 if player chooses 1
                #if pile_2 != 0:
                pile_2 -= 1 #computer removes 1 stone
                #print("Pile 1: ", pile_1, "Pile 2:", pile_2)
            elif choose_pile == 2 and pile_1 != 0: #choose_pile == 1 and #and pile_1 == 0: #else: #if pile 2 is 0
                pile_1 -= 1 #computer removes 1 stone
                #print("Pile 1:", pile_1)
                #print("Pile 2: ", pile_2)
            elif choose_pile == 1 and pile_2 == 0 and pile_1 !=0:
                pile_1 -= 1 #computer removes 1 stone
            elif choose_pile == 2 and pile_1 == 0 and pile_2 !=0:
                pile_2 -= 1 #computer removes 1 stone
            if pile_1 == 0 and pile_2 == 0:
                print("Pile 1:", pile_1, "   Pile 2:", pile_2)
                print("\nComputer wins!") 
            players_turn = True
        if pile_1 == 0 and pile_2 == 0:
            game_over = True
        #else: #switch turns
    print("Score -> human: 0 ; computer:",play_str)# leave this as is (provided code) maybe delete later
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")

