import tkinter as tk
from tkinter import ttk
import os
from abc import ABC, abstractmethod #


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass

class SmartSpeaker(SmartDevice):
    def __init__(self, name):
        super().__init__("Echo Dot 5")

    def turn_on(self):
        return f"{self.name} is ON. Enjoy your favorite music!"

class SmartTv(SmartDevice):
    def __init__(self, name):
        super().__init__("LG Smart Tv")

    def turn_on(self):
        return f"{self.name} is ON. Enjoy your favorite shows!"

class SmartLigth(SmartDevice):
    def __init__(self, name):
        super().__init__("Smart Light")

    def turn_on(self):
        return f"{self.name} is ON. Brighten up your space!"

class smarthomeapp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism with Camila Keilany Carrillo Fuentes")
        self.geometry("480x360")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "icon.png")
        if os.path.exists(icon_path):
            self.iconphoto(False, tk.PhotoImage(file=icon_path))
        else:
            print("Icon file not found. Using default icon.")

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "TV": SmartTv("LG Smart Tv"),
            "Speaker": SmartSpeaker("Echo Dot 5"),
            "Light": SmartLigth("Smart Light"),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Times New Roman", 25, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Times New Roman", 18, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn On device",
            command=self._handle_action,
            bg="#79577c",
            fg="white",
            font=("Times New Roman", 12, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'Turn On device'.",
            font=("Times New Roman", 10, "italic"),
            bg="#ecf0f1",
            fg="#2e045e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_on()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Times New Roman", 10, "normal"))



# LAUNCHER
if __name__ == "__main__":
    app = smarthomeapp()
    app.mainloop()