
from .PlayingPiece import PlayingPiece
from .PieceType import PieceType

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

    def thsprint(self):
        print(self.piece_type)