import datetime as dt

n=dt.datetime.now() # time now
print(n)

date1=dt.datetime(
    year=2020, month=2, day=14,
    hour=13, minute=30
)
print(date1)

day=dt.timedelta(days=25)
date2=date1+day
print(date2)

date2=dt.datetime(
    year=2020, month=2, day=20,
    hour=16 
)

day21=date2-date1 # เวลาห่าง?
print(day21)

print(date1.strftime('%A %d, %B %Y')) # ให้แสดง date ตามที่กำหนด