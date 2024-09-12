import tkinter as tk  

def add(label_result, n1, n2):
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 + num2
    label_result.config(text="Result = %d" % result)

def sub(label_result, n1, n2):
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 - num2
    label_result.config(text="Result = %d" % result)

def mul(label_result, n1, n2):
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 * num2
    label_result.config(text="Result = %d" % result)

def div(label_result, n1, n2):
    num1 = int(n1.get())
    num2 = int(n2.get())
    if num2 == 0:
        label_result.config(text="Cannot divide by zero")
    else:
        result = num1 / num2
        label_result.config(text="Result = %.2f" % result)

root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="A")
labelNum1.place(x=50, y=20)

labelNum2 = tk.Label(root, text="B")
labelNum2.place(x=50, y=50)

buttonadd = tk.Button(root, text="+", command=lambda: add(labelResult, entryNum1, entryNum2))
buttonadd.place(x=100, y=80)

buttonsub = tk.Button(root, text="-", command=lambda: sub(labelResult, entryNum1, entryNum2))
buttonsub.place(x=200, y=80)

buttonmul = tk.Button(root, text="*", command=lambda: mul(labelResult, entryNum1, entryNum2))
buttonmul.place(x=100, y=110)

buttondiv = tk.Button(root, text="/", command=lambda: div(labelResult, entryNum1, entryNum2))
buttondiv.place(x=200, y=110)

labelResult = tk.Label(root)
labelResult.place(x=150, y=150)

entryNum1 = tk.Entry(root, textvariable=number1)
entryNum1.place(x=100, y=20)

entryNum2 = tk.Entry(root, textvariable=number2)
entryNum2.place(x=100, y=50)

root.mainloop()
