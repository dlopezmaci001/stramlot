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
    st.image("data:image/jpeg;base64,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")
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
