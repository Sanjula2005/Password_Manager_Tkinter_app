from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {mail}"
    
                                                 f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("mydata.txt","a") as data_file:
                data_file.write(f"{website}|{mail}|{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,16))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Mansger")
window.config(padx=50,pady=60,bg="white")

canvas=Canvas(width=200,height=200,highlightthickness=0,bg="white")
pic=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pic)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:",bg="white",font=("courier",10))
website_label.grid(column=0,row=1)

website_entry=Entry(width=45)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

mail_label=Label(text="Email/Username:",bg="white",font=("courier",10))
mail_label.grid(column=0,row=2)

mail_entry=Entry(width=45)
mail_entry.grid(column=1,row=2,columnspan=2)
mail_entry.insert(0,"sanjulasudhindra12@gmail.com")


password_label=Label(text="password:",bg="white",font=("courier",10))
password_label.grid(column=0,row=3)

password_entry=Entry(width=27)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate password",highlightthickness=0,command=password_generator)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",highlightthickness=0,width=39,command=save)
add_button.grid(column=1,row=4,columnspan=2)








window.mainloop()