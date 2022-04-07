from multiprocessing import Pool
from urllib.error import URLError

import pytest

import wss_extract


def get_sentiment(sentiment_api):
    test_text = 'It was a good film'
    sentiment_api = getattr(wss_extract, sentiment_api)
    return sentiment_api().sentiment(test_text)


def test_apis():
    '''
    Test the APIs sentiment method. Tests:
    1. Test that the known working APIs return the correct sentiment \
    value for a given sentence.
    2. Test that for a system that is known not to work that it \
    raises an error.
    '''
    working_classes = ['SentiStrength', 'TextAnalysisOnline', 'TextProcessing']
    correct_sentiments = [1, 0.7, 'pos']
    pred_sentiments = []
    with Pool(2) as pool:
        pred_sentiments = pool.map(get_sentiment, working_classes)
    for index, correct_sentiment in enumerate(correct_sentiments):
        pred_sentiment = pred_sentiments[index]
        assert correct_sentiment == pred_sentiment

    not_working_classes = ['ChrisPotts']
    not_working_init_attrs = [('wordnet',)]
    for index, not_working in enumerate(not_working_classes):
        not_working_init_attr = not_working_init_attrs[index]
        not_working_api = getattr(wss_extract, not_working)
        not_working_api = not_working_api(*not_working_init_attr)
        with pytest.raises(URLError):
            not_working_api.sentiment('It was a good film')
    
    with pytest.raises(URLError):
        get_sentiment('Repustate')


def test_robot_error():
    '''
    Test that the :py:func:`wss_extract.sentiment_api.allowed` works
    correctly under the following tests:
    1. robots.txt file that allows web scrapers
    2. robots.txt file that does not allow web scrapers
    '''

    working_api = wss_extract.SentiStrength()
    assert working_api.allowed

    assert not BadRobotsAPI().allowed


class BadRobotsAPI(wss_extract.SentimentAPI):

    @property
    def url(self):
        return 'https://en.wikipedia.org/api/'

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
        return 1
