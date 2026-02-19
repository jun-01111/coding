import datetime

kst_now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
print(kst_now.strftime("%Y-%m-%d"))