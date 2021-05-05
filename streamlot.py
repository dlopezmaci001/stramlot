# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:53:11 2021

@author: danie
"""

import streamlit as st
import pandas as pd
from PIL import Image 
import streamlit as st
from test import print_me
import pyodbc
from fast_to_sql import fast_to_sql as fts
# =============================================================================
# Function creation
# =============================================================================
def fast_server_nimerya(database_name,df,tablename,if_exists):

    """ 
    Parameters
    ----------
    database_name : TYPE
       Add the name of the database you want to upload the df to.
    df : TYPE
       dataframe you want to upload to sql server
    tablename : TYPE
        Name of the table to upload to sql server.
    if_exists : TYPE
       If the table already exists "append".
       If the table has to be deleted "replace".
       
   Important information
   ---------------------
   .to_sql will create the table in the SQL server, therefore the column names of
    the dataframe will be the same column names you will have in the database. 

    """       
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+st.secrets["DB_SERVER"]+
                                     ';DATABASE='+database_name+
                                     ';UID='+st.secrets["DB_USERNAME"]+
                                     ';PWD='+ st.secrets["DB_PASSWORD"])
    
    # =============================================================================
    # Upload de dataframe  
    # =============================================================================
    create_statement  = fts.fast_to_sql(df,tablename, conn, if_exists = if_exists) 
    
    # Commit upload actions and close connection
    conn.commit()
    conn.close()
    
    
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
  return df

def main():
    st.image("data:image/png;base64,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",use_column_width = True)
    st.title('Explore a dataset')
    st.title(print_me())
    # Side bar 
    st.sidebar.header("Elija su opcion")
    task = st.sidebar.radio('Task', ['Alta Usuarios', 'Maestro'], 0)
    if task == 'Alta Usuarios':
        st.write('A general purpose data exploration app')
        st.write(st.secrets["DB_PASSWORD"])
        variable = st.text_area('Input name of client')
        file = st.file_uploader("Upload file", type=['csv' 
                                                     ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        df = get_df(file)
        
        fast_server_nimerya(df,st.secrets["DB_USER"],"sectionaccess_bimbo_prueba",'append')
        
    else:
        st.write("esto para otra cosa")
    
    
# =============================================================================
# Run app 
# =============================================================================

main()
