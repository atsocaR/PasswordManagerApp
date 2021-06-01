from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
# window.minsize(width=1200, height=800)
window.config(padx=50, pady=50)

# image
logo_image = PhotoImage(file="logo.png")

# Canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3, columnspan=1)

# buttons
generate_password_btn = Button(text='Generate Password')
generate_password_btn.grid(column=2, row=3, columnspan=1)

add_btn = Button(text='Add', width=35)
add_btn.grid(column=1, row=4, columnspan=2)




window.mainloop()
