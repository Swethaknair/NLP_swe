import nltk
from nltk.corpus import wordnet

# Download WordNet data if not already downloaded
nltk.download('wordnet')

def explore_sentence_meanings(sentence):
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        synsets = wordnet.synsets(token)
        print(f"Word: {token}")
        if synsets:
            for synset in synsets:
                print("Synset:", synset.name())
                print("Definition:", synset.definition())
                print("Examples:", synset.examples())
        else:
            print("No synsets found for this word.")
        print()

# Example sentence
sentence = input("enter input:")

explore_sentence_meanings(sentence)
