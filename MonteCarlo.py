from random import randint
from collections import defaultdict

# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note: t
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.

# To estimate the best number to hold at, we'll try to estimate the probability of winning
# for each possible hold value between n-5 and n.
# Once we have this, we will know which hold value to use for our strategy.

# This function should try each possible hold value 1000000 times. For each time, play a random
# game. If Player 1 wins, increment the appropriate value in the win_table dictionary.

# n is the limit.

# create policy for best value to hold at, 1-4 always roll,
# make for loops for different hold values and run 1mil times then divide wins by number of games
# P2 is dealer has no choice



def monte_carlo_approach(n) :
    win_table = defaultdict(int)
    hold_values = [n-5, n-4, n-3, n-2, n-1, n]
    for i in range(1000000):
        for hold in hold_values:
            winner, hold_value = approach(n, hold)
            if winner == 0:
                win_table[hold_value] += 1
    for item in sorted(win_table.keys()) :
        print("%d: %f" % (item, win_table[item]/1000000))


def approach(limit, hold) :
    """"
    Returns 0 if player 1 wins, 1 if player 2 wins
    P1 automatically wins if they hit the target score
    If both players exceed the limit, the winner is the player closest to the target
    """
    scores = [0,0]
    winner = None
    exit = False
    while scores[0] < limit and not exit:
        roll = randint(1, 6)
        scores[0] += roll
        if scores[0] == hold:
            break
        if scores[0] == limit:
            return 0, hold

    while scores[1] < limit:
        roll = randint(1, 6)
        scores[1] += roll

    if exit and scores[1] > limit:
        winner = 0
    elif abs(limit - scores[1]) > abs(limit - scores[0]):
        winner = 0
    else:
        winner = 1

    return winner,hold



limit = 10
monte_carlo_approach(limit)







