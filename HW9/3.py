from datetime import datetime
import jdatetime

def differece_to_seconds(date1, date2):
    
        time_difference = abs((date2 - date1).total_seconds())
        return f"\nTime difference in seconds is: {int(time_difference)}"
        
def leap_years(date1, date2):
    leap_years = 0
    for year in range(date1.year, date2.year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return f"\nThere was {leap_years} leap years between these two dates!"


def adjust_time(date1, date2):
    time_forward = date2.year-date1.year-1
    time_backward = date2.year-date1.year-1

    if not (date1.month > 3 and date1.day > 21 and date1.hour > 0 and date1.minute > 0) :
        time_forward += 1
    
    if not (date1.month < 9 and date1.day < 22 and date1.hour > 0 and date1.minute > 0) :
        time_backward += 1
        
    return f"\nBakward: {time_backward}\tForward: {time_forward}"

def convert_to_jalali(date1, date2):
    jalali_date1 = jdatetime.date.fromgregorian(date=date1)
    jalali_date2 = jdatetime.date.fromgregorian(date=date2)
    return f"\nDates to jalali:\ndate1: {jalali_date1.strftime('%Y/%m/%d')}\ndate2: {jalali_date2.strftime('%Y/%m/%d')}\n"
    

date1 = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date and time (YYYY-MM-DD HH:MM:SS): ")

try:
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    print(differece_to_seconds(date1, date2))
    print(leap_years(date1, date2))
    print(adjust_time(date1, date2))
    print(convert_to_jalali(date1, date2))
    
except ValueError:
    print("Enter the date and time in the correct format.")
    
