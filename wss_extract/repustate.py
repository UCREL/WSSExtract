'''
Module contains the following class:

1. :py:class:`Repustate`
'''
import re

from wss_extract.sentiment_api import SentimentAPI


class Repustate(SentimentAPI):
    '''
    Concrete class of the abstract class :py:class:`SentimentAPI`.

    Attributes:

    1. url -- url address of the Repustate sentiment api demo \
    `form <https://www.repustate.com/sentiment-analysis-demo/>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.

    Functions:

    1. _process_sentiment_page -- Fills out and submits the form at the url \
    address and process the returning value to return a sentiment value.
    '''

    @property
    def url(self):
        return 'https://www.repustate.com/sentiment-analysis-demo/'

    @property
    def timeout(self):
        return (10, 25)

    def _process_sentiment_page(self, browser, text) -> float:
        '''
        :param browser: A :py:class:`robobrowser.browser.RoboBrowser` \
        instance which is at the webpage that has the form to access the \
        sentiment system
        :param text: The text to input into the sentiment system/ web form
        :returns: A real valued sentiment score between -1 and 1
        '''
        form = browser.get_form(class_='form')
        form['text'].value = text
        form['language'].value = 'en'
        browser.session.headers['Referer'] = self.url
        browser.submit_form(form)

        sentiment_table = browser.select('form')[0].select('table')[0]
        sentiment_value = re.findall('[\d.]+<', str(sentiment_table))[0]
        sentiment_value = float(sentiment_value.rstrip('<'))
        return sentiment_value
