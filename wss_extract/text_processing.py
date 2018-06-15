'''
Module contains the following class:

1. :py:class:`TextProcessing`
'''
import json
import time
from typing import Dict, Any, Union
import random
import urllib.parse
import urllib.request

from sentiment_api import SentimentAPI


class TextProcessing(SentimentAPI):
    '''
    Concrete class of the abstract class :py:class:`SentimentAPI`.

    Attributes:

    1. url -- url address of the Text Processing sentiment api demo \
    `form <http://text-processing.com/demo/sentiment/>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.

    Functions:

    1. sentiment -- Finds the sentiment of a text by using the sentiment \
    system at the following `URL <http://text-processing.com/demo/sentiment/>`_
    '''

    @property
    def url(self):
        return 'http://text-processing.com/api/sentiment/'

    @property
    def timeout(self):
        return (10, 25)

    def sentiment(self, text: str,
                  sentiment_mapper: Union[None, Dict] = None) -> Any:
        '''
        :param text: The text to input into the sentiment system/ web form
        :param sentiment_mapper: Optional default None. If not None it is \
        a dict that maps the sentiment values that come from the system into \
        a different value e.g. if the system output 1 and -1 a mapper could \
        be {1: 'pos', -1: 'neg'}
        :returns: One of the following Strings: 'pos', 'neg', 'neutral'
        '''

        time.sleep(random.randint(*self.timeout))
        values = {'text': text}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(self.url, data)
        sentiment = False

        with urllib.request.urlopen(req) as response:
            sentiment = response.read()
            sentiment = sentiment.decode('utf-8')
            sentiment = json.loads(sentiment)
            sentiment_label = sentiment['label']
            # More fine grained results
            # sentiment_results = sentiment['probability']
            # pos_prob = sentiment_results['pos']
            # neu_prob = sentiment_results['neutral']
            # neg_prob = sentiment_results['neg']

        if sentiment_label:
            if sentiment_mapper is not None:
                return sentiment_mapper[sentiment_label]
            return sentiment_label
        else:
            raise ValueError('Could not get a sentiment value from Text '
                             'Processing')

    def _process_sentiment_page(self, browser, text):
        '''
        Not required for this class
        '''
        pass
