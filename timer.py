import pygetwindow as pgw
import time
#Splits the title and puts each element into list by splitting at  " - " and gets the last element. (Normally looks like: timer.py - Time-Tracker - Visual Studio Code)
def split_window_title(title):
    title_parts = title.split(' - ')
    return title_parts[-1]
def google_title_split(title):
    title_parts = title.split(' - ')
    return title_parts[-2]
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
                if active_window == "Task Switching":
                    active_window == last_window
                    pass
                if active_window != last_window:
                    print(active_window)
                    last_window = active_window
                    tab_info = google_title_split(title)
                    if tab_info == last_google_tab:
                        print(f"Still on tab: {tab_info}")
                        last_google_tab = tab_info
                        pass

                if active_window == "Google Chrome":
                    time.sleep(1)
                    tab_info = google_title_split(title)
                    if tab_info != last_google_tab:
                        print(f"Google Chrome tab: {tab_info}")
                        last_google_tab = tab_info
#If it's google, get the tab info, if last tab is not same as new tab, print new info
#last_window starts as none, then active window is compared to last window (active window(anything) is definitely not equal to None)), print active then replace last window.

        except pgw.PyGetWindowException:
            pass

user_active_window()