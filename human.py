import game


class HumanPlayer(game.Player):
    def choose_action(self, state):
        possActions = state.actions(self.character)
        for i in range(len(possActions)):
            print("{}: {}".format(i,possActions[i]))

        while True:
            userMove = int(input("Please choose an action: "))
            if int(userMove) < len(possActions) and int(userMove) >= 0 :
                break
            else:
                print("Please enter an option from above")

        state.execute(possActions[userMove])