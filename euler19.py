import calendar
x=0
c=calendar.Calendar()
for year in range(1901,2001):
	for month in range(1,13):
		x+=[0,0,0,0,0,0,1] in c.monthdayscalendar(year,month)
print x
