First setup standard python3 venv.

Then install nltk and praw via pip.

Open up python3 and run the following to download the necessary NLTK packages:

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

You will need your own reddit dev account and app, create a praw.ini file in the same directory as analzyer.py and fill in your credentials.  Replace paul_dev in the script with whatever you named your profile.

Simply run python3 analyzer.py, and you will get a sorted dict of all the subjects in the last 100 post titles.
