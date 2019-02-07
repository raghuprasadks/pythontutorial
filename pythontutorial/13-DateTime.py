#DateTime
#https://www.w3schools.com/python/python_datetime.asp
from datetime import date
from datetime import time
from datetime import datetime
def main():
 	 ##DATETIME OBJECTS
     #Get today's date from datetime class
    today=datetime.now()
    print(today)
  # Get the current time
    t = datetime.time(today)
    print("The current time is", t)
 #weekday returns 0 (monday) through 6 (sunday)
    wd = date.weekday(today)
 #Days start at 0 for monday
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

if __name__== "__main__":
    main()

#Formatting Y - Year - four numbers

from datetime import datetime
def main():
    now = datetime.now()
    print(now.strftime("%Y"))

if __name__== "__main__":
    main()

#Formatting y - Year last two numbers

from datetime import datetime
def main():
    now = datetime.now()
    print("Formatting")
    #year in 4 digits 2018
    print(now.strftime("%Y"))
    #year in 2 digits 18
    print(now.strftime("%y"))
    #Day in full for example Friday
    print(now.strftime("%A"))
    #Day in short for example Fri
    print(now.strftime("%a"))
    #Month in Full for example May
    print(now.strftime("%B"))
    # Month in Full for example May
    print(now.strftime("%b"))
    # Day of the month for example 18
    print(now.strftime("%d"))

if __name__== "__main__":
    main()


#
#Example file for formatting time and date output
#
from datetime import datetime
def main():
   #Times and dates can be formatted using a set of predefined string
   #Control codes
      print("Local date time ")
      now= datetime.now() #get the current date and time
      #%c - local date and time, %x-local's date, %X- local's time
      print(now.strftime("%c"))
      print(now.strftime("%x"))
      print(now.strftime("%X"))
##### Time Formatting ####
      #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
      print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
      print(now.strftime("%H:%M")) # 24-Hour:Minute
if __name__== "__main__":
    main()


import datetime
today_date = datetime.date.today()
print(today_date)
new_today_date = today_date.strftime("%d/%m/%Y")
print(new_today_date)

#Future date
import datetime

x = datetime.datetime(2019, 11, 7)

print(x)