#Paul Tudan
#3/18/21
#to the moon?

import praw
import nltk
import re
from nltk.corpus import stopwords

stop = stopwords.words('english')
SUB_NAME = "CryptoMoonShots"
RELEVANT_POS = ["NN", "NNP", "NNS"]
PRAW_AGENT = "paul_dev"
ADDRESS_REGEX = "0x[a-fA-F0-9]{40}$"
POOCOIN_URL = "https://poocoin.app/tokens/"

def clear_stop_words(text):
    return ' '.join([i for i in text.split() if i not in stop])

def address_from_text(text):
    text = clear_stop_words(text)
    words = nltk.tokenize.word_tokenize(text)
    retset = set()
    for w in words:
        l = re.findall(ADDRESS_REGEX, w)
        for a in l:
            retset.add(a.lower())
    return retset

reddit = praw.Reddit(
            PRAW_AGENT,
            user_agent="SubjectAnalyzer/0.1.0 by ChopChopBoogieBoogie",
            )

subjects = {}
potential_coins = {}
potential_coin_addresses = {}
for submission in reddit.subreddit(SUB_NAME).new(limit=100):
    title = submission.title
    title = clear_stop_words(title)
    sentences = nltk.sent_tokenize(title)
    for sentence in sentences:
        words = nltk.tokenize.word_tokenize(sentence)
        tags = nltk.pos_tag(words)
        for t in tags:
            if t[1] in RELEVANT_POS:
                subjects[t[0]] = subjects.get(t[0], 0) + 1
                if t[0].isupper():
                    potential_coins[t[0]] = potential_coins.get(t[0], 0) + 1
                    if t[0] not in potential_coin_addresses:
                        potential_coin_addresses[t[0]] = set()
                    potential_coin_addresses[t[0]].update(address_from_text(submission.selftext))
print({k: v for k, v in sorted(subjects.items(), key = lambda item: item[1])})

print("COINS??")
for k, v in sorted(potential_coins.items(), key = lambda item: item[1]):
    print(k)
    if len(potential_coin_addresses[k]) > 0:
        for a in potential_coin_addresses[k]:
            print(POOCOIN_URL + a)
    
