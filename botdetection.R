#library(devtools)
#install_github("marsha5813/botcheck")

library(botcheck)
library(httr)
library(xml2) 
library(RJSONIO)

## botometer key
Mashape_key = "API_KEY"

## twitter information
consumer_key = "API_KEY"
consumer_secret = "SECRET"
access_token = "TOKEN"
access_secret = "SECRET"

twitter_bot_app = oauth_app("twitter_bot_app", key=consumer_key, secret=consumer_secret)
sig = sign_oauth1.0(twitter_bot_app, token=access_token, token_secret=access_secret)

data = read.csv("/Users/Ajay/Downloads/test.csv")
data2 = data[index:nrow(data),]
threshold = 0.7 # our level of acceptance/rejection for the bot


print(index)
for (account in data2$user){
  if (account %in% confirmed_bots || account %in% confirmed_not_bots){
    if (account %in% confirmed_bots){
      confirmed_bot_indexes = append(confirmed_bot_indexes, index)
    }
  }
  else{
    btc = botcheck(account)
    if (!is.null(btc) && btc > threshold){
      confirmed_bots = append(confirmed_bots, account)
      confirmed_bot_indexes = append(confirmed_bot_indexes, index)
      print(account)
    }
    else{
      confirmed_not_bots = append(confirmed_not_bots, account)
    }
  }
  index = index + 1
}
