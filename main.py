
import tkinter as tk
from tkinter import messagebox
from backend import Backend
from backend import Message as BackendMessage
# --- Dina unika funktioner ---
class Meny:
    def __init__(self, backend):
        self.backend:Backend = backend

    def button1_callback(self, button_widget):
        message:BackendMessage = self.backend.button1()
        self._check_message_success(button_widget, message)
        print(message.message)

    def button2_callback(self, button_widget):
        print("Knapp 2 aktiverad: Öppnar inställningar")

    def button3_callback(self, button_widget):
        print("Knapp 3 aktiverad: Sparar data")

    def button4_callback(self, button_widget):
        print("Knapp 4 aktiverad: Laddar om")

    def button5_callback(self, button_widget):
        print("Knapp 5 aktiverad: Avslutar programmet")
        root.quit()

    # Din nya smarta hjälpfunktion!
    def _check_message_success(self, button_widget, message:BackendMessage):
        if message.success:
            button_widget.config(bg="green", activebackground="lightgreen")
        else:
            button_widget.config(bg="red", activebackground="salmon")


backend = Backend()
my_meny = Meny(backend = backend)
# --- GUI-uppbyggnad ---

root = tk.Tk()
root.title("Min Applikation")
root.geometry("300x450")

# Rubrik
header = tk.Label(
    root, 
    text="Huvudmeny", 
    font=("Helvetica", 18, "bold"), 
    pady=20
)
header.pack()

# Skapa knapparna manuellt för att koppla dem till de specifika funktionerna
btn1 = tk.Button(root, text="Kör Process A", command=lambda: my_meny.button1_callback(btn1), width=20, pady=5)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Inställningar", command=my_meny.button2_callback, width=20, pady=5)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Spara", command=my_meny.button3_callback, width=20, pady=5)
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Ladda om", command=my_meny.button4_callback, width=20, pady=5)
btn4.pack(pady=10)

btn5 = tk.Button(root, text="Avsluta", command=my_meny.button5_callback, width=20, pady=5, fg="red")
btn5.pack(pady=10)

root.mainloop()