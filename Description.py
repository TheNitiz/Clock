from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
print("Alarm Set...")
now = datetime.now()
current_hour = now.strftime("%I")
current_minute = now.strftime("%M")
time_hour = int(current_hour)+int(alarm_hour)
time_min = int(current_minute)+int(alarm_minute)
if time_min > 60:
    time_hour += time_min//60
    time_min = time_min%60
print(time_hour)
print(time_min)
while True and len(alarm_time)==5:
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    print(current_minute == time_min)
    if(time_hour==current_hour):
        if(time_min==current_minute):
            print("Wake Up!")
            playsound("C:/Users/DELL/VScode/PythonProjects/Ringtone.mp3")
            break
else:
    print("Please Enter Valid Time Format")