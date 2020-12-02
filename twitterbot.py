import tweepy
from time import sleep
from toTweet import toTweet
from random import randint
from config import key, secretKey, token, secretToken #Config file with the API keys/tokens that you get in twitter develop

#Function to conect to API
def oAuth():
    try:
        auth = tweepy.OAuthHandler(key,secretKey) #Keys that you get by twitter develop menu
        auth.set_access_token(token, secretToken) #Tokens that you get by twitter develop menu
        return auth
    except:
        print('Erro ao estabelecer comunicação com a API')
        return None

#Completando o acesso/conexão a API
auth = oAuth()
api = tweepy.API(auth)

#Variaveis de uso
i = 0
lastNumber = len(toTweet) + 2 #Variavel que impedira 2 tweets iguais seguidos
limit = len(toTweet)

#Funcionamento dos tweets
while i < 5:
    #Gerar index na list toTweet
    number = randint(0, limit) #a <= N <= b
    while number == lastNumber:
        number = randint(0,len(toTweet))
        print("Indexs iguais... gerando outro index")
    if number > limit:
        print('Numero Maior')
        
    #Tweetar
    print(f'Tweet = {toTweet[number]}')
    confirm = input('Envie P para postar ou C para cancelar: ')
    if confirm == 'p':
        try:
            api.update_status(toTweet[number])
            print(f'Tweetado: {toTweet[number]}')
        except tweepy.TweepError as e:
            print(e.reason)
    else:
        print('Tweet não postado')
    
    #Variavel não gerar tweets seguidos iguais
    lastNumber = number

    #Intervalo para cada tweet
    if confirm == 'c':
        sleep(5)
    else:
        sleep(3600)
    i = i + 1
