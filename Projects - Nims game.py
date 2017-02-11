# Name: Valerie Lim
# Date: 22/1/2017 Sunday
# Date completed: 23/1/2017 Monday
# Title: Nims Game.py

'''
An interactive two-person game; also known as Stones.
@param pile: the number of stones in the pile to start
@param max_stones: the maximum number of stones you can take on one turn
'''
    
def play_nims(pile, max_stones):
    int(pile)
    int(max_stones)

    while pile > 0:

        ### Player 1 
        player1 = input("Player 1, how many stones would you like to remove?")
        while player1 > max_stones or player1 <= 0 or player1 > pile :
            print "That number is not valid. Please draw between 1 and", \
                   max_stones, "stones, or the remaining amount left. :)"
            player1 = input("Let's try again. Player 1, how many stones would you like to remove?")
        else:
            pile = pile - player1
            print "Remaining stones in pile is", pile

        ### Catch for if pile = 0 without having to loop through player 2 
        if pile == 0:
            break

        ### Player 2
        player2 = input("Player 2, how many stones would you like to remove?")
        while player2 > max_stones or player2 <= 0 or player2 > pile :
            print "That number is not valid. Please draw between 1 and", \
                   max_stones, "stones, or the remaining amount left. :)"
            player2 = input("Let's try again. Player 2, how many stones would you like to remove?")
        else:
            pile = pile - player2
            print "Remaining stones in pile is", pile

    print "Game over." 

     
