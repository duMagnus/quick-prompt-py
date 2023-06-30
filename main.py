import tkinter as tk
from pynput import keyboard
import pyautogui

isOpen = False
window = None

def onActivate():
    global isOpen, window
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

def onDeactivate():
    global isOpen, window
    if isOpen:
        window.destroy()
        isOpen = False

def onKeyPress(key):
    if key == keyboard.Key.esc:
        onDeactivate()

def onHotkeyPress():
    onActivate()

hotkey_listener = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+k': onHotkeyPress
})

key_listener = keyboard.Listener(on_press=onKeyPress)

hotkey_listener.start()
key_listener.start()

root = tk.Tk()
root.withdraw()
root.mainloop()
