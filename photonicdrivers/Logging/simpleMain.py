from logToGraphana import logG

import tkinter as tk
from tkinter import ttk
import random
import threading
import time

class RandomNumberGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("loggingmyvar")
        self.running = False

        self.start_button = ttk.Button(root, text="Start", command=self.start_generating)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_generating, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.log_box = tk.Text(root, height=10, width=50)
        self.log_box.pack(pady=10)

    def start_generating(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.thread = threading.Thread(target=self.generate_random_numbers)
        self.thread.start()

    def stop_generating(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def generate_random_numbers(self):
        while self.running:
            random_number = random.randint(0, 100)
            self.log_box.insert(tk.END, f"{random_number}\n")
            self.log_box.yview(tk.END)
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()