import json
import time
import code

import urllib.parse
import urllib.request

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: https://miopia.grupolys.org/demo/'''

__url__ = 'https://miopia.grupolys.org/api/v1.0/polarity/en/supervised/'

def sentiment(text, token=None):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.
    Reference:
    https://docs.python.org/3.5/howto/urllib2.html

    Added timeouts due to the API rate limitations found here:
    https://miopia.grupolys.org/docs#faqs
    '''

    global __url__
    if token:
        time.sleep(2.05)
    else:
        time.sleep(61)
    values = {'text': text}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(__url__, data)
    sentiment = False

    with urllib.request.urlopen(req) as response:
        sentiment = response.read()
        sentiment = sentiment.decode('utf-8')
        sentiment = json.loads(sentiment)
        sentiment = sentiment['polarity']
    if sentiment:
        return [(text, sentiment)]
    else:
        raise(Exception('Could not get a sentiment value'))
