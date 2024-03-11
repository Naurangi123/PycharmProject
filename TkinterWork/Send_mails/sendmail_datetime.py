import datetime as dt
import random

now=dt.datetime.now()
year=now.year
day=now.day
day_of_week=now.weekday()
print(now,year,day,int(day_of_week))

date_of_birth=dt.datetime(year=2002,month=7,day=15,hour=7,minute=45,second=34)
print(date_of_birth)



now=dt.datetime.now()
weekday=now.weekday()
if weekday==1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()
    print(quote)
else:
    print("It's not Monday, so no quote for today.")