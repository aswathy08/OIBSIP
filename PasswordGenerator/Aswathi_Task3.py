import random
import string

def password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1

    # Variety check
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # Final rating
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def password_generator():
    try:
        length = int(input("Enter password length: "))

        # User preferences
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Build pool
        characters = ""
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if digits:
            characters += string.digits
        if symbols:
            characters += string.punctuation

        if not characters:
            print("You must select at least one character type!")
            return

        # Guarantee at least one from each chosen type
        password = []
        if uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if lowercase:
            password.append(random.choice(string.ascii_lowercase))
        if digits:
            password.append(random.choice(string.digits))
        if symbols:
            password.append(random.choice(string.punctuation))

        # Fill rest
        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)
        final_password = ''.join(password)

        # Output
        print("Generated Password:", final_password)
        print("Strength:", password_strength(final_password))

    except ValueError:
        print("Invalid input! Please enter a number.")

# Run
password_generator()

