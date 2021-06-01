from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
# window.minsize(width=1200, height=800)
window.config(padx=20, pady=20)

# image
lock_image = PhotoImage(file="logo.png")

# Canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)
















window.mainloop()
