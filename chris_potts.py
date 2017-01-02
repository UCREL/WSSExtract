import random
import re
import time

from robobrowser import RoboBrowser

'''Finds the sentiment of sentences using the sentiment analysis tool found
 here: http://sentiment.christopherpotts.net/lexicon/textscores_results/

 which contains the following sentiment classifiers:
 1. wordnet
 2. sentiwordnet
 3. opinion lexicon
 4. mpqa
 5. imdb'''

__url__ = 'http://sentiment.christopherpotts.net/lexicon/textscores_results/'

def sentiment(text):
    '''Given a string of text will return a list contain a tuple with the
    following values:
    1. name of the sentiment classifier used to classify the text
    2. a list containing a tuple of:
      1. the text classified
      2. the sentiment value

    This system can only analyse text as one sentences does not split
    the text into sentences. Can only do up to 140 chars.'''

    assert len(text) < 140, 'The text has to contain less than 140 chars contains {}'.format(len(text))

    global __url__

    action = '/lexicon/textscores_results/'

    browser = RoboBrowser(parser='html.parser')
    browser.open(__url__)

    time.sleep(random.randint(10,25))

    form = browser.get_form(action=action)
    form['text'].value = text
    browser.submit_form(form)

    senti_clf = ['wordnet', 'sentiwordnet', 'opinionlexicon', 'mpqa', 'imdb']
    senti_clf_values = dict(list(zip(senti_clf, [0]*len(senti_clf) )))
    for clf in senti_clf:
        div_area = browser.select('#'+str(clf))
        assert len(div_area) == 1, 'has to be only one div area per clf'
        div_area = str(div_area[0])
        data_rows = re.findall('data.addRow\([^\)]*', div_area)
        overall_score = float(0)
        for row in data_rows:
            row = re.findall('\[[^\]]*', row)[0]
            row = re.findall('"[^"]*', row)
            assert len(row) == 2, 'Row has to be of length two to remove the word'
            row = row[1]
            row = row.replace('"', '')
            row = row.split(',')
            data_items = []
            for item in row:
                item = item.strip()
                if item == '':
                    continue
                elif item == 'null':
                    item = float(0)
                else:
                    item = float(item)
                data_items.append(item)
            pos = data_items[0]
            neg = data_items[1]
            neu = data_items[2]

            assert pos >= 0, 'Positive is not a positive value {}'.format(pos)
            assert neg <= 0, 'Negative is not a negative value {}'.format(neg)

            overall_score += pos
            overall_score += neg
        senti_clf_values[clf] = overall_score

    sentiment_values = []
    for clf, value in senti_clf_values.items():
        sentiment_values.append((clf, [(text, value)]))
    return sentiment_values
