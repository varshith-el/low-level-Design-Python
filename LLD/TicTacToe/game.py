from queue import deque
from models.Board import Board
from models.Player import Player
from models.PlayingPieceX import PlayingPieceX
from models.PlayingPieceO import PlayingPieceO
from models.PieceType import PieceType

class Game:
    def __init__(self) -> None:
        self.gameboard = None
        self.players = deque()

    def initializeGame(self):
        xPiece = PlayingPieceX()
        opiece = PlayingPieceO()

        player1 = Player("Player1", xPiece)
        player2 = Player("Player2", opiece)

        self.players.append(player1)
        self.players.append(player2)

        self.gameboard = Board(3)


    def startGame(self):
        noWinner = True

        while noWinner:
            playerturn = self.players.popleft()

            self.gameboard.print_board()

            print(f"Player:{playerturn.name} Enter Row and Col please.")
            s = input()
            values = s.split(",")
            input_row = int(values[0])
            input_col = int(values[1])

            pieceAdded = self.gameboard.add_piece(input_row,input_col, playerturn.playing_piece)
            print(pieceAdded)

            if not pieceAdded:
                print("Incorrect position choosen,try again!")
                self.players.appendleft(playerturn)
                continue
            self.players.append(playerturn)

            winner = self.check_winner(input_row, input_col,playerturn.playing_piece)
            if winner:
                return playerturn.name

    def check_winner(self, row, column, piece_type):
        row_match = all(self.gameboard.board[row][i] is not None and self.gameboard.board[row][i].piece_type == piece_type for i in range(self.gameboard.size))
        column_match = all(self.gameboard.board[i][column] is not None and self.gameboard.board[i][column].piece_type == piece_type for i in range(self.gameboard.size))
        diagonal_match = all(self.gameboard.board[i][i] is not None and self.gameboard.board[i][i].piece_type == piece_type for i in range(self.gameboard.size))
        anti_diagonal_match = all(self.gameboard.board[i][self.gameboard.size - i - 1] is not None and self.gameboard.board[i][self.gameboard.size - i - 1].piece_type == piece_type for i in range(self.gameboard.size))

        return row_match or column_match or diagonal_match or anti_diagonal_match