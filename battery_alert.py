#!/usr/bin/env python3
import psutil
import tkinter
from tkinter import messagebox
import time

CHECK_INTERVAL = 60000  # 1 minute

window = tkinter.Tk()
window.withdraw()  

def check_battery():
    # Get battery status
    battery = psutil.sensors_battery()
    if battery:
        battery_percent = int(battery.percent)
        is_plugged = battery.power_plugged

        # Check for conditions and display warnings
        if battery_percent > 80:
            messagebox.showinfo("Warning", f"Charging Status:{is_plugged},Battery is close to 100% ({battery_percent}%). Please unplug your charger.")
        elif battery_percent < 20:
            messagebox.showinfo("Warning", f"Chargig Status:{is_plugged},Battery is About to die ({battery_percent}%).Please plug your in your charger.") 
        else:
            pass
    else:
        messagebox.showinfo("error","Battery Not Found!")
    # Scheduled check
    window.after(CHECK_INTERVAL, check_battery)

# Start the periodic battery checks
check_battery()

# Run the Tkinter event loop
window.mainloop()
