import calendar

# python calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2020, 1, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
output = hc.formatmonth(2020, 1)
print(output)