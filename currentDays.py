                            #! To Find The Current Day Number

from time import strptime 
from datetime import datetime
from calendar import isleap

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
result = strptime(time_now , "%Y-%m-%d %H:%M:%S")
print(f"Current Day Number:{result.tm_yday}")


                            #! How Many Days Remaining In This Year

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
result = strptime(time_now , "%Y-%m-%d %H:%M:%S")

if isleap(datetime.now().year):
    print(f"Remaining Days In This Year: {366 - result.tm_yday}")
else:
    print(f"Remaining Days In This Year: {365 - result.tm_yday}")
