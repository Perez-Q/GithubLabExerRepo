import random

NounFile = open("/workspaces/GithubLabExerRepo/Lab2/nouns.txt")
Nouns = NounFile.read().splitlines()
VerbFile = open("/workspaces/GithubLabExerRepo/Lab2/verbs.txt")
Verbs = VerbFile.read().splitlines()
ArticleFile = open("/workspaces/GithubLabExerRepo/Lab2/articles.txt")
Articles = ArticleFile.read().splitlines()
PrepositionFile = open("/workspaces/GithubLabExerRepo/Lab2/preposition.txt")
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
