import tkinter as tk
from tkinter import messagebox

# --- Dina unika funktioner ---

def button1_callback():
    print("Knapp 1 aktiverad: Startar process A")
    messagebox.showinfo("Info", "Du tryckte på Knapp 1!")

def button2_callback():
    print("Knapp 2 aktiverad: Öppnar inställningar")

def button3_callback():
    print("Knapp 3 aktiverad: Sparar data")

def button4_callback():
    print("Knapp 4 aktiverad: Laddar om")

def button5_callback():
    print("Knapp 5 aktiverad: Avslutar programmet")
    root.quit()

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
btn1 = tk.Button(root, text="Kör Process A", command=button1_callback, width=20, pady=5)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Inställningar", command=button2_callback, width=20, pady=5)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Spara", command=button3_callback, width=20, pady=5)
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Ladda om", command=button4_callback, width=20, pady=5)
btn4.pack(pady=10)

btn5 = tk.Button(root, text="Avsluta", command=button5_callback, width=20, pady=5, fg="red")
btn5.pack(pady=10)

root.mainloop()