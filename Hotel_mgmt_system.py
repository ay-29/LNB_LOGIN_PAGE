from tkinter import *
import time
import random

root = Tk()
root.geometry("1600x800+0+0")
root.resizable(0, 0)
root.config(bg="white")
root.title("LEARN AND BUILD MANAGEMENT SYSTEM")

# Function to display current time
def show_time():
    current_time = time.asctime(time.localtime(time.time()))
    time_label.config(text=current_time)
    time_label.after(1000, show_time)

# Define variables for student details
student_name = StringVar()
student_roll = StringVar()
student_class = StringVar()
student_age = StringVar()
student_address = StringVar()

# Function to reset all entry fields
def reset_fields():
    student_name.set("")
    student_roll.set("")
    student_class.set("")
    student_age.set("")
    student_address.set("")

# Function to save student details
def save_details():
    name = student_name.get()
    roll = student_roll.get()
    s_class = student_class.get()
    age = student_age.get()
    address = student_address.get()

    # Here, you can add code to save the student details to a database or file
    # For now, we'll just print the details
    print("Student Details:")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Class:", s_class)
    print("Age:", age)
    print("Address:", address)
    print()

# Title Label
title_label = Label(root, text="LEARN AND BUILD MANAGEMENT SYSTEM", font=("Arial", 22, "bold"), bg="powder blue")
title_label.place(x=400, y=4)

# Time Label
time_label = Label(root, font=("Arial", 10, "bold"), bg="white")
time_label.place(x=600, y=70)
show_time()

# Student Details Labels
Label(root, text="Student Name:", font=("Arial", 12, "bold"), bg="white").place(x=100, y=150)
Label(root, text="Roll Number:", font=("Arial", 12, "bold"), bg="white").place(x=100, y=200)
Label(root, text="Class:", font=("Arial", 12, "bold"), bg="white").place(x=100, y=250)
Label(root, text="Age:", font=("Arial", 12, "bold"), bg="white").place(x=100, y=300)
Label(root, text="Address:", font=("Arial", 12, "bold"), bg="white").place(x=100, y=350)

# Student Details Entry Fields
Entry(root, bg="powder blue", textvariable=student_name, font=("Arial", 12)).place(x=250, y=150)
Entry(root, bg="powder blue", textvariable=student_roll, font=("Arial", 12)).place(x=250, y=200)
Entry(root, bg="powder blue", textvariable=student_class, font=("Arial", 12)).place(x=250, y=250)
Entry(root, bg="powder blue", textvariable=student_age, font=("Arial", 12)).place(x=250, y=300)
Entry(root, bg="powder blue", textvariable=student_address, font=("Arial", 12)).place(x=250, y=350)

# Buttons
Button(root, text="SAVE", font=("Arial", 12, "bold"), bg="powder blue", command=save_details).place(x=100, y=400)
Button(root, text="RESET", font=("Arial", 12, "bold"), bg="powder blue", command=reset_fields).place(x=200, y=400)
Button(root, text="EXIT", font=("Arial", 12, "bold"), bg="powder blue", command=root.destroy).place(x=300, y=400)

root.mainloop()
