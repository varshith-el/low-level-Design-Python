from game import Game

def main():
    game = Game()
    game.initializeGame()
    print("Game winner is: " + game.startGame())

if __name__ == "__main__":
    main()