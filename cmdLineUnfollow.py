import tweepy
import sys
from keys import tateKey #keys

# boilerplate for authentication
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)



# import keys from keyfile and store in the cfg var
cfg = tateKey
api = get_api(cfg)

# assign command line arg as 'a'
# a is the USERNAME
a = ' '.join(sys.argv[1:])


# check if there is a user in command
if len(a) > 1:
	# follow the user
	api.destroy_friendship(a)
else:
    print('Provide a string!')