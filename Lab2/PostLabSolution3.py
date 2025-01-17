import random

NounFile = open("/workspaces/GithubLabExerRepo/Lab2/nouns.txt") #Copied the path of the txt file and pasted.
Nouns = NounFile.read().splitlines() #Reads the file and returns a LIST for every "Enter key" entered in the txt file.
VerbFile = open("/workspaces/GithubLabExerRepo/Lab2/verbs.txt")
Verbs = VerbFile.read().splitlines()
ArticleFile = open("/workspaces/GithubLabExerRepo/Lab2/articles.txt")
Articles = ArticleFile.read().splitlines()
PrepositionFile = open("/workspaces/GithubLabExerRepo/Lab2/preposition.txt")
Prepositions = PrepositionFile.read().splitlines()

Nouns_T = tuple(Nouns) #From list it will be converted into a tuple.
Verbs_T = tuple(Verbs)
Articles_T = tuple(Articles)
Prepositions_T = tuple(Prepositions)

def make_sentence():
    return noun_sentence() + " " + verb_sentence()
def noun_sentence():
    return random.choice(Articles_T) + " " + random.choice(Nouns_T)
def verb_sentence():
    return random.choice(Verbs_T) + " " + noun_sentence() + " " + preposition()
def preposition():
    return random.choice(Prepositions_T) + " " + noun_sentence()
  
answer = int(input("How many sentences? "))
for i in range(answer):
    print(make_sentence())
