import tweepy


def post(config, message):
    auth = tweepy.OAuthHandler(config['api']['key'], config['api']['secret'])
    auth.set_access_token(config['token']['key'], config['token']['secret'])

    api = tweepy.API(auth)
    retval = api.update_status(status=message)

    if not retval:
        raise RuntimeError("Could not send message to Twitter")
