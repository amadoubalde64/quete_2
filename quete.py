import streamlit as st
import pandas as pd
import seaborn as sns
data = sns.load_dataset("taxis")


# Titre
st.title("Bienvenue sur le site Web de")
st.header("AMADOU BALDE")

# Menu deroulant
ma_ville = st.selectbox("Indiquez votre point de récupération",
             ["Brooklyn", "Bronx", "Manhattan", "Queens", "Nan"])

if "Brooklyn" in ma_ville :
    st.write("Tu as choisi:",)
    st.image("https://www.new-york.fr/f/estados-unidos/nueva-york/guia/brooklyn.jpg")
if "Bronx" in ma_ville:
    st.write("Tu as choisi le Bronx")
    st.image("https://a.travel-assets.com/findyours-php/viewfinder/images/res70/471000/471807-Bronx.jpg")
if "Manhattan" in ma_ville:
    st.write("Tu as choisi Manhattan")
    st.image("https://www.new-york-city.fr/wp-content/uploads/2020/11/Manahttan_principale.jpg")
if "Queens" in ma_ville:
    st.write("Tu as choisi le Queens")
    st.image("https://i.ytimg.com/vi/UDUJV6s_LUY/maxresdefault.jpg")
if "Nan" in ma_ville:
    st.write("Tu as choisi le : nan")
    st.image("https://www.xalimasn.com/wp-content/uploads/2013/03/inconnu.jpg")
