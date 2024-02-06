##################### Normal Starting Project ######################
import random
import smtplib
from datetime import datetime

import pandas

my_email = 'test@gmail.com'
my_password = ''

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
today = datetime.now()
today_tuple = (today.month, today.day)


# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv('birthdays.csv')

# Dictionary comprehension template for pandas DataFrame looks like this:
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f'Subject: Happy Birthday!!\n\n {contents}'

        )

