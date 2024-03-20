import nltk
# Download WordNet data
nltk.download('wordnet')
from nltk.corpus import wordnet
syn = wordnet.synsets('hello')[0]
print ("Synset name :  ", syn.name())
print ("\nSynset meaning : ", syn.definition())
print ("\nSynset example : ", syn.examples())
