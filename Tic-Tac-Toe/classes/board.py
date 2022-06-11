class Board:

    def __init__(self):

        self.board = []


    def make_board(self):
        for num in range(9):
            self.board.append(" ")

    def draw_board(self):
        print(" +-----+")
        print(f" |{self.board[0]}|{self.board[1]}|{self.board[2]}|")
        print(" |-+-+-|")
        print(f" |{self.board[3]}|{self.board[4]}|{self.board[5]}|")
        print(" |-+-+-|")
        print(f" |{self.board[6]}|{self.board[7]}|{self.board[8]}|")
        print(" +-----+")

    def check_win(self, player):
    # player symbol has to match one of the combinations to trigger True
        if (player == self.board[0] == self.board[1] == self.board[2] or
            player == self.board[3] == self.board[4] == self.board[5] or
            player == self.board[6] == self.board[7] == self.board[8] or
            player == self.board[0] == self.board[3] == self.board[6] or
            player == self.board[1] == self.board[4] == self.board[7] or
            player == self.board[2] == self.board[5] == self.board[8] or
            player == self.board[0] == self.board[4] == self.board[8] or
            player == self.board[2] == self.board[4] == self.board[6]): 
            return True
        else: return False

    def get_spot(self, spot):
        return self.board[spot]

    def set_spot(self, spot, player):
        self.board[spot] = player