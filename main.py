import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def gram_to_mg(grams):
    return grams * 1000

def mg_to_gram(mg):
    return mg * 0.001

def gold_rate(value):
    return value / 10

def gold_material_cost(total_weight_in_gram, price_rate):
    return total_weight_in_gram * price_rate

def gold_making_charge(total_weight_in_gram, mc_input):
    return total_weight_in_gram * mc_input

def calculate_gold_price():
    grams_value = grams_entry.get()
    mgs_value = mgs_entry.get()
    mc_input = mc_entry.get()
    price_input = price_entry.get()

    # Check if any input field is empty
    if not grams_value or not mgs_value or not mc_input or not price_input:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    try:
        grams_value = float(grams_value)
        mgs_value = float(mgs_value)
        mc_input = float(mc_input)
        price_input = float(price_input)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        return

    total_mg = gram_to_mg(grams_value) + mgs_value
    total_weight_in_gram = mg_to_gram(total_mg)

    material_price = total_weight_in_gram * gold_rate(price_input)
    gst_value = int(material_price * 0.03)
    making_price = gold_making_charge(total_weight_in_gram, mc_input)

    total_price = material_price + gst_value + making_price

    result_label.config(text="Total price: ₹ {:.2f}".format(total_price))
    result_label_without_gst.config(text="Total price (without 3% GST): ₹ {:.2f}".format(total_price - gst_value))

def refresh_inputs():
    grams_entry.delete(0, tk.END)
    mgs_entry.delete(0, tk.END)
    mc_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    result_label.config(text="")
    result_label_without_gst.config(text="")

# Create the main application window
root = tk.Tk()
root.title("Gold Price Calculator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Light gray background

# Create input labels and entry fields side by side using place
intro_label = ttk.Label(root, text="***Enter the Gold Values Accordingly***", font=("Stencil Std",12,"bold"))
intro_label.place(x=118, y=20)

grams_label = ttk.Label(root, text="Grams:", font=("Arial", 14))
grams_label.place(x=40, y=50)

grams_entry = ttk.Entry(root, font=("Arial", 14),width=12)
grams_entry.place(x=40, y=80)

mgs_label = ttk.Label(root, text="Milligrams:", font=("Arial", 14))
mgs_label.place(x=260, y=50)

mgs_entry = ttk.Entry(root, font=("Arial", 14),width=12)
mgs_entry.place(x=260, y=80)

mc_label = ttk.Label(root, text="Making Charge (for 1 gram):", font=("Arial", 14))
mc_label.place(x=40, y=120)

mc_entry = ttk.Entry(root, font=("Arial", 14),width=23)
mc_entry.place(x=40, y=150)

price_label = ttk.Label(root, text="Rate of Gold (INR):", font=("Arial", 14))
price_label.place(x=40, y=200)

price_entry = ttk.Entry(root, font=("Arial", 14),width=16)
price_entry.place(x=220, y=200)

# Create a button to calculate the total price
calculate_button = tk.Button(root, text="Calculate", command=calculate_gold_price,bg='orange',fg='white',font=12)
calculate_button.place(x=100, y=250,width=250,height=30)

# Create labels to display the results with relief sunken
result_label = ttk.Label(root, text="", font=("Arial", 16), relief="sunken")
result_label.place(x=40, y=300, width=420)

result_label_without_gst = ttk.Label(root, text="", font=("Arial", 16), relief="sunken")
result_label_without_gst.place(x=40, y=350, width=420)

# Create a "Refresh" button to clear inputs
refresh_button = tk.Button(root, text="Refresh", command=refresh_inputs,font=12,bg='red',fg='white')
refresh_button.place(x=100,y=420,width=250,height=30)

# Start the Tkinter event loop
root.mainloop()
