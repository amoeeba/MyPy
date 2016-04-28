import datetime
# Prior date example of "11 March 2016"
old_date = datetime.date(2016,3,11)
# New date example of "today"
new_date = datetime.date.today()
date_delta = new_date - old_date
# date_delta is a "datetime.timedelta" object
# "date_delta.days" gives an integer number of days
print("Days Between = %s" % date_delta.days)
print("Weeks Between = %s" % (date_delta.days/7.0))
# related example, add 30 days to date
print("30 days from %s is %s" % \
  ( new_date, new_date+datetime.timedelta(days=30) ))