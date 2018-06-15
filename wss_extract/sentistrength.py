'''
Module contains the following class:

1. :py:class:`SentiStrength`
'''
import re

from sentiment_api import SentimentAPI


class SentiStrength(SentimentAPI):
    '''
    Concrete class of the abstract class :py:class:`SentimentAPI`.

    Attributes:

    1. url -- url address of the SentiStrength sentiment api demo \
    `form <http://sentistrength.wlv.ac.uk/>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.

    Functions:

    1. _process_sentiment_page -- Fills out and submits the form at the url \
    address and process the returning value to return a sentiment value.
    '''

    @property
    def url(self):
        return 'http://sentistrength.wlv.ac.uk/'

    @property
    def timeout(self):
        return (10, 25)

    def _process_sentiment_page(self, browser, text) -> int:
        '''
        :param browser: A :py:class:`robobrowser.browser.RoboBrowser` \
        instance which is at the webpage that has the form to access the \
        sentiment system
        :param text: The text to input into the sentiment system/ web form
        :returns: A the binary sentiment value either -1 or 1.
        '''
        form = browser.get_forms()[0]
        if form['submit'].value != "Detect Sentiment":
            raise(Exception('Cannot find the correct form to submit to'))
        form['result'].value = 'binary'
        form['text'].value = text
        browser.submit_form(form)

        # Regular expression reference:
        # http://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
        all_text = str(browser.select('html'))
        sentiment_text = re.findall('has binary result[\w\W]*?(?=</b>)',
                                    all_text)[0]
        sentiment_value = int(re.findall('[-\d]+', sentiment_text)[0].strip())
        return sentiment_value
