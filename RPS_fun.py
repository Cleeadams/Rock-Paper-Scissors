import random
import pandas as pd
from RPS_game import play, quincy, abbey, mrugesh, human, random_player, kris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from six import StringIO
import pydot
from fpdf import FPDF
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def trainers(history, response):
    response.append('')
    df = pd.DataFrame({'History': history, 'Response': response})
    X = pd.get_dummies(df, columns=['History']).drop(['Response'], axis=1)
    y = pd.get_dummies(df, columns=['Response']).drop(['History'], axis=1)
    Xtest = X[-1:]
    X = X[1:]
    y = y[:-1]
    return X, y, Xtest

def trees(history, response):
    global X, y
    X, y, Xtest = trainers(history, response)
    clf = DecisionTreeClassifier(max_depth=2, random_state=42)
    clf.fit(X, y)
    # dot_data = StringIO()
    # pdf = FPDF()
    # export_graphviz(clf, out_file='tree.dot')
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    # graph[0].write_pdf("RPS.pdf")
    next_move = clf.predict(Xtest)
    y.loc[len(y.index)] = next_move[0]
    predicted_move = pd.Series.tolist(y.idxmax(axis=1)[-1:])[0]
    return predicted_move

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

play(player, kris, 1000)
