#Paul Tudan
#3/18/21
#to the moon?

import praw
import nltk
from nltk.corpus import stopwords


SUB_NAME = "CryptoMoonShots"
RELEVANT_POS = ["NN", "NNP", "NNS"]
PRAW_AGENT = "paul_dev"

reddit = praw.Reddit(
            PRAW_AGENT,
            user_agent="SubjectAnalyzer/0.1.0 by ChopChopBoogieBoogie",
            )

stop = stopwords.words('english')
subjects = {}
for submission in reddit.subreddit(SUB_NAME).new(limit=100):
    title = submission.title
    title = ' '.join([i for i in title.split() if i not in stop])
    sentences = nltk.sent_tokenize(title)
    for sentence in sentences:
        words = nltk.tokenize.word_tokenize(sentence)
        tags = nltk.pos_tag(words)
        for t in tags:
            if t[1] in RELEVANT_POS:
                subjects[t[0]] = subjects.get(t[0], 0) + 1

print({k: v for k, v in sorted(subjects.items(), key = lambda item: item[1])})


