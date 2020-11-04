import game, random, math


class RandomPlayer(game.Player):
    def choose_action(self, state):
        possActions = state.actions(self.character)
        randMove = random.randrange(len(possActions))

        state.execute(possActions[randMove])


class MinimaxPlayer(game.Player):
    def choose_action(self, state):
        action = self.miniMaxDecision(state)

        state.execute(action)

    def miniMaxDecision(self, state):

        minVal = -20

        possActions = state.actions(self.character)
        for a in possActions:
            print("Considering Tree: ", a)
            cloneState = state.clone()
            successorState = cloneState.execute(a)
            newMinVal = self.MinValue(successorState)
            #print("newMinVal pre check:",newMinVal)

            if newMinVal > minVal:
                minVal = newMinVal
                bestAction = a

            print("SucessorState Value: ", minVal)

        print("best action: ", bestAction)
        return bestAction

    def MaxValue(self, state):
        # termination conditions
        if state.winner() == self.character:
            return 1
        elif state.winner() == oppositeCharacter(self.character):
            return -1
        elif state.num_empties() == 0:
            return 0

        v = -20

        possActions = state.actions(self.character)

        for a in possActions:
            successorState = self.results(state, a)
            newMin = self.MinValue(successorState)
            v = max(v, newMin)
        return v

    def MinValue(self, state):
        # termination conditions
        if state.winner() == self.character:
            return 1
        elif state.winner() == oppositeCharacter(self.character):
            return -1
        elif state.num_empties() == 0:
            return 0

        v = 20

        possActions = state.actions(oppositeCharacter(self.character))

        for a in possActions:
            successorState = self.results(state, a)
            newMax = self.MaxValue(successorState)
            v = min(v, newMax)
        return v

    def results(self, state, action):
        cloneState = state.clone()
        newState = cloneState.execute(action)
        return newState

def oppositeCharacter(character):
    if character == "X":
        return "O"
    elif character == "O":
        return "X"
