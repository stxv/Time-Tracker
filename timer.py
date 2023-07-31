import pygetwindow as pgw
import time
def split_window_title(title):
    title_parts = title.split(' - ')
    return title_parts

def user_active_window():
    active_window = pgw.getActiveWindow()
    title = active_window.title
    title_list = split_window_title(title)
    print(title_list[-1])
    
user_active_window()

