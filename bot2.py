import tweepy
import time 
import schedule

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('F0La2N13uvPaoBCd28bT2nPaf','p58IKsszHYjFGaF1huSqWvdCe4yQRs70RO3c6uJ5anC1k4tQan')
auth.set_access_token('1264450907917422593-z5vSkj8T2BPdYZWdAFZ9SQ6cc9ETnB','ofFDNAqhK2rJDfRyMRdQHCO9MZkDlALBx3hHioMGeNJuX')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search3 = ('cefet')
search = ('cefet')
search2 = ('​cefet')
search3 = ('cefet')
searchR = ('cefet')

numeroDeTweetsR = 0
numeroDeTweets = 500
numeroDeTweets2 = 5

def pesquisar():

    for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
        try:
            print('tweet retuitado e favoritado')
            tweet.retweet()
            tweet.favorite()
            time.sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def pesquisa2():
    
    for tweet in tweepy.Cursor(api.search, search2).items(numeroDeTweets2):
        try:
            print('tweet retuitado e favoritado')
            tweet.retweet()
            tweet.favorite()
            time.sleep(10)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def pesquisa3():
    
    for tweet in tweepy.Cursor(api.search, search3).items(numeroDeTweets2):
        try:
            print('tweet retuitado e favoritado')
            tweet.retweet()
            tweet.favorite()
            time.sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#def resposta():
#    for tweet in tweepy.Cursor(api.search, searchR).items(numeroDeTweetsR):
#        try:
#            print("nome do usuario: @" + tweet.user.screen_name)
#            api.update_status("@" + tweet.user.screen_name + " hmmm, ainda não sei ler mano.", in_reply_to_status_id=tweet.id)
#            print("tuite enviado corretamente")
#            time.sleep(30)
#        except tweepy.TweepError as e:
#            print(e.reason)
#        except StopIteration:
#            break

schedule.every(10).seconds.do(pesquisar)
schedule.every(60).seconds.do(pesquisa2)
schedule.every(3000).seconds.do(pesquisa3)
#schedule.every(60).seconds.do(resposta)
while True:
    schedule.run_pending()
    time.sleep(1)