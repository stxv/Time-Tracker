import pygetwindow as pgw
import time
#Splits the title and puts each element into list by splitting at  " - " and gets the last element. (Normally looks like: timer.py - Time-Tracker - Visual Studio Code)
def split_window_title(title):
    title_parts = title.split(' - ')
    return title_parts[-1]
#Function that gets active window, splits it, and returns it 
def user_active_window():
    last_window = None
    while True:
        window = pgw.getActiveWindow()
        title = window.title
        active_window = split_window_title(title)
#last_window starts as none, then active window is compared to last window (active window(anything) is definitely not equal to None)), print active then replace last window.
        if active_window != last_window:
            print(active_window)
            last_window = active_window
        time.sleep(1)
        
user_active_window()
