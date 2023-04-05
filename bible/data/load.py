import pickle
import pandas as pd

with open('bible/data/bible_dict.pickle', 'rb') as f:
    data = pd.read_pickle(f)

print(data)