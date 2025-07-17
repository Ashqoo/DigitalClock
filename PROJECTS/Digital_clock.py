import tkinter as drj
from time import strftime
root=drj.Tk()
root.title("digital Clock")

def time():
    string = strftime(" %H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)

label= drj.Label(root , font=('calibri', 50, "bold"), background="yellow" , foreground="black")  
label.pack(anchor="e")  
time()
root.mainloop()
    