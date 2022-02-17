""" Python Date time """
from datetime import datetime ,date,time
# 1 Current day, month, year, hour, minute and timestamp

now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)

# 2 current date using format: "%m/%d/%Y, %H:%M:%S"
now = datetime.now()
print(now.strftime("%m/%d/%y, %H:%M:%S"))

#3 Change this 5 December 2019 string to time
date_str = " 5 December, 2019"
print("date_str =",date_str)
print(datetime.strptime(date_str, '%d %B, %Y'))


#4 calculating difference between now and new year.
today = date(year=2022, month=2, day =17)
new_year = date(year = 2023, month=1, day=1)
print(new_year - today, 'time left for new year')

# 5 calculate the time difference between 1 January 1970 and now
today = date(year=2022, month=2, day =17)
the_past = date(year = 1970, month=1, day= 1)
print(new_year - the_past, 'time betweeen now and 1970')

#6 Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# 🎉 CONGRATULATIONS ! 🎉