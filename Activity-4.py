import string

UserName = input("Enter your full name (First, Middle, Last): ")

parts = [part.strip() for part in UserName.split(",")]

if len(parts) == 3:
    first = parts[0].capitalize()
    middle = parts[1].capitalize()
    last = parts[2].title()
    middle_initial = middle[0] + "."
    formatted = f"{last}, {first} {middle_initial}"
    print(f"Formatted Name: {formatted}")
else:
    print("Invalid input format. Please enter: First, Middle, Last")