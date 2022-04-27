#-----------------------------
#      Tic-Tac-Toe Game
#    Author: Dallas Eaton
#-----------------------------

def main():
    game_over = False
    player = 'x'
    board = make_board()
    while (game_over == False):
        draw_board(board)
        prompt_move(player, board)
        if (player == "x"):
            player = "o"
        else:
            player = "x"

def make_board():
    board = []
    for spot in range(9):
        board.append(" ")
    return board

def draw_board(board):
    print("  a b c")
    print(" +-----+")
    print(f"1|{board[0]}|{board[1]}|{board[2]}|")
    print(" |-+-+-|")
    print(f"2|{board[3]}|{board[4]}|{board[5]}|")
    print(" |-+-+-|")
    print(f"3|{board[6]}|{board[7]}|{board[8]}|")
    print(" +-----+")

def prompt_move(player, board):
    spot = int(input(f"{player}, please make a move (1-9, starting top-left): "))
    while (board[spot - 1] != " "):
        spot = int(input(f"{player}, try again: "))    
    board[spot-1] = player


if __name__ == "__main__":
    main()