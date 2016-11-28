import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: https://www.repustate.com/api-demo/'''

__url__ = 'https://www.repustate.com/api-demo/'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.'''

    global __url__

    class_ = 'form'
    browser = RoboBrowser()
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form =  browser.get_form(class_=class_)
    form['text'].value = text
    form['language'].value = 'en'
    browser.session.headers['Referer'] = __url__
    browser.submit_form(form)

    sentiment_table = browser.select('form')[0].select('table')[0]
    sentiment_value = re.findall('[\d.]+<',str(sentiment_table))[0].rstrip('<')
    # Make it conform to the other return statements of a list of tuples
    # containing sentence, sentiment value of that sentence.
    sentiment_values    = [sentiment_value]
    sentences           = [text]
    sentences_sentiment = list(zip(sentences, sentiment_values))
    return sentences_sentiment
