from tkinter import *
from tkinter import messagebox
# main
root = Tk()
# window size
root.geometry("350x250")
# window title
root.title("Username and Password List")
# window background
root.config(bg="Yellow")

# labels
list_label = Label(root, text="List:", bg="red", font=("Consolas 12 bold"))
list_label.place(x=150, y=5)
number_label = Label(root, text="42, 12, 13, 89, 63, 11", bg="red", font=("Consolas 12 bold"))
number_label.place(x=60, y=50)
arr = [42, 12, 13, 89, 63, 11]

# quick sort function
def quick_sort(username_password):
    length = len(username_password)
    if length <= 1:
        return username_password
    else:
        pivot = username_password.pop()

    items_greater = []
    items_lower = []

    for item in username_password:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def result():
    messagebox.showinfo("sorted into", quick_sort(arr))

sortbtn = Button(root, text="Show Sorted List", command=result, borderwidth="10", font=("Consolas 15 bold"), bg="red")
sortbtn.place(x=50, y=100)

root.mainloop()
