#-----------------------------
#      Tic-Tac-Toe Game
#    Author: Dallas Eaton
#-----------------------------

def main():
    # Set inital game-state
    game_over = False
    player = 'X'
    board = make_board()
    timer = 0

    # Game loop 
    while (game_over == False):
        timer += 1
        
        if (timer >= 10):
            # All spaces will have been filled, so game loop will end
            break

        player = change_player(player)
        
        draw_board(board)
        
        prompt_move(player, board)
        
        game_over = check_win(board, player)

    # Draw final board
    draw_board(board)
    # Determine the right message based on timer
    if (timer < 10):
        print(f"Congratulations player: {player}. You win!")
    else:
        print("Game over. It's a draw!")
        

def make_board():
    board = []
    for num in range(9):
        board.append(" ")
    return board

def change_player(player):
        if (player == "X"):
            return "O"
        else:
            return "X"

def check_win(board, player):
    # player symbol has to match one of the combinations to trigger True
    return (player == board[0] == board[1] == board[2] or
            player == board[3] == board[4] == board[5] or
            player == board[6] == board[7] == board[8] or
            player == board[0] == board[3] == board[6] or
            player == board[1] == board[4] == board[7] or
            player == board[2] == board[5] == board[8] or
            player == board[0] == board[4] == board[8] or
            player == board[2] == board[4] == board[6])

def draw_board(board):
    print(" +-----+")
    print(f" |{board[0]}|{board[1]}|{board[2]}|")
    print(" |-+-+-|")
    print(f" |{board[3]}|{board[4]}|{board[5]}|")
    print(" |-+-+-|")
    print(f" |{board[6]}|{board[7]}|{board[8]}|")
    print(" +-----+")

def prompt_move(player, board):
    spot = int(input(f"Player: {player}, please make a move (enter 1-9. Grid starting top-left, ending bottom-right): "))
    # Make sure space is not already taken
    while (board[spot - 1] != " "):
        # if it is, prompt again (until empty space is chosen)
        spot = int(input(f"{player}, try again: "))    
    board[spot-1] = player


if __name__ == "__main__":
    main()