from IPython.display import clear_output

def display_board(board):
    x=1
    for i in range(1,6):
           print('')
           for k in range(0,11):
                    if i%2==0:
                        print('-',end='')
                    else :
                        if k in [0,2,4,6,8,10]:
                            print('-',end='')
                        elif k in [3,7]:
                            print('|',end='')
                        elif k in [1,5,9]:
                            print(board[x],end='')
                            x=x+1
                     
        
    
   def player_input():
    x=True
    while x :
        player=input("Please input a marker 'X' or '0' :")
        
        if player !='X' and player !='0' :
            print('Wrong Input ,Enter again:')
        else :
            x=False
        
    if player=='0':
        p='X'
    else :
        p='0'
    return (player,p)
    pass
    def place_marker(board, marker, position):
    position=int(position)
    board[position]=marker
    
    pass
    def win_check(board, mark):
    for i in range(1,6):
        list=[mark,mark,mark]
        if board[1:4]==list or board[4:7]==list or board[7:] ==list or [board[1],board[4],board[7]]==list or [board[2],board[5],board[8]]==list or [board[3],board[6],board[9]]==list or [board[1],board[5],board[9]]==list or [board[3],board[5],board[7]]==list:
            return True
        
        
        
    
    pass
    import random

def choose_first():
    x= random.randint(0,100)
    x=int(x)
    if x%2==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
    pass
    def space_check(board, position):
    position=int(position)
    if board[position] == '0'or board[position] == 'X':
        return False
    else :
        return True
    
    pass

def full_board_check(board):
    c=0
    for position in range(1,10):
        
        if board[position] == '0' or board[position] == 'X':
            c=c+1
    if c==9 :
        return True
    else:
        return False
    
  
        
    
    pass
    def player_choice(board):
    
    x=input('Enter next move:')
    x=int(x)
    y=space_check(board,x)
    if y== True:
        return x
    
    pass
    def replay():
    x=input("Want to play again??? \n Press 1 if Yes:")
    if x=='1':
        return True
    return False
    pass
    print('Welcome to Tic Tac Toe!')

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break
        

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('\n Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
            