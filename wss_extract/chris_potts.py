'''
Module contains the following class:

1. :py:class:`ChrisPotts`
'''
from typing import Dict, Any, Union
import re

from wss_extract.sentiment_api import SentimentAPI


class ChrisPotts(SentimentAPI):
    '''
    Concrete class of the abstract class :py:class:`SentimentAPI`.

    Attributes:

    1. url -- url address of many lexicon based \
    `systems <http://sentiment.christopherpotts.net/lexicon>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.
    3. senti_clf -- the lexicon classifier to be used from the 5 systems \
    found at this \
    `URL address <http://sentiment.christopherpotts.net/lexicon\
    /textscores_results/>`_

    Functions:

    1. _process_sentiment_page -- Fills out and submits the form at the url \
    address and process the returning value to return a sentiment value.
    '''

    def __init__(self, senti_clf):
        '''
        :param senti_clf: One of the following Strings that represents a \
        different sentiment classifier/system: 1. 'wordnet', \
        2. 'sentiwordnet' 3. 'opinionlexicon', 4. 'mpqa', 5. 'imdb'
        '''
        senti_clfs = ['wordnet', 'sentiwordnet',
                      'opinionlexicon', 'mpqa', 'imdb']
        if senti_clf not in senti_clfs:
            raise ValueError('senti_clf has to be one of the following Strings'
                             f' {senti_clfs}\nnot {senti_clf}')
        self.senti_clf = senti_clf

    @property
    def url(self):
        return 'http://sentiment.christopherpotts.net/'\
               'lexicon/textscores_results/'

    @property
    def timeout(self):
        return (10, 25)

    def sentiment(self, text: str,
                  sentiment_mapper: Union[None, Dict] = None) -> Any:
        '''
        :param text: The text to input into the sentiment system/ web form. \
        Can not be any longer than 140 characters.
        :param sentiment_mapper: Optional default None. If not None it is \
        a dict that maps the sentiment values that come from the system into \
        a different value e.g. if the system output 1 and -1 a mapper could \
        be {1: 'pos', -1: 'neg'}
        :returns: A the value the system outputs or the values of the mapper \
        if the sentiment_mapper is given
        '''
        text_length = len(text)
        assert_msg = 'The text has to contain less than '\
                     f'140 chars contains {text_length}'
        assert text_length < 140, assert_msg
        return super().__init__(text, sentiment_mapper)

    def _process_sentiment_page(self, browser, text) -> float:
        '''
        :param browser: A :py:class:`robobrowser.browser.RoboBrowser` \
        instance which is at the webpage that has the form to access the \
        sentiment system
        :param text: The text to input into the sentiment system/ web form
        '''

        action = '/lexicon/textscores_results/'
        form = browser.get_form(action=action)
        form['text'].value = text
        browser.submit_form(form)

        div_area = browser.select('#'+str(self.senti_clf))
        assert len(div_area) == 1, 'has to be only one div area per clf'
        div_area = str(div_area[0])
        data_rows = re.findall('data.addRow.*(?=]\);)', div_area)
        overall_score = float(0)
        for row in data_rows:
            row = re.findall('\[[^\]]*', row)[0]
            row = re.findall('"[^"]*', row)
            if len(row) != 2:
                import code
                code.interact(local=locals())
            row_assert_msg = 'Row has to be of length two to remove the word'
            assert len(row) == 2, row_assert_msg
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

            assert pos >= 0, f'Positive is not a positive value {pos}'
            assert neg <= 0, f'Negative is not a negative value {neg}'

            overall_score += pos
            overall_score += neg
        return overall_score
