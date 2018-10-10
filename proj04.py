''' Project 4 play the game of "Craps"
    player is promted for inputs to play the game 
    which is computed within the functions'''


from cse231_random import randint  # the cse231 test random for Mimir testing

def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance():
    '''Prompt player for initial bank balance 
    (from which wagering will be added or subtracted) 
    the player-entered bank balance is returned as an int'''
    balance = input("Enter an initial bank balance (dollars):")
    return int(balance)

def add_to_bank_balance(balance):
    '''Prompts the player for an amount to add to the balance. 
    The balance is returned as an int.'''
    add_balance = int(input())
    return int(balance + add_balance)

def get_wager_amount():
    '''prompts the player for a wager on a particular roll
    the wager is returned as an int'''
    wager = input(" Enter a wager (dollars):")
    return int(wager) 
    
def is_valid_wager_amount(wager, balance):
    '''checks that the wager is less than or equal to the balance; 
    returns True if it is; False otherwise'''
    while balance != 0:
        if wager <= balance:
            return True
        else:
            return False 

def roll_die():
    '''rolls random number 1-6 and assigns numbers to dice'''
    die2_value = randint(1,6)
    return die2_value

def calculate_sum_dice(die1_value, die2_value):
    '''sums the values of thr two die and returns the sum as an int'''
    sum_dice = int(die1_value) + int(die2_value)
    return int(sum_dice)

def first_roll_result(sum_dice):
    '''Function determines the result on the first roll of the pair of dice.
    a string is returned. 
    you are required to use at least one boolean operator 
    "or" or "and" in this function.
    1 if the sum is 7 or 11 on the roll, 
    the player wins and "win" is returned.
    2 if the sum is 2, 3, or 12 on the first throw (called "craps"), 
    the player loses
    (i.e. the "house" wins) and "loss" is returned.
    3 if the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
    then the sum becomes the player's point and "point" is returned'''
    if sum_dice == 7 or sum_dice == 11:
            return "win"
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
            return "loss"
    else:
            point_value = 0
            point_value = sum_dice + point_value
            return "point"
   
def subsequent_roll_result(sum_dice, point_value):
    '''Determines the result on the subsequent rolls of the pair of dice.
    a string is returned.
    1 if sum_dice is the point_value, then "point" is returned
    2 if sum_dice is 7 then "loss" is returned
    3 otherwise, "neither" is returned'''
    if sum_dice == 7:
        return "loss"
    elif sum_dice == point_value:
        return "point"
    else:
        return "neither"

def main():    
    '''takes no input
    returns nothing
    call the functions from here
    that, the game is played in this fucntion'''
    
    game_over = False
    display_game_rules()
    balance = get_bank_balance()
    while game_over != True:
            wager = get_wager_amount()
        #if is_valid_wager_amount(wager, balance) == False:
        #    print("Error: wager > balance. Try again.")
        #    continue
        #else:
            roll1 = roll_die()
            roll2 = roll_die()
            print(" Die 1:", roll1)
            print("Die 2:", roll2)
            sum_dice = calculate_sum_dice(roll1, roll2)
            print("Dice sum:", sum_dice)
            if first_roll_result(sum_dice) == "win":
                print("Natural winner.")
                print("You WIN!")
                balance = balance + wager
                print("Balance:", (balance))
                play = input("Do you want to continue? ")
                if play == "yes":
                    willadd = (input("Do you want to add to your balance?"))
                    if willadd == "yes":
                        balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:1"))
                        print("Balance", balance)
                        wager = get_wager_amount() ### is wager in the right place?
                    else: 
                        continue
                else:
                    print("Game is over.")
                    game_over = True
                    break
            if first_roll_result(sum_dice) == "loss":
                print("Craps.")
                print("You lose.")
                balance = balance - wager
                print("Balance:", (balance))# - wager)) ####problem area for balance

                play = input("Do you want to continue? ")         
                if play == "yes":
                    #balance = balance - wager
                    willadd = (input("Do you want to add to your balance?"))
                    if willadd == "yes":
                        balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:2"))
                        print("Balance", balance)
                        wager = get_wager_amount()
                    else: 
                        continue
                else:
                    print("Game is over.")
                    game_over = True
                    break
            if first_roll_result(sum_dice) == "point":
                print("*** Point:", sum_dice)
                point_value = sum_dice
                roll1 = roll_die()
                roll2 = roll_die()
                print("Die 1:", roll1)
                print("Die 2:", roll2)
                sum_dice = calculate_sum_dice(roll1, roll2)
                print("Dice sum:", sum_dice)#########last output before death
                if subsequent_roll_result(sum_dice, point_value) == "loss":
                    print("You lose.")
                    balance = balance - wager
                    print("Balance:", (balance))
                    play = input("Do you want to continue? ")         
                    if play == "yes":
                        #balance = balance - wager
                        willadd = (input("Do you want to add to your balance?"))
                        if willadd == "yes":
                            balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:3"))
                            print("Balance", balance)
                            wager = get_wager_amount() ### is wager in the right place?
                    else:
                        print("Game is over.")
                        game_over = True
                        break
                if subsequent_roll_result(sum_dice, point_value) == "point":
                    print("You matched your Point.")
                    print("You WIN!")
                    balance = balance + wager
                    print("Balance:", (balance))
                    play = input("Do you want to continue? ")         
                    if play == "yes":
                        #####balance = balance - wager ##### not sure if this is subtracting from the correct balance
                        willadd = (input("Do you want to add to your balance?"))
                        if willadd == "yes":
                            balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:4"))
                            print("Balance", balance)
                            wager = get_wager_amount() ### is wager in the right place?
                            continue
                    else:
                        print("Game is over.")
                        game_over = True
                        break
                while subsequent_roll_result(sum_dice, point_value) == "neither":
                    #continue
                    roll1 = roll_die()
                    roll2 = roll_die()
                    print("Die 1:", roll1)
                    print("Die 2:", roll2)
                    sum_dice = calculate_sum_dice(roll1, roll2)
                    print("Dice sum:", sum_dice)
                    if subsequent_roll_result(sum_dice, point_value) == "loss":
                        print("You lose.")
                        balance = balance - wager
                        print("Balance:", (balance))
                        play = input("Do you want to continue? ")         
                        if play == "yes":
                            #balance = balance - wager
                            willadd = (input("Do you want to add to your balance?"))
                            if willadd == "yes":
                                balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:"))
                                print("Balance", balance)
                                wager = get_wager_amount() ### is wager in the right place?
                        else:
                            print("Game is over.")
                            game_over = True
                            break
                    if subsequent_roll_result(sum_dice, point_value) == "point":
                        print("You matched your Point.")
                        print("You WIN!")
                        #print("Balance:", balance)
                        #print("wager", wager)
                        balance = balance + wager
                        print("Balance:", (balance)) ######problem area

                        play = input("Do you want to continue? ")         
                        if play == "yes":
                            #balance = balance + wager ##### not sure if this is subtracting from the correct balance
                            willadd = (input("Do you want to add to your balance?"))
                            if willadd == "yes":
                                balance = add_to_bank_balance(input("Enter how many dollars to add to your balance:"))
                                print("Balance", balance)
                                wager = get_wager_amount() ### is wager in the right place?
                        else:
                            print("Game is over.")
                            game_over = True
                    continue
            #break         





if __name__ == "__main__":
    main()