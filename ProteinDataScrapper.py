import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

def ScrapeData():    
    url  = 'https://www.rcsb.org/stats/growth/growth-released-structures'
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_="header-left") 
    
    table_a1 = table.find(id="header-counts")
    
    
    DataSearching = table_a1.find_all('a')
    return DataSearching

def GetData():
    Data = ScrapeData()
    Structure   = Data[0].text
    ComputerStructure  = Data[1].text
    return [Structure,ComputerStructure]

def PDB_ShowData():
    Data = GetData()
    
    col1, col2= st.columns(2)
    col1.metric("Structures from the PDB", Data[0])
    col2.metric("Computed Structure Models (CSM)", Data[1])

st.header('3D Structure Database Informations')
st.sidebar.header('Select Databases')

with st.expander('About this app'):
    PDB_ShowData()

#Database Selection
noDatabase = True

PDB = st.sidebar.checkbox('PDB')
if PDB:
    noDatabase = False
    st.write('### PDB')
    PDB_ShowData()
     
Database2 = st.sidebar.checkbox('Database2')
if Database2:
    noDatabase = False
    st.write('### Database2')
    PDB_ShowData()

Database3 = st.sidebar.checkbox('Database3')
if Database3:
    noDatabase = False
    st.write('### Database3')
    PDB_ShowData()

Database4 = st.sidebar.checkbox('Database4')
if Database4:
    noDatabase = False
    st.write('### Database4')
    PDB_ShowData()

Database5 = st.sidebar.checkbox('Database5')
if Database5:
    noDatabase = False
    st.write('### Database5')
    PDB_ShowData()

Database6 = st.sidebar.checkbox('Database6')
if Database6:
    noDatabase = False
    st.write('### Database6')
    PDB_ShowData()

if noDatabase:
    st.write('Select Databases From Sidebar')
