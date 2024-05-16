import pyperclip
import socket

def send_clipboard_content():
    clipboard_content = pyperclip.paste()
    server_ip = 'DESKTOP_IP_ADDRESS'  # Replace with your desktop's IP address
    server_port = 65432  # Ensure this port is open and not in use

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.sendall(clipboard_content.encode('utf-8'))
        print("Clipboard content sent successfully.")

if __name__ == "__main__":
    send_clipboard_content()
