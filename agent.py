import game, random


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
        nodeDepth = 0
        possActions = state.actions(self.character)
        for a in possActions:
            cloneState = state.clone()
            successorState = cloneState.execute(a)
            newMinVal = self.MinValue(successorState, nodeDepth+1)

            if newMinVal > minVal:
                minVal = newMinVal
                bestAction = a

        return bestAction

    def MaxValue(self, state, nodeDepth):
        # termination conditions
        if state.winner() is not None:
            return self.terminationConditions(state,nodeDepth)

        v = -20

        possActions = state.actions(self.character)

        for a in possActions:
            successorState = self.results(state, a)
            newMin = self.MinValue(successorState,nodeDepth+1)
            v = max(v, newMin)
        return v

    def MinValue(self, state, nodeDepth):
        # termination conditions
        if state.winner() is not None:
            return self.terminationConditions(state,nodeDepth)

        v = 20

        possActions = state.actions(oppositeCharacter(self.character))

        for a in possActions:
            successorState = self.results(state, a)
            newMax = self.MaxValue(successorState,nodeDepth+1)
            v = min(v, newMax)
        return v

    def results(self, state, action):
        cloneState = state.clone()
        newState = cloneState.execute(action)
        return newState

    def terminationConditions(self, state,nodeDepth):
        if state.winner() == self.character:
            return 1/nodeDepth
        elif state.winner() == oppositeCharacter(self.character):
            return -1/nodeDepth
        elif state.num_empties() == 0:
            return 0

def oppositeCharacter(character):
    if character == "X":
        return "O"
    elif character == "O":
        return "X"
