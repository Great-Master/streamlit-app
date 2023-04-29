import streamlit as st

# Define the Streamlit app
def main():
    # Read the contents of the HTML file
    with open("index.html", "r") as f:
        page = f.read()
    
    # Define the app layout
    st.write("Welcome to my app!")
    st.write("This is the home page.")
    name = st.text_input("Enter your name:")
    st.write(f"Hello, {name}!")

    # Display the contents of the HTML file on Streamlit
    st.write(page, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
