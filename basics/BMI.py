# BMI Application

from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = float(weight_tf.get())
    m = float(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        status = 'Underweight'
    elif bmi > 18.5 and bmi < 24.9:
        status = 'Normal'
    elif bmi > 24.9 and bmi < 29.9:
        status = 'overweight'
    elif bmi > 29.9 and bmi < 34.9:
        status = 'Class I Obesity'
    elif bmi > 34.9 and bmi < 39.9:
        status = 'Class II Obesity'
    else:
        status = 'Class III Obesity'
    messagebox.showinfo('Body Max Index', f'BMI = {bmi} \nStatus: {status}')

ws = Tk()
ws.title('BMI Status')
ws.geometry('300x300+1000+50')
ws.resizable(0,0)

var = IntVar()

frame = Frame(ws,padx=10,pady=10)
frame.pack(expand=True)


age_lb = Label(frame,text='Enter Age (2 - 120)')
age_lb.grid(row=1, column=1)

age_tf = Entry(frame,)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(frame,text='Select Gender')
gen_lb.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(frame2,text = 'Male',variable = var,value = 1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2,text = 'Female',variable = var,value = 2)
female_rb.pack(side=RIGHT)

height_lb = Label(frame,text = "Enter Height (cm) ")
height_lb.grid(row=3, column=1)

weight_lb = Label(frame,text = "Enter weight (kg) ",)
weight_lb.grid(row=4, column=1)

height_tf = Entry(frame,)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(frame,)
weight_tf.grid(row=4,column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3,text='Calculate', command=calculate_bmi)
cal_btn.pack(side=LEFT)

reset_btn = Button(frame3,text = 'Reset',command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn = Button(frame3,text='Exit', command=lambda:ws.destroy())
exit_btn.pack(side=RIGHT)



ws.mainloop()
