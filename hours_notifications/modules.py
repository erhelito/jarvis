#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

def get_time(asctime) :
    raw_time = asctime
    time = raw_time[11:-5]
    hours = int(time[0:2])
    minutes = int(time[3:5])
    seconds = int(time[6:8])

    return time, hours, minutes, seconds

def clock(hours, minutes, seconds, sleep, system) :
    print("{0} h {1} min {2} s".format(hours, minutes, seconds))
    sleep(1)
    system("clear")

def command_function(path, hours, minutes) :
    title_command = "\"Time:\""
    logo_command = f"--icon=\"{path}/hours_notifications/clock.png\""
    hours_command = f"\"It's {hours} h {minutes} min.\""
    alarm_command = f"play \"{path}/hours_notifications/bell.wav\""
    hours_alert_command = f"play \"{path}/hours_notifications/metronome.wav\""
    command = f"notify-send {logo_command} {title_command} {hours_command} & {alarm_command}"

    return command, hours_alert_command