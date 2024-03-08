import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)


    my_email = "test_email@gmail.com"

    #Needed to generate special password by gmail
    password = "abc12345"

    #Encrypting connection


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="destination email", 
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )



