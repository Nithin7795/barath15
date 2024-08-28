import random
import string

# Function to generate password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Main function
def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
