class Player:
    def __init__(self, char):
        self.character = char

    def choose_action(self,state):
        pass


class Game:
    def __init__(self, gameBoard, player1, player2):
        self.gameBoard = gameBoard
        self.Player1 = player1
        self.Player2 = player2

    def play(self):
        print(self.gameBoard.pprint_string())

        while not self.gameBoard.winner():
            self.Player1.choose_action(self.gameBoard)
            print(self.gameBoard.pprint_string())
            if self.gameBoard.winner():
                print("X Wins!")
                break
            self.Player2.choose_action(self.gameBoard)
            print(self.gameBoard.pprint_string())
            if self.gameBoard.winner():
                print("O Wins!")
                break
            if self.gameBoard.num_empties() == 0:
                print("Tie")
                break
