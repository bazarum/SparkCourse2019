from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = 'w8TL68073oA9fBB8uY4jmXQ1C'
consumer_secret = 'mWkBQcUKu9MFUAGSVOUjAv6EIKHmEwOLoohVYXdTEoq8glcKO1'
access_token = '870541-Xxzh1Oke7Y4VqWxU6mqjO441TPTJ0xwmE3IjAYjXsLJ'
access_token_secret = 'INTa3rPviJQ0AhAhK4vEceuTo2OkBxAK00f9J7YrWYEd7'

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):


        print(str(json.loads(data)['text'])) #.encode('UTF-8'))
        print(str(json.loads(data)['text'])) #.encode('UTF-8'))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['trump'])
