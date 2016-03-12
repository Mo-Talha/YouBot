from textwrap import TextWrapper
from YouBot import searchParameters

import tweepy


class YouBotStreamListener(tweepy.StreamListener):

    #Gives status of tweets
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print(self.status_wrapper.fill(status.text))
            print('%s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source))
        except:
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        #Keep stream alive
        return True

    def on_timeout(self):
        print('Application has timed out.')


def main():

    consumer_key = "oLT41c1FVjGXrCuVEXrDtZ3vd"
    consumer_secret = "ftY2n8uhzLC7eX2IdsCi9WwSKDoiqL7LPy00S33g8YTVXTZKG8"
    access_token = "708674786805813248-j6INo0dAJthGhIBs9eCFZw1DCCxY8vb"
    access_token_secret = "tmGwqGyvKCdoZfCjgTOyuVEORyygdiD7aoJIcjpJNsKq1"

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, YouBotStreamListener(), timeout=None)

    stream.filter(track=searchParameters)

    # Prompt for mode of streaming
    '''valid_modes = ['sample', 'filter']
    while True:
        mode = input('Mode? [sample/filter] ')
        if mode in valid_modes:
            break
        print('Invalid mode! Try again.')

    if mode == 'sample':
        stream.sample()

    elif mode == 'filter':
        follow_list = input('Users to follow (comma separated): ').strip()
        track_list = input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
            userid_list = []
            username_list = []

            for user in follow_list:
                if user.isdigit():
                    userid_list.append(user)
                else:
                    username_list.append(user)

            for username in username_list:
                user = tweepy.API().get_user(username)
                userid_list.append(user.id)

            follow_list = userid_list
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None
        print(follow_list)
        stream.filter(follow_list, track_list)'''


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
