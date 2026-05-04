import tkinter as tk
import random
window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("400x250") 
window.resizable(False, False)
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
window.mainloop()