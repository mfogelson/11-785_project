"""The :mod:`streamlit_app` serves as a demo application to show the poetry generation API system at work.
This runs on sreamlit
"""
# Author: Xinkai Chen

import requests
import streamlit as st
import SessionState
import datetime
import emails


def app():
    st.title("Youshen Poetry Generator")
    st.write("Hi there! This is a friendly AI who loves poetry.")  # description
    #st.subheader("<font color='blue'>Test your</font>")
    st.header("Please help us evaluate our AI Poem Generator")
    st.header("By playing \"Guess who wrote it\" :question:") 
    st.header("Feel free to leave a comment! :writing_hand:")
    st.subheader("")
    st.subheader("Team Members")
    st.write("[Mitchell B. Fogelson](mailto:mfogelso@andrew.cmu.edu), [Qifei Dong](mailto:qifeid@andrew.cmu.edu), "
             "[Christopher Dare](mailto:cdare@andrew.cmu.edu), [Xinkai Chen](https://www.linkedin.com/in/xinkai-chen/)")
    st.write(":office: Carnegie Mellon University")
    st.write(":round_pushpin: Pittsburgh, PA 15213 :heavy_plus_sign: BP 6150, Kigali, Rwanda")
    st.subheader("Description")
    st.write("This project was a course project for [Introduction to Deep Learning](http://deeplearning.cs.cmu.edu/) course at CMU Fall 2020.\n\nThe goal of this project was to create a novel poetry generation Deep Learning Model.")
    st.subheader("Constraints")
    st.write("We decided to constrain the problem to the poetry form of [Limericks](https://en.wikipedia.org/wiki/Limerick_(poetry)).")
    st.write("Limericks are rhyming poems of the form:\n\n:a:\n\n:a:\n\n:b:\n\n:b:\n\n:a:")
    st.subheader("Model Architecture")
    st.write("We used the [GPT2 117M](https://github.com/nshepperd/gpt-2) architecture based off the code from [nshepperd](https://github.com/nshepperd)")
    st.write("We trained on-top of a pretrained model that learned from general poetry by [Gwern](https://www.gwern.net/GPT-2)")
    st.subheader("Dataset")
    st.write("We used a corpus of [~90,000 Limericks](https://raw.githubusercontent.com/sballas8/PoetRNN/master/data/limericks.csv) thanks to [sballas8](https://github.com/sballas8)")
    st.subheader("Preprocessing")
    st.write(":white_medium_small_square: We removed all punctuation\n\n:white_medium_small_square: We converted all numbers to text\n\n:white_medium_small_square: We removed all poems that did not conform to the structure above\n\n:white_medium_small_square: We added <|endoftext|> token to end of each poem")
    st.subheader("Evaluation Metrics")
    st.write(":white_medium_small_square: We implemented a Rhyming evaluation\n\n:white_medium_small_square: We implemented a Coreference evaluation\n\n:white_medium_small_square: We implemented a Nonsense word evaluation\n\n:white_medium_small_square: We also set up this website where we had human's evaluate poems generated from our model vs. from the training dataset. This is the best way we can evaluate the success of our system")
    st.subheader("Downsampling")
    st.write("From 8000 unconditionally generated poems 1000 were scored well enough to pass the 3 metrics described above and used for user testing.")
    #st.subheader("Source Code")
    #st.write("Check out our [Github](https://github.com/mfogelson/11-785_project)")
    #st.subheader("Video")
    #st.video("https://youtu.be/8ypnLjwpzK8")
    #st.subheader("References")
    #st.write("[Gwern's GPT-2 Tutorial](https://www.gwern.net/GPT-2)")
    '''
    st.subheader("Contact Us")
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    comment = st.text_input("Tell us what you think", "")
    if st.button("Submit"):
        if '@' not in email and len(email) > 0:
            st.write('Please input a valid email address! We would love to get back to you.')
        #elif len(name) == 0:
        #    st.write('Please give us a name! Nicknames are fine!')
        elif len(comment) == 0:
            st.write('Please input a valid comment. Anything is appreciated!')
        else:
        #message = emails.Message(text="<p>{0}</p>".format(comment), subject="Comment from {0}".format(name), mail_from=(name, email))
        #r = message.send(to='xinkaichen97@gmail.com', smtp={'host': 'smtp.gmail.com', 'timeout': 10, 'port': 465})
        #print(r.status_code, flush=True)
            with open('comments.txt', 'a') as f:
                f.write("Name: {0}, Email: {1}, Comment: {2}, Timestamp: {3}\n".format(name, email, comment, datetime.datetime.now()))
            st.write("Thanks {0}! Your feedback is highly appreciated.".format(name))'''
    #st.subheader("Source Code")
    #st.write("Check out our [Github](https://github.com/mfogelson/11-785_project)")
    st.subheader("Key Resources")
    st.write("[Gwern's Blog: Poetry Learning with GPT2](https://www.gwern.net/GPT-2)")
    st.write("[Nshepperd/gpt-2 Github](https://github.com/nshepperd/gpt-2)")
    st.write("[Cole Peterson Master's Thesis](https://dspace.library.uvic.ca/bitstream/handle/1828/10801/Peterson_Cole_MSc_2019.pdf?sequence=3&isAllowed=y#Hfootnote.12)")
    st.write("[Ng Wai Foong's Medium Article](https://medium.com/ai-innovation/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f)")
    
