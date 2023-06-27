import tkinter as tk
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry.get()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            play_alarm_sound()
            break

        time.sleep(1)

def play_alarm_sound():
    frequency = 2500  # Set the frequency (in Hz)
    duration = 1000  # Set the duration (in milliseconds)
    winsound.Beep(frequency, duration)

# Create the main application window
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("300x200")

# Create a label and entry field for setting the alarm time
label = tk.Label(window, text="Set Alarm Time (HH:MM:SS):", font=("Arial", 12))
label.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 12))
entry.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm, font=("Arial", 12), width=10)
button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
