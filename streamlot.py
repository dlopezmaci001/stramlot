# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:53:11 2021

@author: danie
"""

import streamlit as st
import pandas as pd
from PIL import Image 
import streamlit as st

# =============================================================================
# Function creation
# =============================================================================
def is_authenticated(password):
    return password == st.secrets["DB_PASSWORD"]

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2

def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input('Password')

def get_df(file):
  # get extension and read file
  extension = file.name.split('.')[1]
  if extension.upper() == 'CSV':
    df = pd.read_csv(file)
  elif extension.upper() == 'XLSX':
    df = pd.read_excel(file, engine='openpyxl')
  elif extension.upper() == 'PICKLE':
    df = pd.read_pickle(file)
  return df

def main():
    st.image("https://erasmusintern.org/sites/default/files/styles/full_mediam/public/recruiter/logo/Nimerya%20Logo.png?itok=p3bSHht9")
    st.write('A general purpose data exploration app')
    variable = st.text_area('Input name of client')
    file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'
                                                 ,'pickle'])
    if not file:
        st.write("Upload a .csv or .xlsx file to get started")
        return
    df = get_df(file)
    print(df.head())

# =============================================================================
# Run app 
# =============================================================================

login_blocks = generate_login_block()
password = login(login_blocks)

if is_authenticated(password):
    clean_blocks(login_blocks)
    # st.secrets["DB_PASSWORD"]
    main()
elif password:
    st.info("Please enter a valid password")
