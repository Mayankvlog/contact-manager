import streamlit as st
import sqlite3

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

st.title("Contact Number Manager")

page = st.sidebar.radio("Navigation", ["Add Contact", "View Contacts"])

if page == "Add Contact":
    create_contacts_table()

    st.header("Add a New Contact")
    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    if st.button("Add Contact"):
        insert_contact(name, phone_number)
        st.success(f"Added {name} to contacts.")

elif page == "View Contacts":
    st.header("Contacts List")
    contacts = get_contacts()
    for contact in contacts:
        st.write(f"Name: {contact[1]}, Phone Number: {contact[2]}")
        if st.button(f"Delete {contact[1]}"):
            delete_contact(contact[0])

