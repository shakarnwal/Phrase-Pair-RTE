import pandas as pd
from sklearn.linear_model import LogisticRegression
import nltk

def calc_binary_feat():

	df = pd.read_csv('phrase_pair_5_classes.csv')
	# all parameters not specified are set to their defaults
	logisticRegr = LogisticRegression(class_weight="auto")

	p1_substring_p2 = []                    #p1 is a substring of p2 
	p2_substring_p1 = []                    #p2 is a substring of p1 
	POSp1_POSp2 = []                        #POS(p1) == POS(p2) 
	lexical_p1_p2 =[]                       #Both p1 and p2 are lexical
	phrasal_p1_p2 = []                      #Either p1 and p2 are phrasal

	for index,row in df.iterrows():
    		p1_substring_p2.append(row['text'] in row['hypothesis'])
    		p2_substring_p1.append(row['hypothesis'] in row['text'])                      

	for index,row in df.iterrows():
    		POSp1_POSp2.append(nltk.pos_tag(nltk.word_tokenize(row['text']))[0][1] == nltk.pos_tag(nltk.word_tokenize(row['hypothesis']))[0][1])

	for index,row in df.iterrows():
   		lexical_p1_p2.append((' ' not in row['text']) and (' ' not in row['hypothesis']))
    		phrasal_p1_p2.append((' ' in row['text']) or (' ' in row['hypothesis']))    

	return p1_substring_p2,p2_substring_p1,POSp1_POSp2,lexical_p1_p2,phrasal_p1_p2

if __name__ == '__main__':
	calc_binary_feat()
