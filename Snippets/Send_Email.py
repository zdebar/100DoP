#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# Sending emails - needs to generate special password - manage account / security etc


# my_email = "zdebarthX@gmail.com"
# new_password = "password"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # TLS - transport layer security, start encryption
#     connection.login(user=my_email, password=new_password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs=my_email, 
#         msg="Subject:Hello\nz\nThis the body of the email."
#         )




# Date time module

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1982, month=1, day=21, hour=11, minute=45)
# print(date_of_birth)

