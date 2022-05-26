import pandas as pd
from itertools import combinations
import numpy as np


def get_vector(hand):
    vec = np.zeros(len(cards))

    for c in hand:
        vec += np.array(card_dict[c])
    return vec


data = pd.read_csv('card_vectors.csv')
cards = data['card']
data.set_index('card', inplace=True)

card_dict = {}
for card in cards:
    card_dict[card] = list(data.loc[card])

# ALL POSSIBLE HAND COMBINATIONS
hand_combinations = list(combinations(cards, 5))

# VECTORS FOR ALL POSSIBLE HAND COMBINATIONS
hand_vectors = []
for hand in hand_combinations:
    hand_vectors.append(get_vector(hand))

# HUUUUUUGE DATASET
comb_dataset = pd.DataFrame(hand_vectors, index=hand_combinations)

# SAVING
comb_dataset.to_csv('hand_combinations.csv')
