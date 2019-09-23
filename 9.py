import my_module as mm
import sys
import datetime
import calendar


courses = ['History', 'Math', 'Physics', 'CompSci']
print(mm.find_index(courses, 'Art'))
print(sys.path)
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))
