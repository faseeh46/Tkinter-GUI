from tkinter import *
from random import choice,randint,shuffle
import pyperclip
from tkinter import messagebox
import json



def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error Message", message="OOppss!! See Your Credentials Again Something is Missing")
    else:
        try:
            with open("file.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
                with open("file.json" , "w") as file:
                 json.dump(new_data,file, indent=4)
        else:
            data.update(new_data)

            with open("file.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website= website_entry.get()
    try:
        with open ("file.json") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showerror(title="No Directory", message="No Data File Found\n Create Some Data File or\n Enter Data First")
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email = {email}\n Password = {password}")
    else:
        messagebox.showerror(title="ERROR", message=f"No Data Found related to {website}")

def generate_passwordd():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0 , password)
    pyperclip.copy(password)
window = Tk()
window.title("Password Generator & Saver")
#window.minsize(height = 400 , width = 400)
window.config(padx=30, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo)
canvas.grid(row = 0, column = 1)


website_label = Label(text="Website:")
website_label.grid(row = 1 , column = 0)
email_label = Label(text="Email/Username:")
email_label.grid(row = 2 , column = 0)
website_label = Label(text="Password:")
website_label.grid(row = 3 , column = 0)

website_entry = Entry(width=32)
website_entry.grid(row=1 , column = 1 )

search_button= Button(text="Search" , width=14 , command=find_password)
search_button.grid (row = 1, column =2 )
email_entry = Entry(width=50)
email_entry.grid(row=2 , column = 1,columnspan =2)
password_entry = Entry(width=32 )
password_entry.grid(row=3 , column = 1 )

generate_password = Button(text="Generate Password",width = 14 ,command = generate_passwordd)
generate_password.grid(row=3 , column = 2 )
add_button= Button(text="Add", width = 42 , command = save_data)
add_button.grid(row = 4, column = 1,columnspan =2)








window.mainloop()