from models.game import Game
from models.player import Player

def main():
    boardSize = int(input("Enter board Size\n"))
    numberOfPlayers = int(input("Enter number of players\n"))
    numSnakes = int(input("Enter number of snakes\n"))
    numLadders = int(input("Enter number of ladders\n"))

    game = Game(numLadders, numSnakes, boardSize)
    for i in range(numberOfPlayers):
        pName = input("Enter player name\n")
        player = Player(pName)
        game.addPlayer(player)
    game.playGame()

if __name__ == "__main__":
    main()