"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare
import json

import requests
import streamlit as st

base_url = "http://127.0.0.1:8080"
generation_endpoint = "generate"

st.title("Youshen Poetry Generator")
st.write("Poems you'll love by a friendly AI. ")  # description

text_prompt = "My grandfather's clock was too large for the shelf"
user_input = st.text_input("Starter text", text_prompt)

if st.button("Generate Poem"):
    payload = dict()
    payload["user_input"] = str(user_input)

    payload = json.dumps(payload)
    st.write("Posting")
    st.write(payload)
    response = requests.post(f"{base_url}/{generation_endpoint}", data=payload)
    data = response.json()
    output = "An error occured"
    if data["success"]:
        output = data["payload"]
    st.title(output)
