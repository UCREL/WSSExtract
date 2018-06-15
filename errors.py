from reppy.robots import Robots


class RobotsError(Exception):
    '''
    Exception raised when the client is not allowed to connect to the URL \
    web page due to robots.txt

    Attributes:

    1. message -- States the URL address the client is connecting to and \
    the robots.txt url address that is disallowing the clients connection.
    '''

    def __init__(self, url: str) -> None:
        '''
        :param url: URL of the webpage the client is trying to connect to.
        '''

        robots_url = Robots.robots_url(url)
        message = f'Cannot connect to {url} due to the robots.txt file at '\
                  f'{robots_url}'
        self.message = message
