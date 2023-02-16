from IPython.display import clear_output


#creat board
def display_board(board):
    clear_output()
    print("   |   |   ")
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print("-----------")
    print("   |   |   ")
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print("   |   |   ")
    print("-----------")
    print(' '+ board[1]+' | '+board[2]+' | '+board[3])
    print("   |   |   ")



#creat function that assigns symbol to player   
def player_input():
    
    marker = ''
    #keep asking player1 to choose
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
        
    #assign player2
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1,player2)
  
 
 
#creat function for placing the marker on board
def place_marker(board, marker, position):
    
    board[position] = marker
    
    
    
#creat win conditions function
def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
    
    
#creat function that randomly decides who goes first
import random

def choose_first():
    
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
        
        
#creat function that check wheter place on baord is free        
def space_check(board, position):
    
    return board[position] == ' '    
    
    

#creat functions that checks if there are free spots on the baord
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True



#creat function that asks player for input for positon to place the marker
def player_choice(board):
    
    position = 0 
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose spot on the board (1-9): "))
    return position
    
    
    
#creat function that asks whetther player wants to rematch 
def replay():
    
    play_again = input("Play again? Enter Yes or No ")
    
    return play_again == "Yes"
    
  
  
  
  
  
#the game itself  
print('Welcome to Tic Tac Toe!')

while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input('Ready to play? Y or N?')
    
    if play_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        #Player 1 Turn
        if turn == 'Player 1':
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board, player1_marker, position)
            
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False
            else:
                if  full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = "Player 2"
        # Player2's turn.
        else:
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board, player2_marker, position)
            
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False
            else:
                if  full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = "Player 1"
       
            
            #pass

    if not replay():
        break
