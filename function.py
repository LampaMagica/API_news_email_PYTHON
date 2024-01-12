import smtplib, ssl
from email.message import EmailMessage
from newsapi import NewsApiClient

def send_email_news(message,send_to='ajin.ekletu@gmail.com'):
    port = 465
    sender_email = "damu.ekletu@gmail.com"
    password = None
    with open('secret/code_secret.txt') as code:
        password = code.read()

    #What do you mean by create context
    context = ssl.create_default_context()

    #Send data
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)

        #server.sendmail(from_addr=sender_email,to_addrs=send_to,msg=message)
        server.send_message(message)

def mail_msg(subject, message, send_to='ajin.ekletu@gmail.com'):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "damu.ekletu@gmail.com"
    msg['To'] = send_to
    msg.set_content(message)
    return msg

def get_top_news(api,subject_query,sources_query,language_query):

    newsapi = NewsApiClient(api_key=api)

    top_headlines = newsapi.get_top_headlines(q=subject_query,
                                              sources=sources_query,
                                              language=language_query)

    return top_headlines