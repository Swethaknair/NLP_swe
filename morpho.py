import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "this is a cat"

tokens = word_tokenize(text)

postags = pos_tag(tokens)

print("Original Text:", text)
print("\nPart-of-speech Tags:", postags)
