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
    print("Button pressed! Text displayed after button press")
    btn1.destroy()

    # Create and place the label after the button is pressed
    y_start = 0.2  # Adjust this value to set the starting vertical position
    y_increment = 0.05  # Adjust this value to set the vertical spacing between labels
    y = y_start

    labels = []  # List to store labels
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

    total_memory_gb = virtual_memory().total / (1024 ** 3)  # Konverterer til GB 
    label = CTkLabel(master=app, text="RAM: {:.2f} GB".format(total_memory_gb), font=("Arial", 20))
    label.place(relx=0.5, rely=y, anchor=CENTER)
    labels.append(label)

    # Add a new button with the same function for new labels
    nextbtn = CTkButton(master=app, text="Neste steg", corner_radius=32, fg_color="#0000FF",
                           hover_color="#4158D0", command=lambda: next_btn(nextbtn, labels, btn1))
    nextbtn.place(relx=0.5, rely=0.50, anchor=CENTER)

def next_btn(button, labels, button1):
    # Destroy all labels and buttons
    for label in labels:
        label.destroy()
    button.destroy()
    button1.destroy()

# Label som viser velkomstteksten
label = CTkLabel(master=app, text="Velkommen til vår hardware checker", font=("Arial", 30))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Knapp som lar deg stare søket etter hardware
btn1 = CTkButton(master=app, text="Sjekk hardware", corner_radius=32, fg_color="#0000FF",
                hover_color="#4158D0", command=delete_button_and_print)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
btn1.configure(width=150, height=50)  # Endrer høyde og bredde på knappen

app.mainloop()
