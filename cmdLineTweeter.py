import tweepy
import sys
from keys import tateKey #keys

# TODO add image support
# Add Key and Token Access from seperate document to make the script more module



#tweepy boilerplate for Auth
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():

  # import keys from keyfile and store in the cfg var
  cfg = tateKey
  api = get_api(cfg)

  # check to see if there is text input
  if len(sys.argv) > 1:
    # add cmd line text to tweet var
    tweet = ' '.join(sys.argv[1:])
    # tweet = status, makes sense to me.. 
    status = api.update_status(status=tweet)

  else:
    print('Provide a string!')
  


if __name__ == "__main__":
  main()