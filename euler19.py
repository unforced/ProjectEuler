import calendar
c=calendar.Calendar()
print len([1 for month in range(1,13) for year in range(1901,2001) if [0,0,0,0,0,0,1] in c.monthdayscalendar(year,month)])
