from tkinter import *
from tkinter import messagebox

# main
root = Tk()
# window size
root.geometry("500x500")
# window background
root.config(bg="skyblue")
# name of application
root.title("Login Form")

# label and place
input_label1 = Label(root, text="Please enter username:") .place(x=5, y=5)
user_entry = Entry(root)
user_entry.place(x=180, y=5)

input_label2 = Label(root, text="Please enter password:") .place(x=5, y=50)
pass_entry = Entry(root, show="*")
pass_entry.place(x=180, y=50)

def check():
    username = ["Jeandre", "Justin", "Abdullah", "Jesse", "Thabo"]
    password = ["1234", "2345", "3456", "4567", "5678"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == password[x1]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS","Access granted")
        root.destroy()
        import newscreen
    else:
        messagebox.showinfo("ERROR INFO", "Access denied")


def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


def exit_program():
    root.destroy()


log_btn = Button(root, text="Login", borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=check)
log_btn.place(x=75, y=100)
clear_btn = Button(root, text="Clear", borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=clear)
clear_btn.place(x=200, y=100)
exit_btn = Button(root, text="Exit", command=exit_program, borderwidth="10", bg="Aqua", font=("Consolas 15 bold"))
exit_btn.place(x=325, y=100)


root.mainloop()
