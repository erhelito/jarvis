#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from os import system, path
from time import asctime, clock, sleep

path = path.abspath("")
print(path)

def clock(hours, minutes, seconds) :
    print("{0} h {1} min {2} s".format(hours, minutes, seconds))
    sleep(1)
    system("clear")

while True :
    raw_time = asctime()
    time = raw_time[11:-5]
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:8])

    clock(hours, minutes, seconds)
    
    minutes = 0

    title_command = "\"Time:\""
    logo_command = f"--icon=\"{path}/hours_notifications/clock.png\""
    hours_command = f"\"It's {hours} h {minutes} min.\""
    alarm_command = f"play \"{path}/hours_notifications/bell.wav\""
    hours_alert_command = f"play \"{path}/hours_notifications/metronome.wav\""
    command = f"notify-send {logo_command} {title_command} {hours_command} & {alarm_command}"

    if minutes == 0 or minutes == 15 or minutes == 30 or minutes == 45 :
        system(command)

        if minutes == 0 :

            if hours > 12:
                hours -= 12
            
            for x in range(hours) :
                system(f"{hours_alert_command}")

        sleep(60)