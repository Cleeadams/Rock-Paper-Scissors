
import random
from IPython.display import display
import math
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player, connor


def player(prev_play, opponent_history=[], my_play=[]):
    opponent_history.append(prev_play)
    if len(opponent_history)>2:
        df = pd.DataFrame({'History': opponent_history[:-1], 'Move': opponent_history[1:]})
        X = pd.get_dummies(df, columns=['History']).drop(['Move'], axis=1)
        y = pd.get_dummies(df,columns=['Move']).drop(['History'],axis=1)
        Xtest = X.iloc[-1:]

        # Begin Decision Tree Model
        X_train, test_x, y_train, test_lab = train_test_split(X, y, test_size=0.2, random_state=42)
        clf = DecisionTreeClassifier(max_depth=2, random_state=42)
        clf.fit(X, y)
        next_move = clf.predict(Xtest)
        y.loc[len(y.index)] = next_move[0]
        move = pd.Series.tolist(y.idxmax(1)[-1:])[0]
        if move == 'Move_P':
            player_choice = 'S'
        elif move == 'Move_R':
            player_choice = 'P'
        else:
            player_choice = 'R'

        # print(player_choice)
        my_play.append(player_choice)
    else:
        player_choice = random.choice(['R', 'P', 'S'])
        my_play.append(player_choice)
    return player_choice

play(player, connor, 2000)







# occur_R = opponent_history.count('R')
# occur_P = opponent_history.count('P')
# occur_S = opponent_history.count('S')
# print(occur_S)
# print(occur_P)
# print(occur_R)
# total_occur = len(opponent_history)-1
# weight_R = math.floor(( (occur_P / total_occur) ) * 100)
# weight_P = math.floor(( (occur_S / total_occur) ) * 100)
# weight_S = math.floor(( (occur_R / total_occur) ) * 100)
# list = ['R']*weight_R
# list.extend(['P']*weight_P)
# list.extend(['S']*weight_S)
