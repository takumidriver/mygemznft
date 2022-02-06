import streamlit as st
import requests, json

def displayNFTs():

    st.sidebar.subheader("Filters")
    collection = st.sidebar.text_input("Collection")
    owner = st.sidebar.text_input("Owner")
    buy = st.sidebar.checkbox("Buy Now", value=False)
    params = {}
    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner

    r = requests.get("https://testnets-api.opensea.io/api/v1/assets", params=params)

    response = r.json()

    for asset in response["assets"]:
        if asset['name']:
            st.write(f"{asset['name']} #{asset['token_id']}")
        else:
            st.write(f"{asset['collection']['name']} #{asset['token_id']}")
        if asset['image_url'].endswith('mp4') or asset['image_url'].endswith('mov'):
            st.video(asset['image_url'])
        elif asset['image_url']:
            st.image(asset['image_url'])

    st.write(r.json())
