import random
import string
import streamlit as st

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all pools
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Function to copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)

# Streamlit app
st.title("Random Password Generator")

# Input for password length and generate button in the same row
_, col1, _, col2, _ = st.columns(5)
with col1:
    length = st.number_input("Password length:", min_value=4, step=1, value=8, label_visibility="collapsed")
with col2:
    generate = st.button("Generate Password")

# Display the generated password
if generate:
    try:
        password = generate_password(length)
        st.text_input("Generated Password:", value=password, key="password", disabled=True)
    except ValueError as e:
        st.error(str(e))
