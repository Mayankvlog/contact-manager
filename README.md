#   contact-manager

This Streamlit application permits clients to oversee contacts through a straightforward point of interaction. 

It involves SQLite for information capacity, including a 'Contacts' table for contact subtleties and a 'Clients' 
table for client qualifications, which are hashed for security. 

On startup, it checks and makes these tables in the event that they don't exist. Clients can join and sign in; the application
hashes passwords for capacity and confirms login qualifications. Upon fruitful login, clients can oversee contacts — adding, recovering, or erasing them. 

The application includes a sidebar for route between join and login pages. It likewise shows a logo at the top and changes the design for a wide screen.
streamlit run main.py
