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

def PDB_CreateFrame():
    Data = GetData()
    
    col1, col2= st.columns(2)
    col1.metric("Structures from the PDB", Data[0])
    col2.metric("Computed Structure Models (CSM)", Data[1])

st.header('3D Structure Database Informations')

col1, col2= st.columns(2)
if col1.st.button('PDB Database'):
    PDB_CreateFrame()
if col2.st.button('yyyyy Database'):
    PDB_CreateFrame()
