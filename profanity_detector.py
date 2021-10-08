import pandas as pd
import re

location1 = input("enter the file location of tweet file :	")
location2 = input("enter the file location  file containg bad words :	")

print("\noperation is running ...\n")

# for this tweet file I used this particular encoding
df = pd.read_csv(location1, encoding ="ISO-8859-1",index_col=False)

def tokenize(sentence): 
    return re.findall(r'\w+', sentence.lower())
    

def profanity_degree(tokens):
    return sum(1 for i in tokens if i in profane_words)/len(tokens)
    
    
with open(location2) as file:
    profane_words = file.readlines()
    profane_words = [profane_word.rstrip() for profane_word in profane_words]
    
df["tokens"] = df.tweets.apply(tokenize)

df["profanity_degree"] = df.head(100000).tokens.apply(profanity_degree)


# saving the result ( tweet file along with profanity degree for every tweet )
df[["tweets","profanity_degree"]].to_csv("tweets_output.csv",index=False)

print("results have been saved in filename :  tweets_output.csv!")
