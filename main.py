from tkinter import *

window= Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


label_1= Label(text="Enter Your Weight (kg)")
label_1.config(fg="black")
label_1.config(padx=4, pady=4)
label_1.pack()


entry_1= Entry()
entry_1.pack()

label_2= Label(text="Enter Your Height (cm)")
label_2.config(fg="black")
label_2.config(padx=4, pady=4)
label_2.pack()

entry_2= Entry()
entry_2.pack()

def button_clicked():
    weight = entry_1.get()
    height = entry_2.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmı = (float(weight) / (float(height) ** 2)) *10000
            if bmı <= 18.4:
                label_3= Label(text="Your BMI is {}. You are underweight.".format(round(bmı,2)))
                label_3.config(padx=4, pady=4)
                label_3.pack()
            elif bmı>18.5 and bmı<24.9:
                label_4 = Label(text="Your BMI is {}. You are normal weight.".format(bmı))
                label_4.config(padx=4, pady=4)
                label_4.pack()
            elif bmı>25.0 and bmı<39.9:
                label_5 = Label(text="Your BMI is {}. You are overweight.".format(bmı))
                label_5.config(padx=4, pady=4)
                label_5.pack()
            else:
                label_6 = Label(text="Your BMI is {}. You are obese.".format(bmı))
                label_6.config(padx=4, pady=4)
                label_6.pack()
        except:
            result_label.config(text="Enter a valid number")




button= Button(text="Calculate", command= button_clicked)
button.config(padx=4, pady=4)
button.pack()

result_label= Label()
result_label.pack()

window.mainloop()
