import requests
import datetime
from function import send_email_news,mail_msg,get_top_news

# Todo -> Configuration of the date in the link
date_to_get = datetime.datetime.now().strftime("%Y-%m-%d")
key_api = "ecefb36de5b34f8c9cdc9df4396bebdb"
url_api = f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-12&sortBy=publishedAt&apiKey={key_api}"

top_news = get_top_news(key_api,"Gaza","bbc-news","en",)


# envoi de la demande de requet
#r = requests.get(url_api)

#Organisation des data
#data = r.json()

#
#articles = data['articles']
articles = top_news['articles']

# Access to the articles Data
data_to_send = ""
for article in articles[:5]:
    data_to_send += f"""
    {article['author']} -> {article['title']}
    {article['description']}
    {article['url']}
    ----------------------------------------
    """
msg = mail_msg('Today news',str(data_to_send))
send_email_news(msg)

