# to run,copy and paste the code below
# streamlit run eugenia.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/

import streamlit as st

title="Climate Crash"
st.title(title)

description="""
This is a game where you can experience saving the world by killing climate change. 
If you like being in the spotlight, this is the game just for you!
"""
st.write(description)


# Input field for user's name
# name = st.text_input("Enter your name:")

st.image("1.png")
