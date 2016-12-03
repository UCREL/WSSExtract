import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://werfamous.com/'''

__url__ = 'http://werfamous.com/'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.'''

    global __url__

    browser = RoboBrowser()
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form = browser.get_forms()[0]
    form['mytext'].value = text
    browser.submit_form(form)

    # Regular expression reference:
    # http://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
    all_text = str(browser.select('html'))
    sentiment_text = re.findall('<h3>Twitter results[\w\W]*?(?=<br>)', all_text)[0]
    sentiment_text = re.findall('Sentiment analysis score.*?[\d.]+', sentiment_text)[0]
    sentiment_value = float(re.findall('[\d.]+', sentiment_text)[0])
    return [(text, sentiment_value)]
