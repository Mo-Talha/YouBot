import tweepy
from textwrap import TextWrapper
import lyricize


class YouBotStreamListener(tweepy.StreamListener):

    searchParameters = []

    totalText = ""

    _status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def __init__(self, search_parameters):
        super().__init__()
        self.searchParameters = search_parameters

    def on_status(self, status):
        try:
            text = self._status_wrapper.fill(status.text)
            if not status.retweeted and 'RT @' not in text and text[0] != "@":
                text = text.replace('@', '')
                print(text)
                self.totalText += text

        except:
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True

    def on_timeout(self):
        print('Application has timed out.')

    def main(self):

        consumer_key = "oLT41c1FVjGXrCuVEXrDtZ3vd"
        consumer_secret = "ftY2n8uhzLC7eX2IdsCi9WwSKDoiqL7LPy00S33g8YTVXTZKG8"
        access_token = "708674786805813248-j6INo0dAJthGhIBs9eCFZw1DCCxY8vb"
        access_token_secret = "tmGwqGyvKCdoZfCjgTOyuVEORyygdiD7aoJIcjpJNsKq1"

        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = tweepy.Stream(auth, self, timeout=None)
        stream.filter(track=self.searchParameters)

    def print_parsed(self):
        lyricize.main(self.totalText)
