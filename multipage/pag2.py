import streamlit as st
import pandas as pd
from PIL import Image


def main():
    st.markdown('<div align="center"><h1>EDA Dataset pinguini</h1></div>', unsafe_allow_html=True)
    df = pd.read_csv("Penguins.csv")
    st.write(df)
    image3 = Image.open('pairplot.png')
    st.divider()
    st.image(image3, caption='pairplot')
    image = Image.open('xxx.jpg')
    st.divider()
    st.image(image, caption='A beautiful image')
    image2 = Image.open('count.png')
    st.divider()
    st.image(image2, caption= '...')

    ###### footer #####################################

if __name__ == "__main__":
    main()