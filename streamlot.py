# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:53:11 2021

@author: danie
"""

import streamlit as st
import os 

def is_authenticated(password):
    os.environ['DB_PASSWORD']


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


def main():
    st.header('Hello')
    st.balloons()


login_blocks = generate_login_block()
password = login(login_blocks)

if is_authenticated(password):
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Please enter a valid password")
