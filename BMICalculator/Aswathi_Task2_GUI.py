import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category, color = "Underweight", "orange"
        elif bmi < 25:
            category, color = "Normal", "green"
        elif bmi < 30:
            category, color = "Overweight", "blue"
        else:
            category, color = "Obese", "red"

        result_label.config(text=f"Your BMI is {bmi:.2f} ({category})", fg=color)
    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="red")

def reset_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

# Window setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.configure(bg="lightgray")

# Weight input
tk.Label(root, text="Weight (kg)", fg="black", bg="lightgray", font=("Arial", 12)).pack(pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height input
tk.Label(root, text="Height (cm)", fg="black", bg="lightgray", font=("Arial", 12)).pack(pady=5)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="navy", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="Reset", command=reset_fields, bg="darkred", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="lightgray")
result_label.pack(pady=10)

root.mainloop()
