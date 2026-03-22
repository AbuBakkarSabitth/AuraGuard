import tkinter as tk
import subprocess
process = None
def start_monitoring():
    global process
    if process is None:
        process = subprocess.Popen(['python','auraguard.py'])
def stop_monitoring():
    global process
    if process is not None:
        process.terminate()
        process = None
def exit_app():
    stop_monitoring()
    root.destroy()
root = tk.Tk()
root.title("AuraGuard")
root.geometry("300x200")
title = tk.Label(root, text = "AuraGuard Monitor",font= ("Arial",14))
title.pack(pady=20)
start_button = tk.Button(root, text = "Start Monitoring", command = start_monitoring)
start_button.pack(pady=5)
stop_button = tk.Button(root, text = "Stop Monitoring", command = stop_monitoring)
stop_button.pack(pady=5)
exit_button = tk.Button(root, text = "Exit", command = exit_app)
exit_button.pack(pady=5)
root.mainloop()