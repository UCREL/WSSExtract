'''
Module contains the following class:

1. :py:class:`SentimentAPI`
'''
from abc import ABC, abstractmethod
import time
from typing import Tuple, Any, Union, Dict
import random

from robobrowser import RoboBrowser
from reppy.cache import AgentCache
from reppy.cache.policy import ReraiseExceptionPolicy
from reppy.exceptions import BadStatusCode

from errors import RobotsError


class SentimentAPI(ABC):
    '''
    Abstract class for scraping values from online sentiment analysis tools

    Attributes:

    1. url -- url address of the Text Processing sentiment api demo \
    `form <http://text-processing.com/demo/sentiment/>`_
    2. timeout -- the number of seconds to randomly wait until the next \
    request to the server.
    3. allowed -- States if it can access the webpage containing the \
    sentiment tool by using the robots.txt file.

    Functions:

    1. sentiment -- Finds the sentiment of a text by using the sentiment \
    system at the given url address.
    2. _process_sentiment_page -- Given the main web page found at the URL \
    this method puts the text through the online system and returns the raw \
    value. This raw value is then processed by the :py:func`sentiment` method \
    to be returned.
    '''

    def sentiment(self, text: str,
                  sentiment_mapper: Union[None, Dict] = None) -> Any:
        '''
        :param text: The text to input into the sentiment system/ web form
        :param sentiment_mapper: Optional default None. If not None it is \
        a dict that maps the sentiment values that come from the system into \
        a different value e.g. if the system output 1 and -1 a mapper could \
        be {1: 'pos', -1: 'neg'}
        :returns: A the value the system outputs or the values of the mapper \
        if the sentiment_mapper is given
        '''
        if not self.allowed:
            raise RobotsError(self.url)

        browser = RoboBrowser(parser='html.parser')
        browser.open(self.url)

        time.sleep(random.randint(*self.timeout))
        value = self._process_sentiment_page(browser=browser, text=text)
        if sentiment_mapper is not None:
            return sentiment_mapper[value]
        else:
            return value

    @abstractmethod
    def _process_sentiment_page(self, browser, text) -> Any:
        pass

    @property
    def allowed(self) -> bool:
        '''
        :return: States whether or not web scraper are allowed on the systems \
        web page. This is done by checking the robots.txt file.
        '''
        cache = AgentCache('*', capacity=100,
                           cache_policy=ReraiseExceptionPolicy(ttl=0))
        is_allowed = True
        try:
            is_allowed = cache.allowed(self.url)
        except BadStatusCode as bad_http_code:
            # Means that the page does not exist due to internal server error
            if bad_http_code.args[1] == 500:
                is_allowed = True
            else:
                is_allowed = False
        return is_allowed

    @property
    @abstractmethod
    def url(self) -> str:
        '''
        :return: URL address of the sentiment system
        '''
        pass

    @property
    @abstractmethod
    def timeout(self) -> Tuple[int, int]:
        '''
        :return: A tuple containing integers that represent a random amount \
        of time to wait before sending another requests to the given online \
        system
        '''
        pass
