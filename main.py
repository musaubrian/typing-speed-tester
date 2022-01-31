import tkinter as tk
import time
import threading
import random


class TypingSpeedGui:
    def __init__(self):
        self.root = tk.Tk();
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text = random.choice(self.texts), font=("Arial", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, wisth=30, font=("Arial", 20))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<keyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text = "Speed: \n 0.00CPS\n 0.00CPM", font=("Arial", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.isRunning = False

        self.root.mainloop()

    def start(self, event):
        pass

    def reset(self):
        pass

    def time_thread(self):
        while self.isRunning:
            time.sleep(0.1)
            self.counter += 0.1
            CPS = len(self.input_entry.get()) /self.counter
            CPM = CPS * 60
            self.speed_label.config(text=f"Speed: \n{CPS:.2F} CPS\n{CPM:.2F} CPM")    


