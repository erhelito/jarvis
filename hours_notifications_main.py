#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from os import system, path
from time import sleep
from hours_notifications import modules

path = path.abspath("")

while True:
    time = modules.get_time()[0]
    hours = modules.get_time()[1]
    minutes = modules.get_time()[2]
    seconds = modules.get_time()[3]

    modules.clock(hours, minutes, seconds)

    if minutes in {0, 15, 30, 45}:
        command = modules.command_function(path, hours, minutes)[0]
        system(command)

        if minutes == 0:
            hours_alert_command = modules.command_function(path, hours, minutes)[1]

            if hours > 12:
                hours -= 12

            for i in range(hours):
                system(f"{hours_alert_command}")

        sleep(60)