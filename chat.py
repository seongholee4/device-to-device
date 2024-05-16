import pyperclip
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ClipboardChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Chat App")
        
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_display.pack(padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        self.entry_message = tk.Entry(root, width=40)
        self.entry_message.pack(padx=10, pady=10, side=tk.LEFT)
        
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10, side=tk.LEFT)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.server_thread = threading.Thread(target=self.receive_clipboard_content)
        self.server_thread.daemon = True
        self.server_thread.start()
        
    def send_message(self):
        message = self.entry_message.get()
        if message:
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.config(state=tk.DISABLED)
            self.entry_message.delete(0, tk.END)
            self.send_clipboard_content(message)
    
    def send_clipboard_content(self, content):
        target_ip = 'TARGET_IP_ADDRESS'  # Replace with the target IP address
        target_port = 65432  # Replace with the target port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            s.sendall(content.encode('utf-8'))
    
    def receive_clipboard_content(self):
        listen_ip = '0.0.0.0'
        listen_port = 65432
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((listen_ip, listen_port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    if data:
                        content = data.decode('utf-8')
                        self.chat_display.config(state=tk.NORMAL)
                        self.chat_display.insert(tk.END, f"Other: {content}\n")
                        self.chat_display.config(state=tk.DISABLED)
                        pyperclip.copy(content)
    
    def on_closing(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardChatApp(root)
    root.mainloop()
