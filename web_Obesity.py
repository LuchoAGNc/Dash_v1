import streamlit as st
import pickle
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


df = pd.read_csv('ObesityDataNew.csv')

def main():
    
    menu = ["Home", "Search", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Home")
        st.success("Full Layout")

        st.title('Dataframe - Niveles de obesidad en individuos México, Perú y Colombia')
        AgGrid(df)

        col1, col2 = st.columns(2)

        col1.success("First Column")
        col2.success("First Column") 

    elif choice == 'Search':
        st.subheader("Search")

    elif choice == 'About':
        st.subheader("About")

    
    

if __name__ == '__main__':
    main()