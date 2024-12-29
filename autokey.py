import tkinter as tk
from tkinter import messagebox
import threading
import keyboard
import time

# Default variables
keys = ['W', 'A', 'S', 'D']
turn_on_key = 'p'
turn_off_key = 'o'
delay_ms = 12
press = False

# Function to start the key press loop
def start_key_press():
    global press
    press = True

def stop_key_press():
    global press
    press = False

def key_press_loop():
    global press, delay_ms, keys
    while True:
        if press:
            for key in keys:
                keyboard.press_and_release(key)
                time.sleep(delay_ms / 1000)

# Tkinter GUI
def create_gui():
    def update_settings():
        global keys, delay_ms
        try:
            keys_str = key_entry.get()
            keys = [key.strip() for key in keys_str.split(",")]
            delay_ms = int(delay_entry.get())
            messagebox.showinfo("Success", "Settings updated!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid delay (integer).")

    # Start the GUI
    root = tk.Tk()
    root.title("Key Trigger GUI")

    # Key Settings
    tk.Label(root, text="Keys to Press (comma-separated):").pack(pady=5)
    key_entry = tk.Entry(root)
    key_entry.insert(0, ",".join(keys))
    key_entry.pack(pady=5)

    # Delay Settings
    tk.Label(root, text="Delay (ms):").pack(pady=5)
    delay_entry = tk.Entry(root)
    delay_entry.insert(0, str(delay_ms))
    delay_entry.pack(pady=5)

    # Buttons
    tk.Button(root, text="Update Settings", command=update_settings).pack(pady=10)
    tk.Button(root, text="Start Key Press", command=start_key_press).pack(pady=5)
    tk.Button(root, text="Stop Key Press", command=stop_key_press).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()

# Run the key press loop in a separate thread
thread = threading.Thread(target=key_press_loop, daemon=True)
thread.start()

# Start the GUI
create_gui()