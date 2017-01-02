import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://www.socialmention.com/

 Note unlike the others this returns a mean sentiment value as the tool
 gives a Positive, neutral and negative sentiment therefore the score is
 (Positive count - Negative count) / (Positive + Negative + Neutral count)'''

__url__ = 'http://www.socialmention.com/'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.

    This system can only analyse text as one sentences does not split
    the text into sentences.

    Note unlike the others this returns a mean sentiment value as the tool
    gives a Positive, neutral and negative sentiment therefore the score is
    (Positive count - Negative count) / (Positive + Negative + Neutral count)

    There is a rate limit of 100 requests per day see here for more details:
    http://www.socialmention.com/api/
    '''

    global __url__

    action = '/search'
    browser = RoboBrowser(parser='html.parser')
    browser.open(__url__)

    form = browser.get_form(action=action)
    form['q'].value = text
    browser.submit_form(form)

    time.sleep(random.randint(10,25))

    # Need to ensure that the page has loaded.
    a = browser.parsed
    all_sentiments = browser.select('#top_keywords table:nth-of-type(1)')[0]
    all_sentiments = all_sentiments.select('tr')
    sentiment_values = 0
    count = 0
    for sentiment in all_sentiments:
        sentiment_fields = sentiment.select('td')
        sentiment_type   = sentiment_fields[0].string
        sentiment_value  = int(sentiment_fields[2].string)
        count += sentiment_value
        if sentiment_type == 'negative':
            sentiment_value = -sentiment_value
        if sentiment_type != 'neutral':
            sentiment_values += sentiment_value
    if count == 0:
        raise(Exception('No sentiment values were found.'))
    sentiment_value = sentiment_values / count
    sentences_sentiment = [(text, sentiment_value)]
    return sentences_sentiment
