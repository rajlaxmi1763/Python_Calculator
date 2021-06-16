from tkinter import *
from tkinter.messagebox import *

# some useful variable
font = ('Constantia', 15, 'bold')


# important functions
def clear():
    exp = textfield.get()
    exp = exp[0:len(exp) - 1]
    textfield.delete(0, END)
    textfield.insert(0, exp)


def all_clear():
    textfield.delete(0, END)


def click_btn_fun(event):
    b = event.widget
    text = b['text']
    if text == 'x':
        textfield.insert(END, '*')
        return

    if text == '=':
        try:
            exp = textfield.get()
            answer = eval(exp)
            textfield.delete(0, END)
            textfield.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return
    textfield.insert(END, text)


# creating a window
window = Tk()
window.title('Calculator')
window.minsize(400, 450)
window.resizable(0, 0)
window.configure(background='#2c3e50')

# heading label
heading = Label(window, text='My Calculator', font=font, bg='#2c3e50', fg='#ffffff')
heading.pack(side=TOP)

# textfiled
textfield = Entry(window, font=font, justify=CENTER)
textfield.pack(side=TOP, pady=5, fill=X, padx=5)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)
buttonFrame.configure(background='#2c3e50')

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, bg='#7f8c8d', relief='sunken',
                     activebackground='orange', activeforeground='white')
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp += 1
        btn.bind('<Button-1>', click_btn_fun)

zerobtn = Button(buttonFrame, text='0', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                 activeforeground='white')
zerobtn.grid(row=3, column=0, padx=3, pady=3)

dotbtn = Button(buttonFrame, text='.', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                activeforeground='white')
dotbtn.grid(row=3, column=1, padx=3, pady=3)

equalbtn = Button(buttonFrame, text='=', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                  activeforeground='white')
equalbtn.grid(row=3, column=2, padx=3, pady=3)

plusbtn = Button(buttonFrame, text='+', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                 activeforeground='white')
plusbtn.grid(row=0, column=3, padx=3, pady=3)

minusbtn = Button(buttonFrame, text='-', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                  activeforeground='white')
minusbtn.grid(row=1, column=3, padx=3, pady=3)

multiplybtn = Button(buttonFrame, text='x', font=font, width=5, bg='#7f8c8d', relief='sunken',
                     activebackground='orange', activeforeground='white')
multiplybtn.grid(row=2, column=3, padx=3, pady=3)

dividebtn = Button(buttonFrame, text='/', font=font, width=5, bg='#7f8c8d', relief='sunken', activebackground='orange',
                   activeforeground='white')
dividebtn.grid(row=3, column=3, padx=3, pady=3)

clearbtn = Button(buttonFrame, text='<--', font=font, width=12, bg='#7f8c8d', relief='sunken',
                  activebackground='orange', activeforeground='white', command=clear)
clearbtn.grid(row=4, column=0, padx=3, pady=3, columnspan=2)

allclearbtn = Button(buttonFrame, text='AC', font=font, width=12, bg='#7f8c8d', relief='sunken',
                     activebackground='orange', activeforeground='white', command=all_clear)
allclearbtn.grid(row=4, column=2, padx=3, pady=3, columnspan=2)

# binding all buttons
zerobtn.bind('<Button-1>', click_btn_fun)
dotbtn.bind('<Button-1>', click_btn_fun)
equalbtn.bind('<Button-1>', click_btn_fun)
plusbtn.bind('<Button-1>', click_btn_fun)
minusbtn.bind('<Button-1>', click_btn_fun)
multiplybtn.bind('<Button-1>', click_btn_fun)
dividebtn.bind('<Button-1>', click_btn_fun)


############################################# SCIENTIFIC MODE ##############################################
# functions of sc:
def sc_click_btn():
    print("Clicked")


menubar = Menu(window, font=font)
mode = Menu(menubar, font=font, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click_btn)
menubar.add_cascade(label="Mode", menu=mode)
window.config(menu=menubar)

window.mainloop()
