import tweepy
import sys


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  api = get_api(cfg)

  if len(sys.argv) > 1:
    tweet = ' '.join(sys.argv[1:])
    status = api.update_status(status=tweet)

  else:
    print('Provide a string!')
  
  
  

  

  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()