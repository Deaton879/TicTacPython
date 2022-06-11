from classes.board import Board

#-----------------------------
#      Tic-Tac-Toe Game
#    Author: Dallas Eaton
#-----------------------------

def main():
    # Set inital game-state
    game_over = False
    player = 'X'
    board = Board()
    board.make_board()
    timer = 0

    # Game loop 
    while (game_over == False):
        timer += 1
        
        if (timer >= 10):
            # All spaces will have been filled, so game loop will end
            break

        player = change_player(player)
        
        board.draw_board()
        
        prompt_move(player, board)
        
        game_over = board.check_win(player)

    # Draw final board
    board.draw_board()
    # Determine the right message based on timer
    if (timer < 10):
        print(f"Congratulations player: {player}. You win!")
    else:
        print("Game over. It's a draw!")
        
def change_player(player):
        if (player == "X"):
            return "O"
        else:
            return "X"

def prompt_move(player, board):
    spot = int(input(f"Player: {player}, please make a move (enter 1-9. Grid starting top-left, ending bottom-right): "))
    # Make sure space is not already taken
    while (board.get_spot(spot - 1) != " "):
        # if it is, prompt again (until empty space is chosen)
        spot = int(input(f"{player}, try again: "))    
    board.set_spot(spot - 1, player)


if __name__ == "__main__":
    main()