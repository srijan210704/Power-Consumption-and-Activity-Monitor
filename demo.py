import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_power_data():
    return random.uniform(50, 150)  # Simulate power data (replace with actual sensor reading)

def read_system_activity():
    return random.uniform(0, 100)  # Simulate system activity (replace with actual reading)

def update_data(choice):
    if choice == 1:
        power = read_power_data()
        activity_label.config(text="System Activity: N/A")
        power_label.config(text=f"Power Consumption: {power:.2f} Watts")
        power_values.append(power)
    elif choice == 2:
        activity = read_system_activity()
        power_label.config(text="Power Consumption: N/A")
        activity_label.config(text=f"System Activity: {activity:.2f}%")
        activity_values.append(activity)
    plot_graph()

def get_user_choice():
    choice = sd.askinteger("Choose Monitor", "Enter your choice (1 for Power Consumption, 2 for Activity Monitor):", initialvalue=1)
    if choice in (1, 2):
        update_data(choice)
    else:
        messagebox.showerror("Invalid Choice", "Please enter a valid choice (1 or 2).")

def plot_graph():
    plt.clf()
    plt.plot(power_values, label='Power Consumption')
    plt.plot(activity_values, label='System Activity')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    canvas.draw()

root = tk.Tk()
root.title("Power and Activity Monitor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

power_label = tk.Label(frame, text="Power Consumption: N/A")
power_label.pack()

activity_label = tk.Label(frame, text="System Activity: N/A")
activity_label.pack()

update_button = tk.Button(frame, text="Update Data", command=get_user_choice)
update_button.pack()

# Matplotlib initialization
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
power_values = []
activity_values = []

root.mainloop()