from tkinter import *

window = Tk()
window.title("Zoznam úloh")
window.minsize(400, 300)
window.resizable(False, False)

# Fotn - collor

main_font = ("Time New Roman", 12)
main_color = "#a7f186"
button_color = "#a7f186"
window.configure(background=main_color)

# Použitie čisto tkinter PhotoImage
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window._icon_ref = icon  # uchováme referenciu, aby nezmizla

# Framy
input_frame = Frame(window, bg=button_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
window.config(bg=main_color)

input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - obsah
user_input = Entry(input_frame, width=35, borderwidth=3,font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Pridať",font=main_font, borderwidth=2,bg=button_color,fg=main_color)
add_button.grid(row=0, column=1 , padx=5, pady=5 , ipadx=10)

# Text frame - obsah
list_box = Listbox(text_frame,height=15 , width=50, borderwidth=3, font=main_font)
list_box.grid(row=0, column=0)

# Button frame - obsah
remove_button = Button(button_frame, text="Odstranit opoložku", borderwidth=2,bg=button_color,fg=main_color)
clear_button = Button(button_frame, text="Vymazať zoznam", borderwidth=2,bg=button_color,fg=main_color)
save_button = Button(button_frame, text="Ulož", borderwidth=2,bg=button_color,fg=main_color)
quit_button = Button(button_frame, text="Zavrieť", borderwidth=2,bg=button_color,fg=main_color , command=window.destroy)

remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=10)

window.mainloop()
