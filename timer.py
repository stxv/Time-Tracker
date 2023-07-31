import pygetwindow as pgw

def user_active_window():
    active_window = pgw.getActiveWindow()
    print(active_window.title)

user_active_window()