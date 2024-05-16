import pyperclip
import socket
import time

# Define functions for each part of the script

def send_clipboard_content(target_ip, target_port):
    clipboard_content = pyperclip.paste()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        s.sendall(clipboard_content.encode('utf-8'))
        print("Clipboard content sent successfully.")

def receive_clipboard_content(listen_ip, listen_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((listen_ip, listen_port))
        s.listen()
        print("Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data = conn.recv(1024)
            if data:
                pyperclip.copy(data.decode('utf-8'))
                print("Clipboard content received and copied.")

def monitor_clipboard(target_ip, target_port):
    previous_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            previous_clipboard = current_clipboard
            send_clipboard_content(target_ip, target_port)
        time.sleep(1)

# User selects the mode of operation
if __name__ == "__main__":
    mode = input("Choose mode (send, receive, monitor): ").strip().lower()
    
    if mode == "send":
        target_ip = input("Enter the target IP address: ").strip()
        target_port = int(input("Enter the target port: ").strip())
        send_clipboard_content(target_ip, target_port)
    
    elif mode == "receive":
        listen_ip = input("Enter the listening IP address: ").strip()
        listen_port = int(input("Enter the listening port: ").strip())
        receive_clipboard_content(listen_ip, listen_port)
    
    elif mode == "monitor":
        target_ip = input("Enter the target IP address: ").strip()
        target_port = int(input("Enter the target port: ").strip())
        monitor_clipboard(target_ip, target_port)
    
    else:
        print("Invalid mode selected.")
