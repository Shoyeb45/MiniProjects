import time
import tkinter as tk
from datetime import datetime

currentTime = int(time.strftime('%H'))

# to return greeting
def greeting():
    if currentTime>=5 and currentTime<12:
        return "Good Morning"
    elif currentTime>=12 and currentTime<18:
        return "Good Afternoon"
    else:
        return "Good Evening"
    
#  for updating every time
    
def update_label():
    greet = greeting()
    label.config(text=greet)
    root.after(10000, update_label)

#  creating window
    
root = tk.Tk()
root.title("Greetings")

# Create a label to display the greeting
label = tk.Label(root, text="", font=("Roman", 16))
label.pack(padx=14, pady=14)

update_label() # updating window

# Set the window to be on top and transparent
root.attributes('-alpha', 0.8)
root.wm_attributes('-topmost', True)

# Set the window size and position
root.geometry("+1370+6")  # Adjust the position as needed

# Run the Tkinter main loop
root.mainloop()

