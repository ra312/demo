# Main page for streamlit resume
import streamlit as st
import about
import resources.ast as ast
from resources import login
import streamlit_authenticator as stauth


def main():
    """Main function of App"""

    authenticator = login.return_authentication_status()
    (name, authentication_status, username) = authenticator.login(
        'Login', 'main')
    auth_status = st.session_state["authentication_status"]
    if auth_status:
        authenticator.logout('Logout', 'main')
        ast.write_page(about)
    elif auth_status is False:
        st.error('Username/password is incorrect')
    elif auth_status is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    main()
