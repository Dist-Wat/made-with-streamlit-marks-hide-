# importing
import streamlit as st 

# main 
hide_st_mark = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_mark, unsafe_allow_html=True)
