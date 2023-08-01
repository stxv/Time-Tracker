import pygetwindow as pgw
import time
#Splits the title and puts each element into list by splitting at  " - " and gets the last element. (Normally looks like: timer.py - Time-Tracker - Visual Studio Code)
def split_window_title(title):
    title_parts = title.split(' - ')
    return title_parts[-1]
def google_title_split(title):
    title_parts = title.split(' - ')
    return title_parts
#Function that gets active window, splits it, and returns it 
def user_active_window():
    last_window = None
    last_google_tab = None
    while True:
        try:
            window = pgw.getActiveWindow()
            if window is not None:
                title = window.title
                active_window = split_window_title(title)
#
                if active_window == "Google Chrome":
                    if google_title_split(title) != last_google_tab:
                        print(google_title_split(title))
                        last_google_tab = google_title_split(title)
#last_window starts as none, then active window is compared to last window (active window(anything) is definitely not equal to None)), print active then replace last window.
                if active_window == "Task Switching":
                    continue
                if active_window != last_window:
                    print(active_window)
                    last_window = active_window

        except pgw.PyGetWindowException:
            pass
user_active_window()
# How the code is now, 