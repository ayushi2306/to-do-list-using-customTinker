import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

tasks = []


def update_tasks():
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")

    for index, task in enumerate(tasks, start=1):
        textbox.insert("end", f"{index}. {task}\n")

    textbox.configure(state="disabled")


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append(task)

    update_tasks()

    entry.delete(0, "end")


def delete_task():
    value = delete_entry.get().strip()

    if not value.isdigit():
        messagebox.showwarning("Warning", "Enter a valid task number!")
        return

    index = int(value) - 1

    if index < 0 or index >= len(tasks):
        messagebox.showwarning("Warning", "Task not found!")
        return

    tasks.pop(index)

    delete_entry.delete(0, "end")

    update_tasks()


app = ctk.CTk()

app.geometry("500x500")
app.title("Modern To Do App")

title = ctk.CTkLabel(
    app,
    text="To Do List",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter a task..."
)
entry.pack()

add_btn = ctk.CTkButton(
    app,
    text="Add Task",
    command=add_task
)
add_btn.pack(pady=10)

textbox = ctk.CTkTextbox(
    app,
    width=350,
    height=220
)
textbox.pack()

textbox.configure(state="disabled")

delete_entry = ctk.CTkEntry(
    app,
    width=120,
    placeholder_text="Task Number"
)
delete_entry.pack(pady=10)

delete_btn = ctk.CTkButton(
    app,
    text="Delete Task",
    command=delete_task
)
delete_btn.pack()

app.mainloop()