import customtkinter as ctk
import platform
import psutil
import socket
import PIL

# Vinduet til selve programmet
app = ctk.CTk()
app.geometry("1000x700")
app.title("Hardware Checker")
ctk.set_appearance_mode("dark")
app.tk.call('tk', 'scaling', 2.0)

placement_config = {
"y_start": 0.2,
"y_increment": 0.5,
"relx": 0.5,
"anchor": ctk.CENTER,
"font": ("Arial", 20)
}

def delete_button_and_print():
    print("Sletter knappen")
    btn1.destroy()

    # Lager tekst når knappen er klikket på
    y_start = 0.2  # Plass mellom teksten vertikalt
    y_increment = 0.05  # Plass mellom hver tekst
    y = y_start

    labels = []  # Liste til å lagre labels
    
    label = ctk.CTkLabel(master=app, text="OS: {}".format(platform.system()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

    label = ctk.CTkLabel(master=app, text="OS-Versjon: {}".format(platform.version()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

    label = ctk.CTkLabel(master=app, text="OS-Platform: {}".format(platform.platform()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

    label = ctk.CTkLabel(master=app, text="Processor: {}".format(platform.processor()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

    label = ctk.CTkLabel(master=app, text="Processor Cores: {}".format(psutil.cpu_count()), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

    total_memory_gb = psutil.virtual_memory().total / (1024 ** 3)  # Endrer til GB
    label = ctk.CTkLabel(master=app, text="RAM: {:.2f} GB".format(total_memory_gb), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)

    # Lager en ny knapp for å gå over til neste skjerm
    nextbtn = ctk.CTkButton(master=app, text="Neste steg", corner_radius=32, fg_color="#0000FF",
    hover_color="#4158D0", command=lambda: next_btn(nextbtn, labels, btn1))
    nextbtn.place(relx=0.5, rely=0.50, anchor=ctk.CENTER)

def next_btn(button, labels, button1):
    # Sletter alt av informasjonen
    for label in labels:
        label.destroy()
    button.destroy()
    button1.destroy()
    network_page()

def network_page():
   
    # Lager tekst når knappen er klikket på
    y_start = 0.2  # Plass mellom teksten vertikalt
    y_increment = 0.05  # Plass mellom hver tekst
    y = y_start

    labels = []  # Liste til å lagre labels

    label = ctk.CTkLabel(master=app, text="IP-adresse: {}".format(socket.gethostbyname(socket.gethostname())), font = ("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=ctk.CENTER)
    labels.append(label)
    y += y_increment

# Label som viser velkomstteksten
label = ctk.CTkLabel(master=app, text="Velkommen til vår hardware checker", font=("Arial", 30))
label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

# Knapp som lar deg starte søket etter hardware
btn1 = ctk.CTkButton(master=app, text="Sjekk hardware", corner_radius=32, fg_color="#0000FF",
                hover_color="#4158D0", command=delete_button_and_print)
btn1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
btn1.configure(width=150, height=50)  # Endrer høyde og bredde på knappen

app.mainloop()
