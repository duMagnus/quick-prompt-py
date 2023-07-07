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

openai.api_key = os.getenv("OPENAI_KEY")

def ask_openai(prompt):

    # Ask Azure OpenAI
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    text = response['choices'][0]['text'].replace('\n', ' ').replace(' .', '.').strip()
    print('Azure OpenAI response:' + text)

def chat_with_open_ai():
    while True:
        print("Azure OpenAI is listening. Say 'Stop' or press Ctrl-Z to end the conversation.")
        try:
            ask_openai(input())
        except EOFError:
            break

# Main

try:
    chat_with_open_ai()
except Exception as err:
    print("Encountered exception. {}".format(err))