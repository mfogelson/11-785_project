
import requests
import streamlit as st
import SessionState
import datetime
import emails

def app():
    st.title("Youshen Poetry Generator")
    st.write("I'm not perfect. Wanna tell me how to improve?")
    st.subheader("Contact Us")
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    comment = st.text_input("Tell us what you think", "")
    if len(name) == 0:
        name = 'Anonymous'
    if st.button("Submit"):
        if '@' not in email and len(email) > 0:
            st.write('Please input a valid email address! We would love to get back to you')
        elif len(comment) == 0:
            st.write('Please input a valid comment. Anything is appreciated!')
        else:                                                                    #message = emails.Message(text="<p>{0}</p>".format(comment), subject="Comment from {0}".format(name), mail_from=(name, email))                                                                                                                  #r = message.send(to='xinkaichen97@gmail.com', smtp={'host': 'smtp.gmail.com', 'timeout': 10, 'port': 465})
             
            #print(r.status_code, flush=True)
            with open('comments.txt', 'a') as f:
                f.write("Name: {0}, Email: {1}, Comment: {2}, Timestamp: {3}\n".format(name, email, comment, datetime.datetime.now()))
                st.write("Thanks {0}! Your feedback is highly appreciated.".format(name))
