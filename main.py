import streamlit as st
import pandas as pd

st.set_page_config(page_title='Channel Partner Orders', page_icon='🤝', layout="centered", initial_sidebar_state="auto", menu_items=None)


st.caption('VACAYZEN')
st.title('Channel Partner Orders')
st.info('Coorelating add-on orders to channel partner homes.')

partner_properties = st.file_uploader('Partner Properties','CSV')

if partner_properties:
    
    pp = pd.read_csv(partner_properties, index_col=False)

    partner_column = 'PARTNER'
    order_column   = 'ORDER #'

    if not 'PARTNER' in pp.columns: partner_column = st.selectbox('Partner Column', options=pp.columns)
    if not 'ORDER #' in pp.columns: order_column   = st.selectbox('Order Column',   options=pp.columns)

    ppdf = pp[[partner_column, order_column]].drop_duplicates()

    partners = st.multiselect('Partners to consider', options=ppdf[partner_column].sort_values().unique(), default=ppdf[partner_column].sort_values().unique())

    sppdf = ppdf[ppdf[partner_column].isin(partners)]

    sppdf