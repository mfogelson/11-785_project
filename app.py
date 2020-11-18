"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare, Xinkai Chen
import json

import requests
import streamlit as st
import app_generate
import app_turing

base_url = "http://127.0.0.1:8080"
generation_endpoint = "generate"
retrieval_endpoint = "retrieve"

PAGES = {
    "Let's write a poem": app_generate,
    "Guess who wrote it": app_turing
}
st.sidebar.title('Try me!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# we don't need this for now
def app():
    pass

    # if st.button("Generate a poem"):
    #     app_generate.generate()
    #     # payload = dict()
    #     # payload["user_input"] = str(user_input)
    #     # payload = json.dumps(payload)
    #     # response = requests.post(f"{base_url}/{generation_endpoint}", data=payload)
    #     # data = response.json()
    #     # output = "An error occured"
    #     # if data["success"]:
    #     #     output = data["payload"]
    #     # st.write(output)
    #
    # if st.button("Retrieve a limerick"):
    #     response = requests.post(f"{base_url}/{retrieval_endpoint}")
    #     data = response.json()
    #     output = "An error occured"
    #     if data["success"]:
    #         output = data["text"]
    #     st.write(output)


