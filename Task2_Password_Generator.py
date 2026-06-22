import random
import string

print("===== Password Generator =====")

length = int(input("Enter Total Password Length: "))

upper = int(input("Enter number of Uppercase Letters: "))
lower = int(input("Enter number of Lowercase Letters: "))
digits = int(input("Enter number of Digits: "))
special = int(input("Enter number of Special Characters: "))

if upper + lower + digits + special != length:
    print("\nError: Sum of all character types must be equal to password length!")
else:
    password = []

    # Uppercase letters
    for i in range(upper):
        password.append(random.choice(string.ascii_uppercase))

    # Lowercase letters
    for i in range(lower):
        password.append(random.choice(string.ascii_lowercase))

    # Digits
    for i in range(digits):
        password.append(random.choice(string.digits))

    # Special characters
    for i in range(special):
        password.append(random.choice(string.punctuation))

    # Shuffle password
    random.shuffle(password)

    # Convert list to string
    password = "".join(password)

    print("\nGenerated Password:", password)
    print("Password Length:", len(password))
