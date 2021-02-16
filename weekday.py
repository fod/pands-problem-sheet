# weekday.py
# Informs the user whether or not today is a weekday
# Author: Fiachra O' Donoghue

# Import the datetime class from the datetime module
from datetime import datetime

#https://docs.python.org/3/library/datetime.html#datetime.date.today
#https://docs.python.org/3/library/datetime.html#datetime.date.weekday
today = datetime.today().weekday()

print("Today is {}".format(datetime.today().strftime('%A')))
if today in (5, 6):
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")


# https://stackoverflow.com/a/9847269
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes