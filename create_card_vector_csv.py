import pandas as pd

RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS_U = ["\u2660", "\u2663", "\u2665", "\u2666"]

deck_list = []

for suit in SUITS_U:
    for rank in RANKS:
        deck_list.append({
            'rank': rank,
            'suit': suit
        })

data = pd.DataFrame(deck_list)
data['card'] = data['suit'] + data['rank']
data = data['card']
data_v = pd.get_dummies(data, columns='card')
result = pd.concat([data, data_v], axis=1)
result.set_index(['card'], inplace=True)
old_col_name = list(result.columns)
new_col_name = [f"Card{i}" for i in range(len(old_col_name))]
columns_rename_dict = {}
for i in range(len(old_col_name)):
    old_name = old_col_name[i]
    new_name = new_col_name[i]
    columns_rename_dict[old_name] = new_name


# Saving
result.rename(columns=columns_rename_dict, inplace=True)
result.to_csv('card_vectors.csv')