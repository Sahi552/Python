#importing library
import tkinter as t

# creating the main window
parent = t.Tk()

# creating buttons with consistent text and color
redbutton = t.Button(parent, text="Red", fg="red")
redbutton.pack(side=t.LEFT)

greenbutton = t.Button(parent, text="Green", fg="green")
greenbutton.pack(side=t.RIGHT)

bluebutton = t.Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=t.TOP)

blackbutton = t.Button(parent, text="Black", fg="black")
blackbutton.pack(side=t.BOTTOM)

# execute until you stop
parent.mainloop()
