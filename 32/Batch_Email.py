import smtplib
import datetime as dt

# my_email = "test_email@gmail.com"

# #Needed to generate special password by gmail
# password = "abc12345"

# #Encrypting connection


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="destination email", 
#         msg="Subject: Hello\n\nThis is the body of my mail"
#     )
#     connection.close()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(day_of_week)

day_of_birth = dt.datetime(year = 1995, month = 12, day = 12, hour=8)
print(day_of_birth)