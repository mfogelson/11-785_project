"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare, Xinkai Chen
import json

import requests
import streamlit as st
import app_intro
import app_generate
import app_turing
import app_contact

st.set_page_config(page_title='Youshen: Your Poetry Generator', layout='centered', initial_sidebar_state='auto')
base_url = "http://127.0.0.1:8080"
generation_endpoint = "generate"
retrieval_endpoint = "retrieve"

PAGES = {
    "Introduction": app_intro,
    "Guess who wrote it": app_turing,
    "Let's write a poem (coming soon)": app_generate,
    "Leave a comment": app_contact
}
st.sidebar.title('Try me!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


# we don't need this for now
def app():
    pass
