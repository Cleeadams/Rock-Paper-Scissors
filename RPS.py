import random
from IPython.display import display
import math
import pandas as pd
from numpy import reshape
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player



def player(prev_play, opponent_history = [], response=[], my_history=[]):

    if len(opponent_history) > 10:
        global df, X, y, test_pred_decision_tree
        dic = {0: 'P', 1: 'R', 2: 'S'}
        response.append(prev_play)
        df = pd.DataFrame({'New Move': response, 'History': opponent_history, 'My History': my_history})
        df = df.iloc[1:]
        dftest = pd.DataFrame({'History': [prev_play], 'My History': my_history.pop()})
        X_df = df.drop(columns='New Move')
        y_df = df['New Move']
        X_df = X_df.apply(LabelEncoder().fit_transform)
        X = OneHotEncoder(sparse=False).fit_transform(X_df.values)
        X = X.shape
        y = LabelEncoder().fit_transform(y_df.values)
        y = y.reshape(-1, 1)
        xTest = dftest.apply(LabelEncoder().fit_transform)
        xTest = OneHotEncoder(sparse=False).fit_transform(xTest.values)
        xTest = xTest.shape
        opponent_history.append(prev_play)
        X_train, test_x, y_train, test_lab = train_test_split(X, y,test_size=0.4,random_state=42)
        clf = DecisionTreeClassifier(max_depth=3,random_state=42)
        clf.fit(X_train,y_train)
        test_pred_decision_tree = clf.predict(xTest)
        # player_choice = dic.get(test_pred_decision_tree[0])
        my_history.append(player_choice)
        return player_choice
    elif len(opponent_history)>0:
        response.append(prev_play)
        opponent_history.append(prev_play)
        player_choice = random.choice(['R', 'P', 'S'])
        my_history.append(player_choice)
        return player_choice
    else:
        opponent_history.append(prev_play)
        player_choice = random.choice(['R','P','S'])
        my_history.append(player_choice)
        return player_choice



play(player,quincy,3000)






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