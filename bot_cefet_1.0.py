import tweepy
import time 

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('x','x')
auth.set_access_token('x','x')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

    
search = ('cefet')
numeroDeTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet retuitado e favoritado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break