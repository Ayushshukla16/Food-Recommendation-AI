import tkinter as tk
from tkinter import ttk
import random

# ------------------ DATA ------------------
food_data = {
    ("Veg", "Breakfast"): [
        "Poha", "Upma", "Idli", "Dosa", "Paratha", "Sandwich",
        "Aloo Toast", "Pancakes", "Cornflakes", "Fruit Salad"
    ],
    ("Veg", "Lunch"): [
        "Paneer Butter Masala", "Rajma Chawal", "Chole Bhature",
        "Veg Pulao", "Dal Rice", "Kadhi Chawal", "Mix Veg",
        "Palak Paneer", "Jeera Rice"
    ],
    ("Veg", "Dinner"): [
        "Veg Biryani", "Khichdi", "Soup", "Chapati Sabzi",
        "Paneer Tikka", "Mushroom Curry", "Veg Fried Rice"
    ],

    ("Non-Veg", "Breakfast"): [
        "Omelette", "Boiled Eggs", "Egg Sandwich",
        "Chicken Sausage", "Scrambled Eggs"
    ],
    ("Non-Veg", "Lunch"): [
        "Chicken Curry", "Fish Fry", "Egg Curry",
        "Chicken Biryani", "Mutton Curry",
        "Chicken Korma", "Grilled Chicken"
    ],
    ("Non-Veg", "Dinner"): [
        "Butter Chicken", "Chicken Biryani", "Fish Curry",
        "Egg Bhurji", "Tandoori Chicken",
        "Chicken Tikka", "Prawn Curry"
    ]
}

mood_food = {
    "Happy": [
        "Ice Cream", "Pizza", "Cake", "Brownie",
        "Donuts", "Milkshake"
    ],
    "Sad": [
        "Chocolate", "Burger", "Fries", "Pasta",
        "Garlic Bread", "Cheesy Nachos"
    ],
    "Stressed": [
        "Coffee", "Tea", "Maggi", "Dark Chocolate",
        "Green Tea", "Soup"
    ],
    "Lazy": [
        "Sandwich", "Instant Noodles", "Wrap",
        "Toast", "Ready-to-eat Meal"
    ]
}


def recommend_food():
    result_label.config(text="⏳ Thinking...")
    root.after(800, show_result)

def show_result():
    diet = diet_var.get()
    meal = meal_var.get()
    mood = mood_var.get()

    suggestions = []

    if (diet, meal) in food_data:
        suggestions.extend(food_data[(diet, meal)])

    if mood in mood_food:
        suggestions.extend(mood_food[mood])

    if suggestions:
        result = random.choice(suggestions)
        type_text(f"🍽️ Try: {result}")
    else:
        type_text("No suggestion 😅")

def type_text(text, i=0):
    if i <= len(text):
        result_label.config(text=text[:i])
        root.after(30, lambda: type_text(text, i+1))

# ------------------ MOVING BACKGROUND ------------------

particles = []

def create_particles():
    for _ in range(25):
        x = random.randint(0, 520)
        y = random.randint(0, 520)
        size = random.randint(2, 6)
        speed = random.uniform(0.5, 2)

        p = canvas.create_oval(x, y, x+size, y+size, fill="#38bdf8", outline="")
        particles.append([p, speed])

def animate_particles():
    for p, speed in particles:
        canvas.move(p, 0, speed)

        pos = canvas.coords(p)
        if pos[1] > 520:
            canvas.coords(p, random.randint(0, 520), 0,
                          random.randint(0, 520)+5, 5)

    root.after(30, animate_particles)

# ------------------ UI ------------------
root = tk.Tk()
root.title("Food Recommender")
root.geometry("520x520")
root.resizable(False, False)

# Canvas Background
canvas = tk.Canvas(root, width=520, height=520, bg="#0f172a", highlightthickness=0)
canvas.place(x=0, y=0)

create_particles()
animate_particles()

# Floating Frame (Glass effect)
frame = tk.Frame(root, bg="#1e293b")
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)

# Title
tk.Label(frame, text="🍔 Food Recommender",
         font=("Segoe UI", 16, "bold"),
         bg="#1e293b", fg="#38bdf8").pack(pady=10)

# Dropdown function
def dropdown(label, values):
    tk.Label(frame, text=label, bg="#1e293b", fg="white").pack(pady=5)
    var = tk.StringVar()
    box = ttk.Combobox(frame, textvariable=var, state="readonly")
    box['values'] = values
    box.current(0)
    box.pack(ipady=4)
    return var

diet_var = dropdown("Diet", ("Veg", "Non-Veg"))
meal_var = dropdown("Meal", ("Breakfast", "Lunch", "Dinner"))
mood_var = dropdown("Mood", ("Happy", "Sad", "Stressed", "Lazy"))

# Button
btn = tk.Button(frame, text="✨ Recommend",
                bg="#38bdf8", fg="black",
                font=("Segoe UI", 11, "bold"),
                command=recommend_food)
btn.pack(pady=15)

# Result
result_label = tk.Label(frame, text="",
                        font=("Segoe UI", 12, "bold"),
                        bg="#0f172a", fg="#22c55e",
                        height=3)
result_label.pack(pady=10, fill="x", padx=10)

# Run
root.mainloop()