from tkinter import *   
from platform import * 
from psutil import *
from socket import *
# Window information / Size + Name
window = Tk()
window.title("System info checker")
window.geometry('1000x700')
window.tk.call('tk', 'scaling', 2.0)

# Label + Button
lbl = Label(window, text="Welcome to our hardware checker")
lbl.grid(column=0, row=0, pady=(10, 0)) 
lbl.config(font=("Arial", 15))


def search(e):
    btnOk.grid_remove() 

    lbl = Label(window, text="OS: " + system(), wraplength=300)
    lbl.grid(column=0, row=2, pady=(10, 0))
    lbl.config(font=("Arial", 15))
    lbl = Label(window, text="OS Version: " + version(), wraplength=300)
    lbl.grid(column=0, row=3, pady=(10, 0))
    lbl.config(font=("Arial", 15))
    lbl = Label(window, text="OS Platform: " + platform(), wraplength=300)
    lbl.grid(column=0, row=4, pady=(10, 0))
    lbl.config(font=("Arial", 15))
    lbl = Label(window, text="Processor: " + processor(), wraplength=300)
    lbl.grid(column=0, row=5, pady=(10, 0))
    lbl.config(font=("Arial", 15))
    lbl = Label(window, text="CPU Count: " + str(cpu_count()), wraplength=300)
    lbl.grid(column=0, row=6, pady=(10, 0))
    lbl.config(font=("Arial", 15))
    total_memory_gb = virtual_memory().total / (1024 ** 3)  # Convert bytes to gigabytes
    lbl = Label(window, text="Memory: " + "{:.2f}".format(total_memory_gb) + " GB", wraplength=300)
    lbl.grid(column=0, row=7, pady=(10, 0), padx=(10, 5))
    lbl.config(font=("Arial", 15))
    lbl = Label(window, text="IP Address: " + gethostbyname(gethostname()), wraplength=300)
    lbl.grid(column=0, row=8, pady=(10, 0), padx=(10, 5))
    lbl.config(font=("Arial", 15))



btnOk = Button(window, text="Start search")
btnOk.grid(column=0, row=1, pady=(50, 0), padx=(10, 10))
btnOk.config(font=("Arial", 20))  
btnOk.bind("<Button-1>", search)

window.grid_rowconfigure(8, weight=1)
window.grid_columnconfigure(0, weight=1)  



window.mainloop()

