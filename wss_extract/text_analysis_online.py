'''
Module contains the following class:

1. :py:class:`TextAnalysisOnline`
'''
import re

from sentiment_api import SentimentAPI


class TextAnalysisOnline(SentimentAPI):
    '''
    Concrete class of the abstract class :py:class:`SentimentAPI`.

    Respect the API Rate limit of 1000 calls per day see \
    `here <http://text-processing.com/docs/index.html>`_ for details

    Attributes:

    1. url -- url address of the Text Analysis Online sentiment api demo \
    `form <http://textanalysisonline.com/pattern-sentiment-analysis>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.

    Functions:

    1. _process_sentiment_page -- Fills out and submits the form at the url \
    address and process the returning value to return a sentiment value.
    '''

    @property
    def url(self):
        return 'http://textanalysisonline.com/pattern-sentiment-analysis'

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
        form = browser.get_forms()[0]
        form['text'].value = text
        browser.submit_form(form)

        all_text = browser.select('html')[0]
        sentiment_value = re.findall('<h4>Analysis Result[\w\W]*?(?=</p>)',
                                     str(all_text))[0]
        sentiment_value = re.findall('Polarity = [\d\.-]*',
                                     str(sentiment_value))[0]
        sentiment_value = float(re.findall('[\d\.-]+',
                                str(sentiment_value))[0])
        return sentiment_value
