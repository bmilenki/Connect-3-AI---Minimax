import util
import connect3 as c3
import human
import game
import agent

def main():
    p1 = util.get_arg(1)
    p2 = util.get_arg(2)

    currState = c3.State()

    if p1 == "human":
        player1 = human.HumanPlayer("X")
    elif p1 == "random":
        player1 = agent.RandomPlayer("X")
    elif p1 == "minimax":
        player1 = agent.MinimaxPlayer("X")
    else:
        print("Player 1 has no agent of they type")

    if p2 == "human":
        player2 = human.HumanPlayer("O")
    elif p2 == "random":
        player2 = agent.RandomPlayer("O")
    elif p2 == "minimax":
        player2 = agent.MinimaxPlayer("O")
    else:
        print("Player 2 has no agent of they type")

    currGame = game.Game(currState, player1, player2)

    currGame.play()




if __name__ == "__main__":
    main()