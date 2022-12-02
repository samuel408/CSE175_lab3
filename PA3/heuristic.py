#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# PLACE YOUR NAME AND THE DATE HERE
#


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0
#  todo itterate through time steps and calculate the probability using value functions of minimax

    # PLACE YOUR CODE HERE
    # delay iterates through min and max time steps
    # got help from TA Yasemin Gokcin understanding how  get expected value over delays using an iterative approach.
    for delayTimes in range(min_time_steps, max_time_steps):
        # sets the remaining time in the state as the value of the delay.
        state.time_remaining = delayTimes

        # sets val equal to its self plus the product of the probability of time and value of the state and ply.
        val += (value(state,ply) * probability_of_time(delayTimes) )
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value 
    # of a state.

    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    # PLACE YOUR CODE HERE
    # todo create a heurisitic funtion that uses board specifications to create strategy in the game
    # todo create strategy by getting the board size
    size = board_size
    # TODO get board location for strategy.
    compLoc = size - state.w_loc
    humanLoc = size - state.e_loc
    #todo create variables for players.
    computer = Player.west
    human = Player.east


    # TODO create scenarios where if the max payoff is 100 the computer wins
    if state.current_turn is computer:# if it is the computers turn
        if humanLoc > compLoc:
            val = -100

    #TODO create scenarios where if the max payoff is -100 the human wins
    if state.current_turn is human:#if it is the humans turn
        if compLoc > humanLoc:
            val = 100


    return val
