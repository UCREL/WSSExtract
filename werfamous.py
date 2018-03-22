import random
import re
import time
import code

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://werfamous.com/sentimentanalyzer/'''

__url__ = 'http://werfamous.com/sentimentanalyzer/'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.'''

    global __url__

    browser = RoboBrowser()
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form =  browser.get_forms()[0]
    form['mytext'].value = text
    browser.submit_form(form)

    code.interact(local=locals())
    sentiment_string = browser.select('h3')[0].string
    print(sentiment_string)
    sentiment_string = re.findall('score is[^%]*', sentiment_string)[0]
    print(sentiment_string)

    # Make it conform to the other return statements of a list of tuples
    # containing sentence, sentiment value of that sentence.
    sentiment_values    = re.findall('\d+', sentiment_string)[0]
    sentences           = [text]
    sentences_sentiment = list(zip(sentences, sentiment_values))
    return sentences_sentiment
