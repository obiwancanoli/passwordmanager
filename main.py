from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
numbers = string.digits
special_char = '!@#$%^&*?<>+'


def generate_password():

    pw_entry.delete(0, END)

    all_data = upper_letters + lower_letters + numbers + special_char
    random_pass = random.sample(all_data, 12)

    generated_pass = "".join(random_pass)
    # Copies generated password to clipboard for easy copy/paste
    pyperclip.copy(generated_pass)
    pw_entry.insert(END, generated_pass)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    user_website = web_entry.get()
    user_email_name = email_user_entry.get()
    user_password = pw_entry.get()

    if len(user_password) <= 0 or len(user_email_name) <= 0 or len(user_website) <=0:
        messagebox.showinfo(title="Error!", message="Please do not leave any fields empty!")
    else:

        # messagebox is used to verify if user wants to save their password.
        # is_ok is a boolean vaiable. Clicking "OK" = True
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \nEmail: {user_email_name} \nPassword: {user_password}")

        if is_ok:

            with open("password_file.txt", 'a') as file:
                file.write(f"{user_website}" + " | " + f"{user_email_name}" + " | " + f"{user_password}" + "\n")


        # .delete() deletes any content in the label.
        web_entry.delete(0, END)
        pw_entry.delete(0, END)

    




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo: 
# The canvas width and height is relative to the size of the image.
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")

# These x and y cooridinates need to be provided to show where image will be placed. 
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)


# Labels:

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)


pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)


# Entries: 

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

email_user_entry = Entry(width=35)
# email_user_entry.insert(0, "contactdanielmurillo@gmail.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3, columnspan=2)


# Buttons:

generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(row=4, column=1)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=5, column=1, columnspan=2)


# Mainloop:
window.mainloop()

