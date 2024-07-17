# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:50:02 2024

@author: SinhVien
"""

import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Get data from entry fields
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_var.get()
    age = age_spinbox.get()
    nationality = nationality_entry.get()
    is_registered = registered_var.get()
    courses_completed = completed_courses_spinbox.get()
    semesters = semesters_spinbox.get()

    # Check if the user agreed to the terms and conditions
    if not terms_var.get():
        messagebox.showerror("Error", "You need to accept the terms and conditions")
        return

    # Print the form data to the console
    print(f"""
        User Information:
            - Ten: {first_name}
            - ho: {last_name}
            - chuc vu: {title}
            - tuoi: {age}
            - quoc tich: {nationality}

        Registration Status:
            - Currently Registered: {"Yes" if is_registered else "No"}
            - Completed Courses: {courses_completed}
            - Semesters: {semesters}
    """)

root = tk.Tk()
root.title("Data Entry Form")
root.geometry("600x450")

# User Information Frame
user_info_frame = tk.LabelFrame(root, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

tk.Label(user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(user_info_frame, text="Last Name").grid(row=0, column=2, padx=5, pady=5, sticky="w")
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

tk.Label(user_info_frame, text="Title").grid(row=0, column=4, padx=5, pady=5, sticky="w")
title_var = tk.StringVar()
title_menu = tk.OptionMenu(user_info_frame, title_var, "Mr", "Mrs", "Ms", "Dr")
title_var.set("Select")
title_menu.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

tk.Label(user_info_frame, text="Age").grid(row=1, column=0, padx=5, pady=5, sticky="w")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=100)
age_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(user_info_frame, text="Nationality").grid(row=1, column=2, padx=5, pady=5, sticky="w")
nationality_entry = tk.Entry(user_info_frame)
nationality_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# Registration Status Frame
registration_frame = tk.LabelFrame(root, text="Registration Status")
registration_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

registered_var = tk.BooleanVar()
tk.Checkbutton(registration_frame, text="Currently Registered", variable=registered_var).grid(row=0, column=0, padx=5, pady=5, sticky="w")

tk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5, sticky="w")
completed_courses_spinbox = tk.Spinbox(registration_frame, from_=0, to=100)
completed_courses_spinbox.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

tk.Label(registration_frame, text="# Semesters").grid(row=0, column=3, padx=5, pady=5, sticky="w")
semesters_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
semesters_spinbox.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

# Terms & Conditions Frame
terms_frame = tk.LabelFrame(root, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

terms_var = tk.BooleanVar()
tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=terms_var).grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Submit Button
submit_button = tk.Button(root, text="Enter data", command=submit_form)
submit_button.grid(row=3, column=0, padx=20, pady=20)

# Allow the columns to expand
for i in range(6):
    user_info_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
