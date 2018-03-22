import random
import re
import time
import code

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://test.umigon.com/'''

__url__ = 'http://test.umigon.com/'

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

    form = False
    form_id = 'j_idt16'
    for a_form in browser.get_forms():
        if form_id in a_form.fields:
            form = a_form
            break
    if not form:
        raise(Exception('Cannot find the correct form to submit to'))

    form['j_idt16:textArea'].value = text
    browser.submit_form(form)

    code.interact(local=locals())

    # Regular expression reference:
    # http://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
    all_text = str(browser.select('html'))
    sentiment_text = re.findall('<h4>Sentiment Result[\w\W]*?(?=</p>)', all_text)[0]
    sentiment_text = re.findall('sentiment:[\w\W]*?(?=<br>)', sentiment_text)[0]
    sentiment_value = re.findall('\s\w+', sentiment_text)[0].strip()
    return [(text, sentiment_value)]
