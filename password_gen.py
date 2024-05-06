import random
import string

uppercase_letters=string.ascii_uppercase
lowercase_letter=string.ascii_lowercase
digits=string.digits
spl_char=string.punctuation
letters=string.ascii_letters

def generate_password(length, complexity):
    if complexity == 'low':
        characters = letters + digits
    elif complexity == 'medium':
        characters = letters + digits+spl_char
    elif complexity == 'high':
        characters = letters+digits+spl_char+uppercase_letters+lowercase_letter
    else:
        raise ValueError("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
    password = "".join(random.sample(characters,length) )
    return password

length=int(input("Enter the length of the password:"))
complexity = input("Enter the complexity level (low, medium, high): ").lower()

try:
    password = generate_password(length, complexity)
    print("Generated Password:", password)
except ValueError as err:
        print(err)
