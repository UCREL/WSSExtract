import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://textanalysisonline.com/pattern-sentiment-analysis'''

__url__ = 'http://textanalysisonline.com/pattern-sentiment-analysis'

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

    form =  browser.get_forms()[0]
    form['text'].value = text
    browser.submit_form(form)

    all_text = browser.select('html')[0]
    sentiment_value = re.findall('<h4>Analysis Result[\w\W]*?(?=</p>)',str(all_text))[0]
    sentiment_value = re.findall('Polarity = [\d\.-]*',str(sentiment_value))[0]
    sentiment_value = float(re.findall('[\d\.-]+',str(sentiment_value))[0])
    # Make it conform to the other return statements of a list of tuples
    # containing sentence, sentiment value of that sentence.
    sentiment_values    = [sentiment_value]
    sentences           = [text]
    sentences_sentiment = list(zip(sentences, sentiment_values))
    return sentences_sentiment
