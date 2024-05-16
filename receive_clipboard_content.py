import pyperclip
import socket

def receive_clipboard_content():
    server_ip = '0.0.0.0'  # Listen on all network interfaces
    server_port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_ip, server_port))
        s.listen()
        print("Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data = conn.recv(1024)
            if data:
                pyperclip.copy(data.decode('utf-8'))
                print("Clipboard content received and copied.")

if __name__ == "__main__":
    receive_clipboard_content()
