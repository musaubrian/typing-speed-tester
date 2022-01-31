from pickle import FALSE
import tkinter as tk
import time
import threading
import random


class TypingSpeedGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("600x400")

        self.texts = open("./texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(
            self.frame, text=random.choice(self.texts), font=("Arial", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=30, font=("Arial", 20))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(
            self.frame, text="Speed: \n 0.00CPM\n 0.00WPM\n", font=("Arial", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(
            self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.isRunning = False

        self.root.mainloop()

    def start(self, event):
        if not self.isRunning:
            # ignores the shift, ctrl and alt keys
            if not event.keycode in [16, 17, 18]:
                self.isRunning = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        # checks if you are typing the correct thing if not text turns red
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.isRunning = False
            self.input_entry.config(fg="green")

    def reset(self):
        self.isRunning = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n 0.00CPS\n")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)

    def time_thread(self):
        while self.isRunning:
            time.sleep(0.1)
            self.counter += 0.1
            CPS = len(self.input_entry.get()) / self.counter
            CPM = CPS * 60
            WPS = len(self.input_entry.get().split(" ")) / self.counter
            WPM = WPS * 60
            self.speed_label.config(
                text=f"Speed: \n{CPM:.2F} CPM\n{WPM:.2F} WPM")


TypingSpeedGui()
