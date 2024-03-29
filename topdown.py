import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'I'
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
    P -> 'with' | 'in'
""")
parser = ChartParser(grammar)
sentence = "I chased the dog"
words = sentence.split()
for tree in parser.parse(words):
    tree.pretty_print()
