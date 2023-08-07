import pygetwindow as pgw
import time
import json

def split_window_title(title):
    title_parts = title.split(' - ')
    return title_parts[-1]

def google_title_split(title):
    title_parts = title.split(' - ')
    return title_parts[-2]

def save_time_data(data):
    with open('time_tracker.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def user_active_window():
    last_window = None
    last_google_tab = None
    start_time = time.time()
    tracked_data = {}  # Dictionary to store tracked data
# IDK what this does yet
    try:
        with open('time_tracker.json', 'r') as json_file:
            tracked_data = json.load(json_file)
    except FileNotFoundError:
        pass

    while True:
        try:
            window = pgw.getActiveWindow()
            if window is not None:
                title = window.title
                active_window = split_window_title(title)

                if active_window == "Task Switching":
                    active_window = last_window
                    pass
                # Code below is for when user swtiches between applications and Google
                # Gets elapsed time between the last window and the new window
                if active_window != last_window:
                    if last_window is not None:
                        elapsed_time = int(time.time() - start_time)
                        # Check if the active window is Google Chrome
                        # If it is Google and there was a last tab, 
                        if last_window == "Google Chrome":
                            if last_google_tab is not None:
                                # Loading data into JSON file
                                # This is for the tabs for Google, not Google itself.
                                # This takes the tracked_data dictionary from above and sets the default to 0 and "Google Chrome". If Chrome exists, this does nothing
                                tracked_data.setdefault("Google Chrome", {}).setdefault(last_google_tab, 0)
                                # Afterwards, it gets the Google Chrome key and the last Google tab and adds the elapsed time.
                                tracked_data["Google Chrome"][last_google_tab] += elapsed_time
                        else:
                            # ELSE, if it isn't a Google tab, add the elapsed time to Google Chrome itself.
                            if last_window not in tracked_data:
                                tracked_data[last_window] = 0
                                tracked_data[last_window] += elapsed_time
                            else:
                                tracked_data[last_window] += elapsed_time

                        save_time_data(tracked_data)
                    # Prints the application the user is on
                    print(f"Application: {active_window}\n")
                    # Sets the current window to the last window for future use.
                    last_window = active_window
                    # Reset the last_google_tab when switching to a new application, this acutally does help
                    last_google_tab = None 
                    start_time = time.time()
####################################################################################################################################
                # Gets Google tab information to display
                if active_window == "Google Chrome":
                    time.sleep(1)
                    tab_info = google_title_split(title)
                    # For when user remains on a tab, will delete soon
                    if tab_info == last_google_tab:
                        print(f"\033AStill on the tab: {tab_info}\n")
                    else:
                        # If the user doesn't remain on the same tab, move to this
                        if last_google_tab is not None:
                            elapsed_time = int(time.time() - start_time)
                            # Adds Google tabs time elapsed. Same code up top, but this is when the window is actually Google. 
                            # Both of the identical codes add the time elapsed in the Google tabs to the JSON file. 
                            tracked_data.setdefault("Google Chrome", {}).setdefault(last_google_tab, 0)
                            tracked_data["Google Chrome"][last_google_tab] += elapsed_time
                            save_time_data(tracked_data)

                        print(f"Google Chrome tab: {tab_info}\n")
                        last_google_tab = tab_info
                        start_time = time.time()

        except pgw.PyGetWindowException:
            pass

user_active_window()
