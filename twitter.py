import tweepy


def post(config, message):
    auth = tweepy.OAuthHandler(config['api']['key'], config['api']['secret'])
    auth.set_access_token(config['token']['key'], config['token']['secret'])

    api = tweepy.API(auth)
    api.update_status(message)
