import tweepy
import time 
import schedule

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('x','x')
auth.set_access_token('x','x')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

    
search = ('#ForaWeintraub')
numeroDeTweets = 5

def pesquisar():

    for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
        try:
            print('tweet retuitado e favoritado')
            tweet.retweet()
            tweet.favorite()
            #time.sleep(10)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

schedule.every(15).seconds.do(pesquisar)

while True:
    schedule.run_pending()
    time.sleep(1)