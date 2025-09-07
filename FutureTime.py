#FutureTime.py
#Name: Connor Pell
#Date: 9/7/2025
#Assignment: lab2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print(f"{currentHour}:{currentMinute}")

  #TODO:
  #Ask user for hours
  usr_hours = int(input("Enter the number of hours to add:  "))

  #Ask user for minutes
  usr_minutes = int(input("Enter the number of minutes to add:  "))
                    
  #Calculate the time after the user-supplied time has passed.
  total_minutes = currentMinute + usr_minutes
  over_hours = total_minutes // 60
  add_minutes = total_minutes % 60

  total_hours = currentHour + usr_hours + over_hours
  add_hours = total_hours % 24

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"{add_hours}:{add_minutes}")

if __name__ == '__main__':
  main()
