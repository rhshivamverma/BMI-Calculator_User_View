#Create a Excetuable File for the User in python\
# BMI Executable File
import tkinter as tk
from tkinter import messagebox
root1 = tk.Tk()
root1.geometry('900x700')
def calculate_bmi():
    weight = float(e1.get())
    height = float(e2.get())
    bmi = weight/(height*height)
    bmi = round(bmi,2)
    message = 'BMI is'+ str(bmi)
    messagebox.showinfo('BMI',message)

var1 = tk.Label(root1, text = 'Enter the Weight in Kg')
var1.pack()
e1 = tk.Entry(root1)
e1.pack()

var2 = tk.Label(root1,text = 'Enter the Height in Meters')
var2.pack()
e2 = tk.Entry(root1)
e2.pack()

button1 = tk.Button(root1, text = 'Calculate BMI', command = calculate_bmi)
button1.pack()

button2 = tk.Button(root1, text = 'Exit', command = root1.destroy)
button2.pack()

root1.mainloop()



