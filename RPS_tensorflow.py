from RPS_game import *
import random
import tensorflow as ts



def tree(history, response)


def player(prev_play, opponent_history=[]):
    if prev_play == '' or len(opponent_history) < 5:
        opponent_history.append(prev_play)
        opponent_history[0] = 'R'
        player_choice = random.choice(['R', 'P', 'S'])
    else:
        opponent_history.append(prev_play)
        response = opponent_history[1:]
        move = trees(opponent_history, response)
        choices = {'Response_R': 'P', 'Response_P': 'S', 'Response_S': 'R'}
        player_choice = choices[move]
    return player_choice


play(player, quincy, 1000)