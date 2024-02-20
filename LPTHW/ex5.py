# Exercise 5: More Variables and Printing
name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} yes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

total = age + height + weight
height_cm = height * 2.54
weight_kg = weight * 0.45 
print(f"If I add {age}, {height}, and {weight} I get {total}")
print(f"My height in cm is {height_cm}.")
print(f"My weight in kg is {weight_kg}.")