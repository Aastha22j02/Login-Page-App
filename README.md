# Project Name: Streamlit Login Page

This project demonstrates how to create a simple login page using Streamlit.

## Project Description

The code creates a login page that prompts users for their username and password. It then checks if the provided username and password match the dictionary of predefined users. If the login credentials are valid, the user is logged in and a success message is displayed. Otherwise, an error message is displayed.

## How to Use

1. Clone the repository or download the code files.
2. Install the required libraries by running `pip install streamlit`.
3. Run the code by typing `streamlit run login_page.py` in the terminal.
4. The login page will open in your web browser.

## Code Description

The `login()` function creates the login page using Streamlit. It prompts the user for their username and password and checks if the entered credentials match the predefined list of users.

The `if __name__ == '__main__':` block ensures that the `login()` function is only run when the script is executed directly, rather than when it is imported as a module.

## Conclusion

This project demonstrates how to create a simple login page using Streamlit. With just a few lines of code, you can create a secure login system for your web application.