import botometer, csv, tweepy

mashape_key = "4C7f3PJdnLmshITTJoq7wGE9bJoQp1LLwlzjsnBisPv4P720To"
twitter_app_auth = {
    'consumer_key': 'a6yzKfwnoZdClaN4iwSlV8pWs',
    'consumer_secret': 'tgQxc6GLhDGcpt32pyiOriixSvR4CpH4VubJyWvYpYlQpjL3oy',
    'access_token': '2766685437-Sb1rJKidcnoNaI1igr50Ob3xU4z9SKdq78vLwKG',
    'access_token_secret': 'RhwITCLXtO1eubcni0g6YZwuW6zYGRjngjYikM1morU8I',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)


index = 1597

trollbots = set()
notTrollbots = set()
with open('/Users/Ajay/Downloads/10.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['user'] in trollbots:
            with open('/Users/Ajay/Desktop/Apps/Bot Detection/10bots.csv', 'a') as botfile:
                out = [row['user'], index]
                writer = csv.writer(botfile)
                writer.writerow(out)
            botfile.close()
        elif row['user'] in notTrollbots:
            continue
        else:
            try:
                result = bom.check_account(row['user'])['scores']['english']
            except:
                continue
            if result >= 0.7:
                with open('/Users/Ajay/Desktop/Apps/Bot Detection/10bots.csv', 'a') as botfile:
                    out = [row['user'], index]
                    writer = csv.writer(botfile)
                    writer.writerow(out)
                botfile.close()
            
        print index
        index += 1
