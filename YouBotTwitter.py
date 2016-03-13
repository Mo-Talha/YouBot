import tweepy
from textwrap import TextWrapper
import lyricize


class YouBotStreamListener(tweepy.StreamListener):

    searchParameters = []

    totalText = ""

    numberOfTweets = 0

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
                self.numberOfTweets += 1
                if self.numberOfTweets >= 15:
                    self.numberOfTweets = 0
                    self.print_parsed()

        except:
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True

    def on_timeout(self):
        print('Application has timed out.')

    def main(self, name):

        consumer_key = "lPLCslO8xPQXstH0r0BD4BFNA"
        consumer_secret = "74FUgxGLFSN0goq2lxNqoEeWX4TzXTU7R1vpPmVHfRLd6NLwVK"
        access_token = "709039187069165568-rEDLr7ezG3hrHI1Qzi53LZOjt2yjULg"
        access_token_secret = "Pux8Y8rHCXYXobavYdNvmIBpQjBPzfZZ1xC4cdHat2jJz"

        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.auth = auth
        self.name = name

        '''timeline = tweepy.API(self.auth).user_timeline(count=300)

        print("Found: %d" % (len(timeline)))
        print("Removing...")

        # Delete tweets one by one
        for t in timeline:
            tweepy.API(self.auth).destroy_status(t.id)
        '''

        stream = tweepy.Stream(auth, self, timeout=None)
        stream.filter(track=self.searchParameters)

    def print_parsed(self):
        api = tweepy.API(self.auth)
        api.update_status(lyricize.main(self.totalText) + self.name)


