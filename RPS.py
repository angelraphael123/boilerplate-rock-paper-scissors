import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    n = 3
    if len(opponent_history) < n:
        return random.choice(["R", "P", "S"])

    # Look for patterns in the opponent's history
    pattern = "".join(opponent_history[-n:])
    possibilities = ["R", "P", "S"]
    next_move = {k: 0 for k in possibilities}

    for i in range(len(opponent_history) - n):
        if "".join(opponent_history[i:i+n]) == pattern:
            next_index = i + n
            if next_index < len(opponent_history):
                next_move[opponent_history[next_index]] += 1

    # Predict the most likely next move based on pattern
    prediction = max(next_move, key=next_move.get)

    # Define counter moves to predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    return counter_moves[prediction]
