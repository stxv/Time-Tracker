A productivity program tracks time spent on applications and Google Chrome tabs.

I made this program out of curiosity about how I'd spend my time while on a computer.

I began the program by listing functions that would help. Since pygetwindow would return outputs in this form:['timer.py', 'Time-Tracker', 'Visual Studio Code'], the functions would get just the name of the application rather than what it was on.

Since I used Google often, I made a function that attempted to get the Google tab that I was on. This would be very inconsistent since not all Google tab titles were structured the same. It would work for website like Youtube, Gmail, and Outlook. Other websites would just have the title of what you're looking at and it doesn't provide any context. An example would be Notion. Notion would display the page you create as the Google tab title. So if your Notion page was "Notes", the program would say that you've been on "Notes" for however long you were on the page.

The program would get the current focused window as long as the code is running and begins counting the seconds you remain in that window. when the focused window is switched, it adds the time to the previous window and begins a new count. The amount of time is then put into a JSON file that you can review after stopping the program.

The main issue with the program would be that if Google is the main browser, the tabs aren't structured the same which makes the code lack context sometimes. I haven't tried applying other browsers like Internet Explorer or FireFox. Prorgam isn't perfect but it is useful for getting a general idea of how time is spent on the computer.