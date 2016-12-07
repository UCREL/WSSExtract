import json
import time

import urllib.parse
import urllib.request

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://text-processing.com/demo/sentiment/'''

__url__ = 'http://text-processing.com/api/sentiment/'

def sentiment(text, token=None):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.
    Reference:
    https://docs.python.org/3.5/howto/urllib2.html

    Added timeouts due to the API rate limitations found here (1000 calls ]
    per day per IP address):
    http://text-processing.com/docs/index.html
    '''

    global __url__
    time.sleep(2.05)

    values = {'text': text}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(__url__, data)
    sentiment = False

    with urllib.request.urlopen(req) as response:
        sentiment = response.read()
        sentiment = sentiment.decode('utf-8')
        sentiment = json.loads(sentiment)
        sentiment_label = sentiment['label']
        # More fine grained results
        sentiment_results = sentiment['probability']
        pos_prob = sentiment_results['pos']
        neu_prob = sentiment_results['neutral']
        neg_prob = sentiment_results['neg']

    if sentiment_label:
        return [(text, sentiment_label)]
    else:
        raise(Exception('Could not get a sentiment value'))
