import streamlit as st
import requests, json

def displayEvents():
    st.sidebar.subheader("Filters")
    collection = st.sidebar.text_input("Collection")
    owner = st.sidebar.text_input("Owner")
    buy = st.sidebar.checkbox("Buy Now", value=False)
    params = {}
    if collection:
        params['collection_slug'] = collection
    if owner:
        params['owner'] = owner
    r = requests.get("https://testnets-api.opensea.io/api/v1/events", params=params)

    response = r.json()


    if response['asset_events']:
        for event in response['asset_events']:
            if event['asset']['name']:
                st.write(f"{event['asset']['name']} #{event['asset']['token_id']}")
            else:
                st.write(f"{event['asset']['collection']['name']} #{event['asset']['token_id']}")
            if event['asset']['image_url'].endswith('mp4') or event['asset']['image_url'].endswith('mov'):
                st.video(event['asset']['image_url'])
            elif event['asset']['image_url']:
                st.image(event['asset']['image_url'])
            st.write({event['event_type']})
            st.write({event['bid_amount']})

    st.write(r.json())
