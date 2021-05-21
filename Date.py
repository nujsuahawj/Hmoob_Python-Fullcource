import datetime as dt
date1=dt.datetime(year=2020,month=2,day=14)
print(date1.strftime('%A %d %B %Y'))
days=dt.timedelta(days=25)
date2=date1+days
#print(date2)
date3=dt.datetime(year=2020,month=2,day=28)
days1= date1-date2
#print(days1)