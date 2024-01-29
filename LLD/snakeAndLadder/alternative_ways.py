"""
Here we store the snakes and ladders in the board Object.
"""

"""
Alternatively we can also create cells class and initiate cells of n size and assign the snakes and ladders to them.
"""
# game.py
import random
from collections import deque
from .board import Board
from .dice import Dice
from .player import Player

class Game:
    #initialize necessary objects
    def __init__(self, numberOfLadders, numberOfSnakes, boardSize):
        #for storing and rotating the player turns
        self._players = deque()
        #initialize the board
        self._board = Board(boardSize, numberOfLadders, numberOfSnakes)
        #dice object
        self._dice = Dice(1, 6, 2)
        #make the board ready(place the ladders and snakes)
        self._board.initBoard()

    def addPlayer(self, player):
        self._players.append(player)
    #users roll dice
    def playGame(self):
        while True:
            player = self._players.popleft()
            print(f"{player._name}'s turn. Type R/r to roll.")
            roll = input().lower()
            if roll == 'r':
                val = self._dice.roll()
                newPosition = player._position + val
                if newPosition > self._board._end:
                    player._position = player._position
                    self._players.append(player)
                else:
                    player._position = self.getNewPosition(newPosition,player._name)
                    if player._position == self._board._end:
                        player._won = True
                        print(f"Player {player._name} Won.")
                    else:
                        print(f"Setting {player._name}'s new position to {player._position}")
                        self._players.append(player)
            else:
                print("Invalid input. Please type R/r to roll.")
                self._players.append(player)
            if len(self._players) < 2:
                break

    def getNewPosition(self, newPosition,player_name):
        for snake in self._board._snakes:
            if snake._head == newPosition:
                print(f"Snake ate {player_name} ")
                return snake._tail
        for ladder in self._board._ladders:
            if ladder._start == newPosition:
                print(f"new position is{newPosition}")
                print("Climbed ladder")
                return ladder._end
        return newPosition

# board.py
from .ladder import Ladder
from .snake import Snake

class Board:
    def __init__(self, size, numberOfLadders, numberOfSnakes):
        self._start = 1
        self._end = size
        self._size = size
        self._snakes = [Snake(0, 0) for _ in range(numberOfSnakes)]
        self._ladders = [Ladder(0, 0) for _ in range(numberOfLadders)]

    def initBoard(self):
        slSet = set()
        for i in range(len(self._snakes)):
            while True:
                snakeStart = random.randint(self._start, self._size)
                snakeEnd = random.randint(self._start, self._size)
                if snakeEnd >= snakeStart:
                    continue
                startEndPair = str(snakeStart) + str(snakeEnd)
                if startEndPair not in slSet:
                    self._snakes[i] = Snake(snakeStart, snakeEnd)
                    slSet.add(startEndPair)
                    break

        for i in range(len(self._ladders)):
            while True:
                ladderStart = random.randint(self._start, self._size)
                ladderEnd = random.randint(self._start, self._size)
                if ladderEnd <= ladderStart:
                    continue
                startEndPair = str(ladderStart) + str(ladderEnd)
                if startEndPair not in slSet:
                    self._ladders[i] = Ladder(ladderStart, ladderEnd)
                    slSet.add(startEndPair)
                    break


