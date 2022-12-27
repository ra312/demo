import streamlit as st
import yaml
from yaml import SafeLoader
import streamlit_authenticator as stauth


def return_authentication_status():
    with open('resources/accounts.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    # (
    # name, authentication_status, username) = authenticator.login(
    # 'Login', 'main')
    return authenticator
