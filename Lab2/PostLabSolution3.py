import random

NounFile = open("nouns.txt")
Nouns = NounFile.read().splitlines()
VerbFile = open("verbs.txt")
Verbs = VerbFile.read().splitlines()
ArticleFile = open("articles.txt")
Articles = ArticleFile.read().splitlines()
PrepositionFile = open("preposition.txt")
Prepositions = PrepositionFile.read().splitlines()

def make_sentence():
    return noun_sentence() + " " + verb_sentence()
def noun_sentence():
    return random.choice(Articles) + " " + random.choice(Nouns)
def verb_sentence():
    return random.choice(Verbs) + " " + noun_sentence() + " " + preposition()
def preposition():
    return random.choice(Prepositions) + " " + noun_sentence()
  
answer = int(input("How many sentences? "))
for i in range(answer):
    print(make_sentence())
