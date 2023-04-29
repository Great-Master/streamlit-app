import streamlit as st

import streamlit as st

# Define the app route
@app.route('/')
def index():
    return render_template('index.html', name='John')

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
    app.run(debug=True)
