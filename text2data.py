import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://text2data.org/Demo'''

__url__ = 'http://text2data.org/Demo'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.

    NOTE: if you are running this from the browser manually you will get
    different results if you do not remove the additional whitespace.'''

    global __url__

    action = '/Demo/Demo'
    browser = RoboBrowser()
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form =  browser.get_form(action=action)

    form['input'].value = text
    browser.submit_form(form)

    sentiment_table = browser.select('#divResults')[0]
    sentiment_value = re.findall('This document is:[^\)]*',str(sentiment_table))[0]
    sentiment_value = float(sentiment_value.split('(')[1])
    # Make it conform to the other return statements of a list of tuples
    # containing sentence, sentiment value of that sentence.
    sentiment_values    = [sentiment_value]
    sentences           = [text]
    sentences_sentiment = list(zip(sentences, sentiment_values))
    return sentences_sentiment
