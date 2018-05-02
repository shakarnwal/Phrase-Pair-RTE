import pandas as pd

df = pd.read_csv('phrase_pair_entailment.csv')

for index,row in df.iterrows():
    if row['majority_label'] == 'synonym':
        row['majority_label'] = 'equivalence'
    elif row['majority_label'] == 'antonym':
        row['majority_label'] = 'alternation'
    elif row['majority_label'] == 'hypernym':
        row['majority_label'] = 'entailment'
    elif row['majority_label'] == 'hyponym':
        t1 = row['text']
        row['text'] = row['hypothesis']
        row['hypothesis'] = t1
        row['majority_label'] = 'entailment'

df['majority_label'].unique()

df.to_csv('phrase_pair_5_classes.csv', index=False)
