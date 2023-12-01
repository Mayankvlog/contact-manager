import streamlit as st
import sqlite3
import hashlib  # For password hashing

# Function to create the Contacts table
def create_contacts_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    );''')
    conn.commit()
    conn.close()

# Function to create the Users table
def create_users_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );''')
    conn.commit()
    conn.close()

# Function to insert a new user
def insert_user(username, password):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
    c.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

# Function to check login credentials
def check_login(username, password):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
    c.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    conn.close()
    return user

# Function to insert a new contact
def insert_contact(name, phone_number):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO Contacts (name, phone_number) VALUES (?, ?)", (name, phone_number))
    conn.commit()
    conn.close()

# Function to retrieve all contacts
def get_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT id, name, phone_number FROM Contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts

# Function to delete a contact by ID
def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM Contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

# Create Streamlit pages
st.set_page_config(page_title="Contact Manager", layout="wide")

# Add logo
logo_path = "Contact_manager.jpg"
st.image(logo_path, width=150)  # Adjust the width as needed

# Create Users table
create_users_table()

# Sign-up/Login page
page = st.sidebar.radio("Navigation", ["Sign Up", "Login"])

if page == "Sign Up":
    st.header("Sign Up")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password", key="signup")
    if st.button("Sign Up"):
        insert_user(new_username, new_password)
        st.success(f"User {new_username} signed up successfully. Please log in.")

elif page == "Login":
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password", key="login")
    if st.button("Login"):
        user = check_login(username, password)
        if user:
            st.success(f"Logged in as {username}.")
            create_contacts_table()  # Create Contacts table after login
            # Continue with the rest of your application
        else:
            st.error("Invalid username or password.")
