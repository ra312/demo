"""About page shown when the user enters the application"""
import streamlit as st


def write():
    """Used to write the about page in the app.py file"""
    st.title("Welcome to Awesome App")
    st.markdown(
        """
        A new way of life
""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    write()
