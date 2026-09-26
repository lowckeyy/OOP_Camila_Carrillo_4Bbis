import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application")
root.geometry("640x480")
root.minsize(50, 100)
root.maxsize(200, 100)

ttk.Label(root, text="hello").pack(padx=20, pady=20)


root.mainloop()