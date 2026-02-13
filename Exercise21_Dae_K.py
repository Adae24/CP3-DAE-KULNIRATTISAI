from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))        #.get ใช้ดึงค่า
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if BMI >= 30:
        labelResult.configure(text="Super fat")
    elif (BMI >= 25 and BMI <= 29.9):
        labelResult.configure(text="Fat")
    elif (BMI >= 23.0 and BMI <= 24.9):
        labelResult.configure(text="Overweight")
    elif (BMI >= 18.6 and BMI <= 22.9):
        labelResult.configure(text="Normal")
    else:
        labelResult.configure(text="Skinny")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="Height (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)           # Entry ใช้รับค่า
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="Weight (Kg)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)           # Entry ใช้รับค่า
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column =0)
labelResult = Label(MainWindow, text="Result")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()