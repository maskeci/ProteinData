import streamlit as st
import pandas as pd
from PDB_scraper import GetData as GetPDB
from EMBL_scrapper import GetData as GetEMBL
from SwissProt_scrapper import GetData as GetSwiss

st.header('3D Structure Database Informations')
st.sidebar.header('Select Databases') #Headers

def PDB_ShowData():
    DataPDB = GetPDB()
    
    col1, col2= st.columns(2)
    col1.metric("Structures from the PDB", DataPDB[0])
    col2.metric("Computed Structure Models (CSM)", DataPDB[1])

def EMBL_ShowData():
    DataEMBL = GetEMBL()

    st.write(DataEMBL)

def Swiss_ShowData():
    DataSwiss = GetSwiss()

    st.write(DataSwiss)

#Database Selection
noDatabase = True

PDB = st.sidebar.checkbox('PDB')
if PDB:
    noDatabase = False
    st.write('### PDB')
    PDB_ShowData()
     
Database2 = st.sidebar.checkbox(' UniProtKB/TrEMBL Protein Database')
if Database2:
    noDatabase = False
    st.write('###  UniProtKB/TrEMBL Protein Database')
    EMBL_ShowData()
    

Database3 = st.sidebar.checkbox('UniProtKB/Swiss-Prot Protein Knowledgebase')
if Database3:
    noDatabase = False
    st.write('### UniProtKB/Swiss-Prot Protein Knowledgebase')
    Swiss_ShowData()

if noDatabase:
    st.write('Select Databases From Sidebar')
