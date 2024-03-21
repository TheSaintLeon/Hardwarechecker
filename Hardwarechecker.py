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

def create_label(text, row):
    lbl = Label(window, text=text, wraplength=300)
    lbl.grid(column=0, row=row, pady=(10, 0))
    lbl.config(font=("Arial", 15))

def search(e):
    btnOk.grid_remove() 

    create_label("OS: " + system(), 2)
    create_label("OS Version: " + version(), 3)
    create_label("OS Platform: " + platform(), 4)
    create_label("Processor: " + processor(), 5)
    create_label("CPU Count: " + str(cpu_count()), 6)
    total_memory_gb = virtual_memory().total / (1024 ** 3)  # Konverterer til GB 
    create_label("Memory: " + "{:.2f}".format(total_memory_gb) + " GB", 7)
    create_label("IP Address: " + gethostbyname(gethostname()), 8)

btnOk = Button(window, text="Start search")
btnOk.grid(column=0, row=1, pady=(50, 0), padx=(10, 10))
btnOk.config(font=("Arial", 20))  
btnOk.bind("<Button-1>", search)

window.grid_rowconfigure(8, weight=1)
window.grid_columnconfigure(0, weight=1)  

window.mainloop()
