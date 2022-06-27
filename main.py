import random
import pandas as pd


opp = []
my_hist = []
prev_move = ''
for i in range(10):
    # This stores the opponents history
    opp.append(prev_move)
    # This is my reaction to his previous move
    my_move = random.choice(['R','P','S'])
    # This stores my moves
    my_hist.append(my_move)
    # This is the opponents new move
    prev_move = random.choice(['R','P','S'])

game = pd.DataFrame({'Opponents move': opp,'My move': my_hist})
print(game)



