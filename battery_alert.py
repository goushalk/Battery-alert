#!/usr/bin/env python3
import psutil
import tkinter
from tkinter import messagebox
import time

CHECK_INTERVAL = 300  # 5 minutes

window = tkinter.Tk()
window.withdraw()  

battery_notif_shown = False

def check_battery():
    global battery_notif_shown

    battery = psutil.sensors_battery()
    if battery:
        battery_percent = int(battery.percent)
        is_plugged = battery.power_plugged

        if battery_percent > 80 and not battery_notif_shown:
            battery_notif_shown = True
            messagebox.showinfo("Warning", f"Charging Status: {is_plugged}, Battery is close to 100% ({battery_percent}%). Please unplug your charger.")
        elif battery_percent < 20 and not battery_notif_shown:
            battery_notif_shown = True
            messagebox.showinfo("Warning", f"Charging Status: {is_plugged}, Battery is about to die ({battery_percent}%). Please plug in your charger.") 
        elif battery_percent <= 80 and battery_notif_shown:
            battery_notif_shown = False
    else:
        messagebox.showinfo("Error", "Battery Not Found!")
    
    window.after(CHECK_INTERVAL, check_battery)

check_battery()

window.mainloop()
