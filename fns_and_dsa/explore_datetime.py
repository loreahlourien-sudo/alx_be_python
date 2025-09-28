import datetime

def display_current_datetime ():
 current_date = datetime.datetime.now()
print("Current date and time:",current_date)



number_of_days = int(input("Enter the number of days :"))
datetime.timedelta(days=number_of_days) 

def calculate_futuretime_date():
    future_date = display_current_datetime + number_of_days
print()
   
