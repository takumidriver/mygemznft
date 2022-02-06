import streamlit as st
import requests, json
from assets import *
from events import *

endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"mygemz // {endpoint}")

if endpoint == 'Assets':
    displayNFTs()
elif endpoint == 'Events':
    displayEvents()
