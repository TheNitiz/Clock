from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM\n")
alarm_hour=int(alarm_time[0:2])
alarm_minute=int(alarm_time[3:5])
print("Alarm Set...")
now = datetime.now()
time_hour = now.hour+alarm_hour
time_min = now.minute+alarm_minute
if time_min > 60:
    time_hour += time_min//60
    time_min = time_min%60
if time_hour > 23:
    time_hour = time_hour//24    
while True and len(alarm_time) == 5:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    if(time_hour==hour):
        if(time_min==minute):
            print("Wake Up!")
            playsound("C:/Users/DELL/VScode/PythonProjects/Clock/Ringtone.mp3")
            break