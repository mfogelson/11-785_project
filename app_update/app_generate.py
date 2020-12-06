"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: v
import json

import requests
import streamlit as st

base_url = "http://127.0.0.1:8080"
generation_endpoint = "generate"


def app():
    st.title("Youshen Poetry Generator")
    st.write("Poems you'll love by a lovely AI. ")  # description
    # prompt for user input
    #text_prompt = "My grandfather's clock was too large for the shelf"
    text_prompt = ""
    user_input = st.text_input("Enter a word/sentence to generate your poem", text_prompt)
    if st.button("Generate a poem"):
        st.write("")
        '''if len(str(user_input)) > 0:
            st.write("Generating a poem given: " + str(user_input))
        else:
            st.write('No user input detected, we will surprise you')'''
        payload = dict()
        payload["user_input"] = str(user_input)
        payload = json.dumps(payload)
        response = requests.post(f"{base_url}/{generation_endpoint}", data=payload)
        data = response.json()
        output = "The most talented version of me is coming in a few days. Stay tuned! :wink:"
        output2 = "Meanwhile, be sure to check out \"Guess who wrote it\" and leave a comment!"
        if data["success"]:
            output = data["generated"]
            for line in output.split('\n'):
                st.subheader(line)
        else:
            st.subheader(output)
            st.subheader(output2)




