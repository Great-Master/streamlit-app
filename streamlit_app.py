import streamlit as st

# Define the Streamlit app
def app():
    # Set the page title and favicon
    st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:")

    # Define the app layout
    st.write("Welcome to my app!")
    st.write("This is the home page.")
    name = st.text_input("Enter your name:")
    st.write(f"Hello, {name}!")

if __name__ == '__main__':
    app()
