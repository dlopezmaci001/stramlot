# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:53:11 2021

@author: danie
"""

import streamlit as st
import os 

import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["DB_PASSWORD"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os
st.write("Has environment variables been set:",
os.environ["db_username"] == st.secrets["db_username"]
)
