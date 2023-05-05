from tkinter import *


root = Tk()
root.title("All-You-Can-Eat Sushi")

menu_items = ["California Roll ($5)", "Spicy Tuna Roll ($6)", "Salmon Nigiri ($3)", "Tuna Sashimi ($8)"]
menu_lb = Listbox(root, height=4, width=20)
for item in menu_items:
    menu_lb.insert(END, item)
menu_lb.grid(row=0, column=0, padx=10, pady=10)
selected_items = []
def add_item():
    selected_item = menu_lb.get(ANCHOR)
    selected_items.append(selected_item)
    cart_lb.insert(END, selected_item)
    total = sum([float(item.split("($")[1].split(")")[0]) for item in selected_items])
    total_lbl.config(text="Total: $%.2f" % total)
add_btn = Button(root, text="Add >>", command=add_item)
add_btn.grid(row=1, column=0, padx=10)


cart_lb = Listbox(root, height=4, width=20)
cart_lb.grid(row=0, column=1, padx=10, pady=10)
def checkout():

    pass
checkout_btn = Button(root, text="Checkout", command=checkout)
checkout_btn.grid(row=1, column=1)


total_lbl = Label(root, text="Total: $0.00")
total_lbl.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
