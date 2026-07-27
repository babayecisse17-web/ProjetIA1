import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
from pandas import read_csv
import pandas as pd

st.sidebar.title("Statistique descriptive")

menu = st.sidebar.selectbox(
    "Navigation :",
    ["Accueil", "Analyse descriptive", "Visualisation", "Rapport"]
)


try:
    data = read_csv("housing.csv")
except Exception as e:
    st.write(e)

st.markdown(
    """
    <div style='text-align:center'>
        <h1 style='color:blue'>
        Analyse des facteurs influençant le prix des logements
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

if menu == "Accueil":

    st.title("Projet de statistique descriptive")

    st.header("Présentation du jeu de données")

    st.write(
        """
        Ce projet présente une analyse descriptive du jeu de données
        California Housing Prices.

        Les données seront analysées à l'aide des statistiques
        descriptives et de différentes techniques de visualisation.
        """
    )

    st.subheader("Les données")

    st.write(data)
     
elif menu == "Analyse descriptive":

    st.header("Analyse descriptive")

    st.subheader("Dimension des données")

    st.write(data.shape)

    st.subheader("Les 5 premières lignes")

    st.write(data.head())

    st.subheader("Les 5 dernières lignes")

    st.write(data.tail())

    st.subheader("Type des données")

    st.write(data.dtypes)

    st.subheader("Valeurs manquantes")

    st.write(data.isnull().sum())

    st.subheader("Statistiques descriptives")

    st.write(data.describe())
 
    st.subheader("La moyenne")

    st.write(data.mean(numeric_only=True))

    st.subheader("La médiane")

    st.write(data.median(numeric_only=True))

    st.subheader("La variance")

    st.write(data.var(numeric_only=True))

    st.subheader("L'écart-type")

    st.write(data.std(numeric_only=True))

   
elif menu == "Visualisation":

    st.header("Visualisation des données")

    
    st.subheader("Matrice de corrélation")

    corr = data.corr(numeric_only=True)

    plt.figure(figsize=(10,8))

    sns.heatmap(corr,
                cmap="summer",
                annot=True,
                fmt=".2f")

    st.pyplot(plt)

    plt.clf()

   
    st.subheader("Histogrammes")

    data.hist(figsize=(12,10))

    st.pyplot(plt)

    plt.clf()

   
    st.subheader("Histogramme de median_house_value")

    plt.figure(figsize=(8,5))

    plt.hist(data["median_house_value"], bins=20)

    plt.title("Distribution du prix des maisons")

    plt.xlabel("Prix")

    plt.ylabel("Fréquence")

    st.pyplot(plt)

    plt.clf()
    

    st.subheader("Boîte à moustaches")

    plt.figure(figsize=(10,6))

    plt.boxplot(data["median_house_value"])

    plt.title("Boîte à moustaches du prix des maisons")

    plt.ylabel("Prix")

    st.pyplot(plt)

    plt.clf()
    
else:

    st.header("Rapport")

    st.write("Résumé de l'analyse")

    st.write("""
    • Les statistiques descriptives permettent de mieux comprendre les données.

    • La matrice de corrélation montre les relations entre les variables.

    • Les histogrammes illustrent la distribution des données.

    • La boîte à moustaches permet d'observer les valeurs extrêmes.

    • Le revenu médian est l'une des variables les plus liées au prix des logements.
    """)

    st.write("Conclusion")

    st.write("""
    Après l'analyse descriptive et les visualisations, on constate que
    certaines variables influencent davantage le prix des logements,
    notamment le revenu médian.

    Les histogrammes permettent d'étudier la distribution des données,
    la matrice de corrélation met en évidence les relations entre les
    variables et la boîte à moustaches permet d'identifier les valeurs
    extrêmes.
    """)