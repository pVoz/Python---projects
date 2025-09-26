import tkinter as tk
def otvor_gui(meno):
    window = tk.Tk()
    window.title("Výsledok")
    window.geometry("400x200")
    label = tk.Label(window, text=meno, justify="left")
    label.pack(padx=20, pady=40)
    window.mainloop()

def open_window():
    vek = None
    def vloz():
        nonlocal vek
        vek = vek_entry.get()  # zoberie text z poľa
        # print(f"Zadal si vek: {vek}")  # vypíše do konzoly
        window.destroy()  # zavrie window
        # return vek
    # 1. Vytvorenie hlavného okna
    window = tk.Tk()
    window.title("Moje window")       # názov v hornom paneli okna
    window.geometry("300x250")      # veľkosť okna (šírka x výška v pixeloch)
    window.config(bg="black")
    vystup_label = tk.Label(window, text="Sem sa vypíše výsledok")
    vystup_label.pack()
    


    # 2. Popisok (Label)
    label = tk.Label(window, text="Riešenie Veku ,sortovanie")  # text nad vstupom
    label.pack(pady=(10, 5))  # umiestni label a pridá zvislý okraj (padding y-hore/dole)

    # 3. Vstupné pole (Entry)
    vek_entry = tk.Entry(window, width=20)  # textové pole na zadanie údajov
    vek_entry.pack()  # zobrazí pole pod labelom
    # 4. Funkcia, ktorá sa spustí po kliknutí na tlačidlo
    

    # 5. Tlačidlo (Button)
    button = tk.Button(window, text="Vlož", width=20, command=vloz)
    button.pack(pady=10)  # zobrazí tlačidlo s malým okrajom
    # 6. Spustenie aplikácie (zobrazí GUI)
    # vek = vloz() 
    # return
    window.mainloop()
    return vek
 


# vek = open_window()
# # print(open_window())