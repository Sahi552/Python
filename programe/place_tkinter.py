import tkinter as ak

tk = ak()

tk.geometry("400x250")  
name = Label(tk, text = "Name").place(x = 30,y = 50)  
email = Label(tk, text = "Email").place(x = 30, y = 90)  
password = Label(tk, text = "Password").place(x = 30, y = 130)
submit = Button(tk, text = "Submit").place(x = 30, y = 170)
e1 = Entry(tk).place(x = 80, y = 50)  
e2 = Entry(tk).place(x = 80, y = 90)  
e3 = Entry(tk).place(x = 95, y = 130)  
tk.mainloop()  
