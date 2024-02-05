import random
import smtplib
import datetime as dt

my_email = 'ian711451@gmail.com'
my_password = 'tyogxtwsatugyxdz'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='mahiaian@yahoo.com',
            msg=f'Subject: Monday Motivation\n\n {quote}'
            )