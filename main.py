from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.minsize(width=1200, height=800)

# image
lock_image = PhotoImage(file="logo.png")

# Canvas
canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=lock_image)
canvas.grid(column=3, row=1)
















window.mainloop()
