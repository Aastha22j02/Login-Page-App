import streamlit as st

# Create a dictionary of username and password pairs
users = {"John": "1234", "Sarah": "5678", "Bob": "password"}
# Create the login page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    # Check if username and password are valid
    if login_button:
        if username in users and users[username] == password:
            st.success("Logged in as {}".format(username))
        else:
            st.error("Invalid username or password")
# Run the login page
if __name__ == '__main__':
    login()