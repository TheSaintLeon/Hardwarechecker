from customtkinter import *
from platform import *
from psutil import *
from socket import *
from PIL import *

# Vinduet til selve programmet
app = CTk()
app.geometry("1000x700")
app.title("Hardware Checker")
set_appearance_mode("dark")

def delete_button_and_print():
    print("Sletter knappen")
    btn1.destroy()

    # Lager tekst når knappen er klikket på
    y_start = 0.2  # Plass mellom teksten vertikalt
    y_increment = 0.05  # Plass mellom hver tekst
    y = y_start

    labels = []  # Liste til å lagre labels
    label = CTkLabel(master=app, text="OS: {}".format(system()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)
    y += y_increment

    label = CTkLabel(master=app, text="OS-Versjon: {}".format(version()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)
    y += y_increment

    label = CTkLabel(master=app, text="OS-Platform: {}".format(platform()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)
    y += y_increment

    label = CTkLabel(master=app, text="Processor: {}".format(processor()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)
    y += y_increment

    label = CTkLabel(master=app, text="Processor Cores: {}".format(cpu_count()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)
    y += y_increment

    total_memory_gb = virtual_memory().total / (1024 ** 3)  # Endrer til GB
    label = CTkLabel(master=app, text="RAM: {:.2f} GB".format(total_memory_gb), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)

    # Lager en ny knapp for å gå over til neste skjerm
    nextbtn = CTkButton(master=app, text="Neste steg", corner_radius=32, fg_color="#0000FF",
                           hover_color="#4158D0", command=lambda: next_btn(nextbtn, labels, btn1))
    nextbtn.place(relx=0.5, rely=0.50, anchor=CENTER)

def next_btn(button, labels, button1):
    # Sletter alt av informasjonen
    for label in labels:
        label.destroy()
    button.destroy()
    button1.destroy()

# Label som viser velkomstteksten
label = CTkLabel(master=app, text="Velkommen til vår hardware checker", font=("Arial", 30))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Knapp som lar deg starte søket etter hardware
btn1 = CTkButton(master=app, text="Sjekk hardware", corner_radius=32, fg_color="#0000FF",
                hover_color="#4158D0", command=delete_button_and_print)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
btn1.configure(width=150, height=50)  # Endrer høyde og bredde på knappen

app.mainloop()
