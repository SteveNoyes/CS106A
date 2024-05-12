import math
import random
def main():
    """
    "Code is there to explain the comments to the computer" 
    — Andy Harris
    The last player to take a stone loses
    keep track of stones
    keep track of players
    need to iterate through until the pile of stones is 1
    """
    # the game starts with a pile of 20 stones
    stone_pile = 20
    # between two players
    player_one = 1
    player_two = 2
    whose_turn_counter = 1
    while(stone_pile > 0):

        # set to one so that player_one goes first, can be changed
        if whose_turn_counter == 1:
            print("There are " + str(stone_pile) + " stones left.")
            player_one_turn = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            if(player_one_turn != 0 and player_one_turn > 1 or player_one_turn < 2):
                stone_pile = stone_pile - player_one_turn
                whose_turn_counter = whose_turn_counter + 1
            # else:
            #     int(input())

        elif whose_turn_counter == 2:
            print("There are " + str(stone_pile) + " stones left.")
            player_two_turn = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            if(player_two_turn != 0 and player_two_turn > 1 or player_two_turn < 2):
                stone_pile = stone_pile - player_two_turn
                whose_turn_counter = whose_turn_counter - 1

    if(stone_pile == 0):
        if(whose_turn_counter == 1):
            print("Player 1 wins!")
        elif(whose_turn_counter == 2):
            print("Player 2 wins!")

    

def auto_turn():
    turnNum = random.randint(1, 2)
    print(turnNum)

if __name__ == '__main__':
    main()