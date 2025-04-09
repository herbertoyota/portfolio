import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import investpy as inv
import seaborn as sns

def home():
    col1,col2,col3 = st.columns(3)
    with col2:
        st.title('App Financeiro')
        st.markdown('---')

def panorama():
    st.title('Panorama de Mercado')
    st.markdown(date.today(),strftime('%d/%m/%Y'))

    st.subheader('Mercados pelo Mundo')

    dict_tickers = {'Bovespa:^BVSP'}
              
    df_info = pd.DataFrame('Ativo':dict_tickers.keys(),'Ticker':dict_tickers.values())
    st.write(df_info)

def mapa_mensal():
    st.title('Mapa Mensal')

def fundamentos():
    st.title('Fundamentos')

def main():
    st.sidebar('Projeto Financeiro')
    st.siderbar.markdown('---')
    lista_menu = ['Home','Panorama de Mercado','Rentabilidade Mensal','Fundamentos']
    escolha = st.sidebar.radio('Escolha a opção')

    if escolha == 'Home':
        home()
    if escolha == 'Panorama de Mercado':
        panorama()
    if escolha == 'Rentabilidade Mensal':
        mapa_mensal()
    if escolha == 'Fundamentos':
        fundamentos()