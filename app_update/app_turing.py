"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: Xinkai Chen

import requests
import streamlit as st
import SessionState
import datetime

base_url = "http://127.0.0.1:8080"
retrieval_endpoint = "retrieve"


def app():
    st.title("Youshen Poetry Generator")
    st.write("Challenge yourself!")  # description
    session_state = SessionState.get(name="", button_sent=False, data="")

    if st.button("Give me a poem"):
        session_state.button_sent = True
        # select poems and keep data in session_state so it's not refreshed when guessing
        response = requests.post(f"{base_url}/{retrieval_endpoint}")
        data = response.json()
        session_state.data = data

    if session_state.button_sent:
        # retrive data from session_state
        data = session_state.data
        if data["success"]:
            text1 = data["text1"]
            #text2 = data["text2"]
            ground_truth = data["ground_truth"]
            #human_text_idx = data["human_text_idx"]
            #model_text_idx = data["model_text_idx"]
            text_index = data["text_idx"]
            st.subheader("Poem")
            #for line in text1.split('\n'):
            #    st.write('{0}                       {1}'.format(line, line))
            #    st.write(line + '\t\t\t\t' + line)
            #for line in text1.split('\n'):
            #    st.write(line)
            #st.subheader("Poem 2")
            st.write(text1)
            st.subheader("Guess it is written by a human or the AI :question:")
            if st.button("Human"):
                if ground_truth == "human":
                    st.write("Okay you are right! We did not fool you this time! :thumbsup:")
                else:
                    st.write("It is a machine-generated poem! We got you! :sunglasses:")
                with open('user_guesses.txt', 'a') as f:
                    f.write("text_idx: {0}, guess: {1}, ground_truth: {2}, timestamp: {3}\n".format(
                        str(text_index), "human", ground_truth, datetime.datetime.now()))

            if st.button("AI"):
                if ground_truth == "model":
                    st.write("Okay you are right! We did not fool you this time! :thumbsup:")
                else:
                    st.write("It is actually a human-generated poem! Thanks for believing in our lovely AI! :heart:")
                with open('user_guesses.txt', 'a') as f:
                    f.write(
                        "text_idx: {0}, guess: {1}, ground_truth: {2}, timestamp: {3}\n".format(
                            str(text_index), "model", ground_truth, datetime.datetime.now()))
