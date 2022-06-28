
import random
from IPython.display import display
import math
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player, connor


def player(prev_play, opponent_history=[], my_play=[]):
    opponent_history.append(prev_play)
    if prev_play == '':
        prev_play = 'R'
    if len(opponent_history)>4:
        df = pd.DataFrame({'History': opponent_history[:-1], 'Move': opponent_history[1:], 'My Plays': my_play})
        X = pd.get_dummies(df, columns=['History', 'My Plays']).drop(['Move'], axis=1)
        y = pd.get_dummies(df,columns=['Move']).drop(['History', 'My Plays'],axis=1)
        Xtest = X.iloc[-1:]

        # Begin Decision Tree Model
        X_train, test_x, y_train, test_lab = train_test_split(X, y, test_size=0.7, random_state=42)
        # clf = DecisionTreeClassifier(max_depth=4, random_state=42)
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)
        next_move = clf.predict(Xtest)
        y.loc[len(y.index)] = next_move[0]
        move = pd.Series.tolist(y.idxmax(1)[-1:])[0]
        if move == 'Move_P':
            player_choice = 'S'
        elif move == 'Move_R':
            player_choice = 'P'
        else:
            player_choice = 'R'

        my_play.append(player_choice)
    else:
        player_choice = random.choice(['R', 'P', 'S'])
        my_play.append(player_choice)
    return player_choice

play(player, abbey, 1000)



