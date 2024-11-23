import time

from win32com.client import Dispatch

print("Enter the time you want to set a reminder")

year = int(input("Enter the year (e.g., 2030): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))
second = int(input("Enter the second (0-59): "))

# Create a struct_time tuple with the given input
# weekday and yearday are set to 0; is_dst is set to -1 to let Python determine daylight saving
future_time = time.struct_time((year, month, day, hour, minute, second, 0, 0, -1))

#The alarm you want to hear
drink = "It's time to drink water."

#helps to convert alarm time to seconds from time module to retrieve the alarm time in seconds since the Unix epoch (January 1, 1970).
future_epoch = time.mktime(future_time)

#The code uses the time module to retrieve the current time in seconds since the Unix epoch (January 1, 1970)
current_epoch = time.time()

#Getting time string from seconds
current = time.ctime(current_epoch)

#calculating the time till code have to got in sleep
time_to_sleep = future_epoch - current_epoch

#getting time string of the alarm from seconds
future = time.ctime(future_epoch)

print(f"Alarm set from {current} to {future}")

#using a while loop to execute the alarm process
while(time.time() != future_epoch ):
    time.sleep(time_to_sleep)
    if time.time() != future_epoch:
        break

#creating a computer speaker for the alarm
speak = Dispatch("SAPI.Spvoice")
speak.Speak(drink)
print(drink)