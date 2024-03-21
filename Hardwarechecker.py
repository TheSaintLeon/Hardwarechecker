from tkinter import *   
from platform import * 
from psutil import *
from socket import *

# Oppretter et Tkinter-vindu
window = Tk()
window.title("Systeminformasjonssjekker")
window.geometry('1000x700')  # Angir størrelsen på vinduet
window.tk.call('tk', 'scaling', 2.0)  # Skalerer vinduet

# Oppretter etikett og knapp
lbl = Label(window, text="Velkommen til vår maskinvare sjekker")
lbl.grid(column=0, row=0, pady=(10, 0)) 
lbl.config(font=("Arial", 15))  # Angir skriftstørrelse

# Funksjon for å opprette og konfigurere etiketter
def create_label(text, row):
    lbl = Label(window, text=text, wraplength=300)
    lbl.grid(column=0, row=row, pady=(10, 0))
    lbl.config(font=("Arial", 15))

# Funksjon som kjøres når knappen trykkes
def search(e):
    btnOk.grid_remove()  # Fjerner knappen

    # Oppretter og viser etiketter med systeminformasjon
    create_label("OS: " + system(), 2)
    create_label("OS-versjon: " + version(), 3)
    create_label("OS-plattform: " + platform(), 4)
    create_label("Prosessor: " + processor(), 5)
    create_label("Antall CPU-er: " + str(cpu_count()), 6)
    total_memory_gb = virtual_memory().total / (1024 ** 3)  # Konverterer til GB 
    create_label("Minne: " + "{:.2f}".format(total_memory_gb) + " GB", 7)
    create_label("IP-adresse: " + gethostbyname(gethostname()), 8)

# Oppretter knappen
btnOk = Button(window, text="Start søk")
btnOk.grid(column=0, row=1, pady=(50, 0), padx=(10, 10))
btnOk.config(font=("Arial", 20))  
btnOk.bind("<Button-1>", search)

# Konfigurerer rutenettet for vinduet
window.grid_rowconfigure(8, weight=1)
window.grid_columnconfigure(0, weight=1)  

# Starter hovedloopen for Tkinter-vinduet
window.mainloop()
