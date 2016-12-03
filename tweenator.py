import random
import time

import urllib.parse
import urllib.request

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://tweenator.com/index.php?page_id=2'''

__url__ = 'http://tweenator.com/response/sentiment_response.php'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.
    Reference:
    https://docs.python.org/3.5/howto/urllib2.html
    '''

    # This is required as PHP has a different url encoder compared to python
    # reference:
    # http://stackoverflow.com/questions/996139/urlencode-vs-rawurlencode
    reserved_terms = [";", "/", "?", ":", "@", "&", "=", "+", ",", "$", " "]
    escaped_text = []
    for char in text:
        if char in reserved_terms:
            escaped_text.append(urllib.parse.quote_plus(char))
        else:
            escaped_text.append(char)
    escaped_text = ''.join(escaped_text)

    global __url__
    time.sleep(random.randint(10,25))

    full_url = __url__ + "?tweet_text=" + escaped_text
    sentiment_data = urllib.request.urlopen(full_url)
    sentiment_value = int(sentiment_data.read().decode('utf-8'))
    if sentiment_value == 0:
        return [(text, 'negative')]
    elif sentiment_value == 4:
        return [(text, 'positive')]
    else:
        raise(Exception('The sentiment value {} is not assigned to a polarity'.format(sentiment_value)))
