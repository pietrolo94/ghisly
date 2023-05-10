import streamlit as st
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import io
import os

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://w.wallhaven.cc/full/zy/wallhaven-zyxvqy.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def main():

    st.title("Classificazione Iris")

    newmodel = joblib.load("Classification_iris.pkl")
    sepal_lenght = st.number_input("sepal length", 1.0,10.0,3.0)
    sepal_width = st.number_input("sepal width", 1.0,10.0,3.0)
    petal_lenght = st.number_input("petal length", 1.0,10.0,3.0)
    petal_width = st.number_input("petal width", 1.0,10.0,3.0)
    res = newmodel.predict([[sepal_lenght,sepal_width, petal_lenght, petal_width]])[0]
    st.write(f"Classification iris: {res}")


    # Parte per caricare il file CSV o Excel
    st.header("Caricamento dati")
    file = st.file_uploader("Carica un file CSV o Excel", type=["csv", "xlsx"])
    if file is not None:
        if file.type.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml'):
            df = pd.read_excel(file, engine='openpyxl')
        else:
            df = pd.read_csv(file)
        dfx = df.to_numpy()
        # Mostra i dati caricati
        st.write("Dati caricati:")
        st.write(df)

        # Previsione dei dati usando il modello di regressione lineare
        st.header("Previsione Iris")
        predictions = newmodel.predict(dfx)
        df['Predicted Iris'] = predictions
        st.write("Risultati previsione:")
        st.write(df)
        # Aggiungi un pulsante per il download del file
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer,sheet_name='Profit_prediction', index=False)
        writer.save()
        output.seek(0)
        st.download_button(
            label="Scarica file Excel",
            data=output,
            file_name='Iris_prediction.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    #fine
    add_bg_from_url()
if __name__ == "__main__":
    main()