import tkinter as tk
from pynput import keyboard
import pyautogui

isOpen = False
def onActivate():
    global isOpen
    if not isOpen:
        window = tk.Toplevel()
        window.overrideredirect(True)
        # set window width and height
        window.configure(width=500, height=300)
        # set window background color
        # window.configure(bg='lightgray', border)
        mouseX, mouseY = pyautogui.position()
        window.geometry(f"+{mouseX}+{mouseY}")  # Set window position
        window.attributes('-topmost', True)
        isOpen = True


listener = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+k': onActivate
})

listener.start()

root = tk.Tk()
root.withdraw()
root.mainloop()
