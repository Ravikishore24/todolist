import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("length of the password you want to generate is: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if _name_ == "_main_":
    main()