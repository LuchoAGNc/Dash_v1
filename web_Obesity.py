import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('ObesityDataNew.csv')

def grafP(tipo_ob):
    df_mayores = df[df['Edad']>=18]
    df_menores = df[df['Edad']<18]

    df_menores.insert(3,"Mayor_edad",'menor',True)
    df_mayores.insert(3,"Mayor_edad",'mayor',True)

    df_G = pd.concat([df_mayores, df_menores], axis=0)
    grupos = list(df['Tipo_obesidad'].unique())

    insuficiente = df_G[df_G['Tipo_obesidad'] == 'Peso_insuficiente']
    normal = df_G[df_G['Tipo_obesidad'] == 'Peso_normal']
    sobre_p1 = df_G[df_G['Tipo_obesidad'] == 'Sobrepeso_Nivel_I']
    sobre_p2 = df_G[df_G['Tipo_obesidad'] == 'Sobrepeso_Nivel_II']
    obesidad1 = df_G[df_G['Tipo_obesidad'] == 'Obesidad_Tipo_I']
    obesidad2 = df_G[df_G['Tipo_obesidad'] == 'Obesidad_Tipo_II']
    obesidad3 = df_G[df_G['Tipo_obesidad'] == 'Obesidad_Tipo_III']

    mayores= [
        len(normal[normal['Mayor_edad']=='mayor']),
        len(sobre_p1[sobre_p1['Mayor_edad']=='mayor']),
        len(sobre_p2[sobre_p2['Mayor_edad']=='mayor']),
        len(obesidad1[obesidad1['Mayor_edad']=='mayor']),
        len(insuficiente[insuficiente['Mayor_edad']=='mayor']),
        len(obesidad2[obesidad2['Mayor_edad']=='mayor']),
        len(obesidad3[obesidad3['Mayor_edad']=='mayor'])
    ]

    menores= [
        len(normal[normal['Mayor_edad']=='menor']),
        len(sobre_p1[sobre_p1['Mayor_edad']=='menor']),
        len(sobre_p2[sobre_p2['Mayor_edad']=='menor']),
        len(obesidad1[obesidad1['Mayor_edad']=='menor']),
        len(insuficiente[insuficiente['Mayor_edad']=='menor']),
        len(obesidad2[obesidad2['Mayor_edad']=='menor']),
        len(obesidad3[obesidad3['Mayor_edad']=='menor'])
    ]



    indice = np.arange(len(grupos))
    fig, ax = plt.subplots(figsize=(14,7))

    ax.bar(indice,  mayores, label='Mayores de edad', color="#80ced6")
    ax.bar(indice, menores, label='Menores de edad', color = "#ffef96", bottom=mayores)
    plt.xticks(indice, grupos)
    plt.ylabel("Participanes")
    plt.xlabel("Grupos")
    plt.title('Participantes por menor/mayor de edad')
    ax.legend()
    st.pyplot(fig)

def grafS(tipo_trans, col1):
    fig_1, ab = plt.subplots(figsize=(6,6))
    bicicleta = df.loc[df.loc[:, 'Medio_transporte'] == 'Bike']
    colores=["#9B59B6","#E74C3C","#148F77"]
    ab.pie(pd.get_dummies(bicicleta['Tipo_obesidad']).sum(), labels=bicicleta['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})

    fig_2, ac = plt.subplots(figsize=(5,6))
    caminar = df.loc[df.loc[:, 'Medio_transporte'] == 'Walking']
    colores=["#FFAB91","#E3F2FD","#B2DFDB","#FFCCBC","#FFF59D","#B39DDB"]
    ac.pie(pd.get_dummies(caminar['Tipo_obesidad']).sum(), labels=caminar['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})
        
    fig_3, am = plt.subplots(figsize=(5,6))
    moto = df.loc[df.loc[:, 'Medio_transporte'] == 'Motorbike']
    colores=["#AB47BC","#1ABC9C","#85C1E9","#D4E6F1"]
    am.pie(pd.get_dummies(moto['Tipo_obesidad']).sum(), labels=moto['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True,colors=colores, textprops={'fontsize': 12})


    fig_4, aa = plt.subplots(figsize=(6,6))
    automovil = df.loc[df.loc[:, 'Medio_transporte'] == 'Automobile']
    colores=["#F8BBD0","#CE93D8","#EF9A9A","#9FA8DA","#D98880","#DC7633","#9575CD"]
    aa.pie(pd.get_dummies(automovil['Tipo_obesidad']).sum(), labels=automovil['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})


    fig_5, at = plt.subplots(figsize=(5,6))
    transportePublico = df.loc[df.loc[:, 'Medio_transporte'] == 'Public_Transportation']
    colores=["#2196F3","#FCE4EC","#F48FB1","#4DB6AC","#D98880","#B2DFDB","#D1C4E9"]
    at.pie(pd.get_dummies(transportePublico['Tipo_obesidad']).sum(), labels=transportePublico['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True,colors=colores, textprops={'fontsize': 12})

    if tipo_trans == 'Bike':
        col1.pyplot(fig_1)
    if tipo_trans == 'Walking':
        col1.pyplot(fig_2)
    if tipo_trans == 'Motorbike':
        col1.pyplot(fig_3)
    if tipo_trans == 'Automobile':
        col1.pyplot(fig_4)
    if tipo_trans == 'Public_Transportation':
        col1.pyplot(fig_5)

def main():

    menu = ["Home", "Predict", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.title('Bienvenido a la plataforma para la predicción de tipos de pesos')

        tipo_ob_options = df['Tipo_obesidad'].unique().tolist()
        tipo_trans_options = df['Medio_transporte'].unique().tolist()

        tipo_ob = st.multiselect('Elija el tipo que desea visualizar', tipo_ob_options, ['Peso_insuficiente','Peso_normal', 
        'Sobrepeso_Nivel_I', 'Sobrepeso_Nivel_II', 'Obesidad_Tipo_I', 'Obesidad_Tipo_II', 'Obesidad_Tipo_III']) 
        grafP(tipo_ob)

        col1, col2 = st.columns(2)

        tipo_trans = col1.selectbox("Elija el tipo que desea visualizar", tipo_trans_options) 
        grafS(tipo_trans, col1)

    elif choice == 'Predict':
        st.subheader("Predict")

    elif choice == 'About':
        st.subheader("About")

    
    

if __name__ == '__main__':
    main()