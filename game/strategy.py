"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
import random
from typing import Any
from adt import Stack, Tree


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return the move that minimizes the possible loss for a player by recursion.
    """
    d = {}
    old_state = game.current_state
    for move in game.current_state.get_possible_moves():
        new_state = game.current_state.make_move(move)
        game.current_state = new_state
        state_score = recursive_minimax_state(game, new_state) * -1
        game.current_state = old_state
        if state_score in d:
            d[state_score].append(move)
        else:
            d[state_score] = [move]
    if 1 in d:
        return random.choice(d[1])
    elif 0 in d:
        return random.choice(d[0])
    return random.choice(d[-1])


def recursive_minimax_state(game: Any, current_state: Any) -> int:
    """
    Return the state score of the current_state by using recursion.
    """
    if game.is_over(current_state):
        if game.is_winner(current_state.get_current_player_name()):
            return 1
        elif not game.is_winner('p1') and not game.is_winner('p2'):
            return 0
        return -1
    score_list = []
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)
        game.current_state = new_state
        score_list.append(recursive_minimax_state(game, new_state) * -1)
    return max(score_list)


# noinspection PyDunderSlots
def iterative_minimax(game: Any) -> Any:
    """
    Return the move that minimizes the possible loss for a player iteratively.
    """
    s = Stack()
    tree = Tree(game.current_state, [])
    s.add(tree)
    while not s.is_empty():
        tree = s.remove()
        current_state = tree.value
        if game.is_over(current_state):
            # change the current state of game in order to use is_winner()
            # to justify whether it is a tie.
            game.current_state = current_state
            if game.is_winner(current_state.get_current_player_name()):
                tree.highest_score = 1
            elif not game.is_winner('p1') and not game.is_winner('p2'):
                tree.highest_score = 0
            else:
                tree.highest_score = -1
        elif tree.children != []:
            tree.highest_score = max([x.highest_score * -1
                                      for x in tree.children])
        else:
            for move in current_state.get_possible_moves():
                new_state = current_state.make_move(move)
                tree.children.append(Tree(new_state, []))
            s.add(tree)
            for child_tree in tree.children:
                s.add(child_tree)
    current_state = tree.value
    # change back the current state of game
    game.current_state = current_state
    if tree.highest_score == -1:
        return random.choice(current_state.get_possible_moves())
    elif tree.highest_score == 0:
        best_move = [current_state.get_possible_moves()[i]
                     for i in range(len(current_state.get_possible_moves()))
                     if tree.children[i].highest_score == 0]
        return random.choice(best_move)
    best_move = [current_state.get_possible_moves()[i]
                 for i in range(len(current_state.get_possible_moves()))
                 if tree.children[i].highest_score == -1]
    return random.choice(best_move)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
