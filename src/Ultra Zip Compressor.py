"""
MIT License

Copyright (c) 2025 Olga Tsiouri, email: olgatsiouri@outlook.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def start_compression():
    input_folder = input_folder_var.get()

    if not input_folder:
        messagebox.showwarning("Input Error", "Please select an input folder.")
        return
    # Change directory
    os.chdir(os.path.dirname(input_folder))
    # Create WinRAR command  -m5: maximum compression
    command = f'WinRAR.exe a -afzip -m5 "{os.path.basename(input_folder)}.zip" "{os.path.basename(input_folder)}"'

    try:
     # Run command
        subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def select_folder():
    file_path = filedialog.askdirectory()
    input_folder_var.set(file_path)

# Set up tkinter app
app = tk.Tk()
app.title("Ultra Zip Compressor")

# Input file selection
input_folder_var = tk.StringVar()
tk.Label(app, text="Input folder to compress:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(app, textvariable=input_folder_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

# Start button
tk.Button(app, text="Compress folder", command=start_compression).grid(row=1, column=1, padx=10, pady=20)

# Trademark label
trademark_label = tk.Label(app,  text="Copyright (c) Olga Tsiouri, 2025 <olgatsiouri@outlook.com>", font=("Arial", 10), fg="black")
trademark_label.grid(row=2, column=0, columnspan=3, pady=(20, 10), sticky="s")

app.mainloop()
