from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
list_of_words = ["Trantor",
"Naboo", "Targaryen", "Skywalker",
"Galactica", "Caprica", "Tatooine",
"Stark", "Thanos", "Kamino",
"Mandalore", "Ilum", "Ultron",
"Asgard", "Zendikar", "Mirrodin",
"Eldraine", "Theros", "Kamigawa",
"BaSingSe", "Dominiria", "Ravnica",
"Kobol", "Mobius", "Palpatine",
"Dameron", "Mustafar", "Rakdos",
"Selesnya", "Boros", "Izzet",
"Azouris", "Gruul", "Golgari",
"Dimir", "Orzhov", "Simic"]
numbers = string.digits
special_char = '!@#$%&?+'


def generate_password():

    pw_entry.delete(0, END)

    random_word = random.sample(list_of_words, 2)
    random_digits = random.sample(numbers, 3)
    random_special = random.sample(special_char, 2)
    random_pass = random_word + random_digits + random_special
    random.shuffle(random_pass)

    generated_pass = "".join(random_pass)
    # Copies generated password to clipboard for easy copy/paste
    pyperclip.copy(generated_pass)
    pw_entry.insert(END, generated_pass)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    user_website = web_entry.get().lower()
    user_email_name = email_user_entry.get()
    user_password = pw_entry.get()

    # json data format
    new_data = {
        user_website: {
        "email": user_email_name,
        "password": user_password,
        }
    }

    if len(user_password) <= 0 or len(user_email_name) <= 0 or len(user_website) <=0:
        messagebox.showinfo(title="Error!", message="Please do not leave any fields empty!")


    else:
        # messagebox is used to verify if user wants to save their password.
        # is_ok is a boolean vaiable. Clicking "OK" = True
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \nEmail: {user_email_name} \nPassword: {user_password}")

        if is_ok:
            try:
                with open("password_file.json", 'r') as file:
            
                    # .load() Reading the old data
                    data = json.load(file)

            except FileNotFoundError:
                    # If file doesnt't exist, new one is made and first json data is added.
                    with open("password_file.json", 'w') as file:
                        
                        # json.dump() is used to write the json file.
                        json.dump(new_data, file, indent=4)
                
            else:
                    # Since the file exists, the data must be updated before adding it to json file.
                    # .update() Updating data file with new information
                    data.update(new_data)
                    with open("password_file.json", 'w') as file:

                        # .dump() Saving the updated data to the file.
                        json.dump(data, file, indent=4)
            finally:
                    web_entry.delete(0, END)
                    pw_entry.delete(0, END)

    
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = web_entry.get().lower()
    try:
        with open("password_file.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data File Found!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            website = website.capitalize()
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        else:
             messagebox.showinfo(title="Error", message=f"No details for {website} exists!")


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

web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=1)

email_user_entry = Entry(width=35)
# email_user_entry.insert(0, "contactdanielmurillo@gmail.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=35)
pw_entry.grid(column=1, row=3, columnspan=2)


# Buttons:

generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(row=4, column=1)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)


# Mainloop:
window.mainloop()