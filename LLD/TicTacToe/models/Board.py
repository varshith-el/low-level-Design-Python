
class Board:

    def __init__(self,size) -> None:
        self.size = int(size)
        self.board = [[None for _ in range(self.size)] for size in range(self.size)] 

    def add_piece(self, row, col,playing_piece):
        if row < 0 or row >= 3 or col >= 3  or col < 0:
            return False
        elif self.board[row][col] != None:
            return False
        else:
            self.board[row][col] = playing_piece
            return True

    def get_free_cells(self):
        freeCells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    freeCells.append(self.board[i][j])
        return freeCells


    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(self.board[i][j].piece_type.name, end=" | ")
                else:
                    print(" ", end=" | ")
            print()