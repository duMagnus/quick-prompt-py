# import tkinter as tk
# from pynput import keyboard
# from pynput import mouse
# import pyautogui
#
# isOpen = False
# window = None
#
# def onActivate():
#     global isOpen, window
#     if not isOpen:
#         window = tk.Toplevel()
#         window.overrideredirect(True)
#         # set window width and height
#         window.configure(width=500, height=100)
#         # set window background color
#         window.configure(bg='lightgray')
#         mouseX, mouseY = pyautogui.position()
#         window.wm_geometry(f"+{mouseX}+{mouseY}")  # Set window position
#         window.attributes('-topmost', True)
#         isOpen = True
#
# def onDeactivate():
#     global isOpen, window
#     if isOpen and window:
#         window.destroy()
#         isOpen = False
#
# def onKeyPress(key):
#     if key == keyboard.Key.esc:
#         onDeactivate()
#
# def onHotkeyPress():
#     onActivate()
#
# def shouldWindowClose(x, y, button, pressed):
#     print(x, y, button, pressed)
#
# hotkey_listener = keyboard.GlobalHotKeys({
#     '<ctrl>+<alt>+k': onHotkeyPress
# })
#
# key_listener = keyboard.Listener(on_press=onKeyPress)
#
# mouseListener = mouse.Listener(on_click=shouldWindowClose)
#
# hotkey_listener.start()
# key_listener.start()
# mouseListener.start()
#
# root = tk.Tk()
# root.withdraw()
# root.mainloop()

import os
import openai
import requests

openai.api_key = "OPENAI_KEY"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

response.to_dict()
print(response.to_dict())