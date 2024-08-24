import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("350x250")
        self.master.resizable(False, False)

        
        self.label = tk.Label(self.master, text="Enter desired password length:")
        self.label.pack(pady=10)

        
        self.length_entry = tk.Entry(self.master)
        self.length_entry.pack(pady=5)

        
        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        
        self.password_label = tk.Label(self.master, text="",  wraplength=300)
        self.password_label.pack(pady=10)

    def get_password_length(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Invalid Length", "Please enter a positive number.")
                return None
            
            return length
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return None

    def generate_password(self):
        length = self.get_password_length()
        if length is None:
            return

        
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(all_chars) for _ in range(length))

        
        self.password_label.config(text=f"Your Password:\n{password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
