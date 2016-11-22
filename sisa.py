import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the Selasdia Intelligent Sales
 Assistant sentiment analysis tool found here:
 http://www.aiaioo.com:8080/annotator-0.1/automation/demoView/1'''

__url__ = 'http://www.aiaioo.com:8080/annotator-0.1/automation/demoView/1'

def sentiment(text):
    '''Given a string of text will return a list of tuples each containing:
    1) String that reprsents a sentence from the text.
    2) The sentiment value of the associated sentence
    Note if one sentence given the length of the list will be 1.'''

    global __url__

    action = '/annotator-0.1/automation/demo'
    browser = RoboBrowser()
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form = browser.get_form(action=action)
    form['text'].value = text
    browser.submit_form(form)

    sentiment_values = []
    sentiments     = browser.select('font')
    sentiments_len = len(sentiments)
    # Finds the respective sentences
    sentences      = str(browser.select('b')[0])
    sentences      = re.findall('Sentence \d: [^=]*', sentences)
    sentences      = list(map(lambda sent: re.split('Sentence \d:', sent)[1].strip(),
                              sentences))
    # If their is more than one sentence then the first value is the document
    # sentiment therefore get rid of it.
    if len(sentiments) > 1:
        sentiments_len  =- 1
        sentiments_iter = iter(sentiments)
        _               = next(sentiments_iter)
        for sentiment in sentiments_iter:
            sentiment_values.append(sentiment.string)
    elif len(sentiments) == 1:
        sentiment_values.append(sentiments[0].string)

    sentence_sent_err = ('The number of sentiments do not match the number of '
                         'sentences')
    assert sentiments_len != len(sentiments), sentence_sent_err

    sentences_sentiment    = list(zip(sentences, sentiment_values))
    return sentences_sentiment
