import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache(allow_output_mutation=True)
def data_up():
    return pd.read_csv('ObesityDataNew.csv')

st.set_page_config(page_title='Niveles de obesidad en personas', layout='wide')
df = data_up()

def grafP(c2):

    df_mayores = df[df['Edad']>=18]
    df_menores = df[df['Edad']<18]

    df_menores.insert(3,"Mayor_edad",'menor',True)
    df_mayores.insert(3,"Mayor_edad",'mayor',True)

    df_G = pd.concat([df_mayores, df_menores], axis=0)
    
    fig = px.bar(df_G, x="Tipo_obesidad", y="T_uso_dispositivos", color="Mayor_edad", barmode = 'stack', color_discrete_map={'mayor':'#53BF9D', 'menor':'#F94C66'})
    c2.write(fig)


# def grafS(tipo_trans, col2):
#     fig_1, ab = plt.subplots(figsize=(6,6))
#     bicicleta = df.loc[df.loc[:, 'Medio_transporte'] == 'Bike']
#     colores=["#9B59B6","#E74C3C","#148F77"]
#     ab.pie(pd.get_dummies(bicicleta['Tipo_obesidad']).sum(), labels=bicicleta['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})

#     fig_2, ac = plt.subplots(figsize=(5,6))
#     caminar = df.loc[df.loc[:, 'Medio_transporte'] == 'Walking']
#     colores=["#FFAB91","#E3F2FD","#B2DFDB","#FFCCBC","#FFF59D","#B39DDB"]
#     ac.pie(pd.get_dummies(caminar['Tipo_obesidad']).sum(), labels=caminar['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})
        
#     fig_3, am = plt.subplots(figsize=(5,6))
#     moto = df.loc[df.loc[:, 'Medio_transporte'] == 'Motorbike']
#     colores=["#AB47BC","#1ABC9C","#85C1E9","#D4E6F1"]
#     am.pie(pd.get_dummies(moto['Tipo_obesidad']).sum(), labels=moto['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True,colors=colores, textprops={'fontsize': 12})


#     fig_4, aa = plt.subplots(figsize=(6,6))
#     automovil = df.loc[df.loc[:, 'Medio_transporte'] == 'Automobile']
#     colores=["#F8BBD0","#CE93D8","#EF9A9A","#9FA8DA","#D98880","#DC7633","#9575CD"]
#     aa.pie(pd.get_dummies(automovil['Tipo_obesidad']).sum(), labels=automovil['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True, colors=colores, textprops={'fontsize': 12})


#     fig_5, at = plt.subplots(figsize=(5,6))
#     transportePublico = df.loc[df.loc[:, 'Medio_transporte'] == 'Public_Transportation']
#     colores=["#2196F3","#FCE4EC","#F48FB1","#4DB6AC","#D98880","#B2DFDB","#D1C4E9"]
#     at.pie(pd.get_dummies(transportePublico['Tipo_obesidad']).sum(), labels=transportePublico['Tipo_obesidad'].unique(), autopct='%1.1f%%', shadow=True,colors=colores, textprops={'fontsize': 12})

#     if tipo_trans == 'Bike':
#         col2.pyplot(fig_1)
#     if tipo_trans == 'Walking':
#         col2.pyplot(fig_2)
#     if tipo_trans == 'Motorbike':
#         col2.pyplot(fig_3)
#     if tipo_trans == 'Automobile':
#         col2.pyplot(fig_4)
#     if tipo_trans == 'Public_Transportation':
#         col2.pyplot(fig_5)

# def grafT(col3):

#     grupos = list(df['Tipo_obesidad'].unique())

#     insuficiente = df[df['Tipo_obesidad'] == 'Peso_insuficiente']
#     normal = df[df['Tipo_obesidad'] == 'Peso_normal']
#     sobre_p1 = df[df['Tipo_obesidad'] == 'Sobrepeso_Nivel_I']
#     sobre_p2 = df[df['Tipo_obesidad'] == 'Sobrepeso_Nivel_II']
#     obesidad1 = df[df['Tipo_obesidad'] == 'Obesidad_Tipo_I']
#     obesidad2 = df[df['Tipo_obesidad'] == 'Obesidad_Tipo_II']
#     obesidad3 = df[df['Tipo_obesidad'] == 'Obesidad_Tipo_III']

#     Bike= [
#         len(normal[normal['Medio_transporte']=='Bike']),
#         len(sobre_p1[sobre_p1['Medio_transporte']=='Bike']),
#         len(sobre_p2[sobre_p2['Medio_transporte']=='Bike']),
#         len(obesidad1[obesidad1['Medio_transporte']=='Bike']),
#         len(insuficiente[insuficiente['Medio_transporte']=='Bike']),
#         len(obesidad2[obesidad2['Medio_transporte']=='Bike']),
#         len(obesidad3[obesidad3['Medio_transporte']=='Bike'])
#     ]

#     Walking= [
#         len(normal[normal['Medio_transporte']=='Walking']),
#         len(sobre_p1[sobre_p1['Medio_transporte']=='Walking']),
#         len(sobre_p2[sobre_p2['Medio_transporte']=='Walking']),
#         len(obesidad1[obesidad1['Medio_transporte']=='Walking']),
#         len(insuficiente[insuficiente['Medio_transporte']=='Walking']),
#         len(obesidad2[obesidad2['Medio_transporte']=='Walking']),
#         len(obesidad3[obesidad3['Medio_transporte']=='Walking'])
#     ]

#     Automobile= [
#         len(normal[normal['Medio_transporte']=='Automobile']),
#         len(sobre_p1[sobre_p1['Medio_transporte']=='Automobile']),
#         len(sobre_p2[sobre_p2['Medio_transporte']=='Automobile']),
#         len(obesidad1[obesidad1['Medio_transporte']=='Automobile']),
#         len(insuficiente[insuficiente['Medio_transporte']=='Automobile']),
#         len(obesidad2[obesidad2['Medio_transporte']=='Automobile']),
#         len(obesidad3[obesidad3['Medio_transporte']=='Automobile'])
#     ]

#     Motorbike= [
#         len(normal[normal['Medio_transporte']=='Motorbike']),
#         len(sobre_p1[sobre_p1['Medio_transporte']=='Motorbike']),
#         len(sobre_p2[sobre_p2['Medio_transporte']=='Motorbike']),
#         len(obesidad1[obesidad1['Medio_transporte']=='Motorbike']),
#         len(insuficiente[insuficiente['Medio_transporte']=='Motorbike']),
#         len(obesidad2[obesidad2['Medio_transporte']=='Motorbike']),
#         len(obesidad3[obesidad3['Medio_transporte']=='Motorbike'])
#     ]

#     Public_Transportation= [
#         len(normal[normal['Medio_transporte']=='Public_Transportation']),
#         len(sobre_p1[sobre_p1['Medio_transporte']=='Public_Transportation']),
#         len(sobre_p2[sobre_p2['Medio_transporte']=='Public_Transportation']),
#         len(obesidad1[obesidad1['Medio_transporte']=='Public_Transportation']),
#         len(insuficiente[insuficiente['Medio_transporte']=='Public_Transportation']),
#         len(obesidad2[obesidad2['Medio_transporte']=='Public_Transportation']),
#         len(obesidad3[obesidad3['Medio_transporte']=='Public_Transportation'])
#     ]

#     indice = np.arange(len(grupos))
#     fig6, ax = plt.subplots(figsize=(14,8))

#     ax.bar(indice, Motorbike, label='Moto', color="#5499C7")
    
#     ax.bar(indice, Bike, label='Bicicleta', color = "#3498DB", bottom=np.array(Motorbike))

#     ax.bar(indice, Walking, label='Caminata', color = "#1ABC9C", bottom=np.array(Bike))

#     ax.bar(indice, Automobile, label='Automovil', color = "#27AE60",  bottom=np.array(Walking))

#     ax.bar(indice, Public_Transportation, label='Transporte Publico', color = "#138D75", bottom=np.array(Motorbike)+np.array(Bike)+np.array(Walking)+np.array(Automobile))

#     plt.xticks(indice, grupos)
#     plt.ylabel("Medio de transporte")
#     plt.xlabel("Tipo de obesidad")
#     plt.title('Cantidad de Personas que Utilizan un Determinado Medio de Transporte')
#     ax.legend()
#     col3.pyplot(fig6)


def grafF(col2):
    fig7 = px.bar( df.groupby(["Tipo_obesidad"]).mean().reset_index().sort_values(by="Consumo_agua", ascending=False), 
    x ="Consumo_agua", y ="Tipo_obesidad", barmode = 'stack', color_discrete_sequence=['#53BF9D'], 
    orientation='h')
    
    col2.write(fig7)    

    #  df.groupby('Tipo_obesidad')['F_actvidad_fisica'].mean().plot(kind = 'barh', legend = 'reverse', color = '#138D75')

    #  plt.title('Relación obesidad - Consumo de agua', 
    #          loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:red'})

    #  plt.ylabel("Tipo de obesidad", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    #  plt.xlabel('Consumo de agua promedio en litros', fontdict = {'fontsize':14, 'fontweight':'bold'})
    #  plt.show()
    #  col2.pyplot(fig7)

# def grafFi(col3):
#     fig8, ax = plt.subplots(figsize = (14,8))

#     df.groupby('Tipo_obesidad')['F_actvidad_fisica'].mean().plot(legend = 'reverse', 
#                                                                     color = '#5499C7',
#                                                                     marker = "o", 
#                                                                     markersize=12,
#                                                                 markerfacecolor="red")


#     plt.title('Relación obesidad - Actividad física', 
#             loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:red'})

#     plt.xlabel("Tipo de obesidad", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
#     plt.ylabel('Tiempo de actividad física', fontdict = {'fontsize':14, 'fontweight':'bold'})
#     col3.pyplot(fig8)

def main():

    menu = ["Datos", "Exploración", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    
    if choice == 'Datos':
        c1, c2, c3 = st.columns([1,3,1])
        c2.title('Datos - Niveles de obesidad en personas de México, Perú y Colombia.')
        c2.write("""El presente Dataset muestra información de personas encuestadas en Colombia, Perú y México en un rango de 
        edades que va desde los 14 a los 61 años entre hombres y mujeres. El Dataset cuenta con 17 columnas y 2111 registros, donde en 
        la ultima columna se concluye el tipo de peso que tiene una persona la cual se clasifica en 7 categoría: peso insuficiente, peso 
        norma, sobre peso nivel I, sobrepeso nivel II, obesidad tipo I, obesidad tipo II y obesidad tipo III""")
        c2.title('')
        col1, col2, col3 = st.columns([1,5,1])
        col2.subheader('Datos registrados en el Dataframe')
        col2.write(df)
        c2.title('')

        col2.subheader('Estadisticas')
        d_d2 = df.describe()
        col2.write(d_d2)

    elif choice == 'Exploración':
        c1, c2, c3 = st.columns([1,3,1])
        c2.title('Exploración - Niveles de obesidad en personas de México, Perú y Colombia.')
        c2.title('')
        c2.subheader('Tipo de peso que padece una persona teniendo presente si es mayor o menor de edad.')
        grafP(c2)
        c2.write("""Si es menor de edad es muy probable que el menor tenga peso insuficiente o se encuentre en su peso normal, 
        pero para el caso donde las personas son mayores de edad existe mayor probabilidad de sufrir de obesidad ya sea tipo I, II o III.""")

        c2.title('')
        c2.title('')
        cl1, cl2, cl3 = st.columns([1,4,1])
        c1, c2, c3, = st.columns([1,1,3])
        col1, col2, col3, col4 = st.columns([1,4,5,1])
        co1, co2, co3 = st.columns([1,8,1])
        
        cl2.subheader('Relación entre los medios de trasnposte utilizados por las personas y el tipo de peso que reportan.')
        c2.subheader('')
        tipo_trans_options = df['Medio_transporte'].unique().tolist()
        tipo_trans = c2.selectbox("Elija el tipo de transporte que desea visualizar", tipo_trans_options)
        c2.subheader('')
        # grafS(tipo_trans, col2)
        # grafT(col3)
        co2.write("""Basados en los datos reportados através de las gráficas podemos concluir que un transporte usual como la bicicleta 
        de las personas registradas utilizan(51.7%) poseen un peso normal  y el resto de los datos distribuidos entre las personas 
        con obesidad tipo 2 y sobre peso nivel 1. En cambio si observamos la gráfica de las personas que caminan y como se relaciona con su peso el porcentaje 
        connotativo esta dado por las personas que sufren sobre peso nivel 2 , seguido por la obesidad tipo 1; 
        solo la minoría representada en un 3.6% tienen un peso normal.""")
        co2.write("""En medios terrestres como la moto existe mucho contraste con las 
        personas de peso normal (54.5%), el (27.3%) que figuran las personas con sobre peso nivel 1 y el (9.1%) que comparten las Personas 
        con sobre peso nivel 1 y la obesidad tipo 1. Por lo tanto , podemos decir que este no es un medio favorecedor en cuestión de 
        transporte para los ciudadanos que presentan cualquier tipo de obesidad o sobrepeso.""")

        cl1, cl2, cl3 = st.columns([1,4,1])
        c1, c2, c3, = st.columns([1,1,3])
        col1, col2, col3, col4 = st.columns([1,8,8,1])
        cl2.title('')
        cl2.title('')
        cl2.subheader('¿Como influye en el peso de una persona el hecho de tomar o no agua y realizar actividades físicas?')
        c2.subheader('')
        grafF(col2)
        # grafFi(col3)


    elif choice == 'About':
        cl1, cl2, cl3 = st.columns([1,4,1])
        cl2.title("¿Quienes somos?")
        cl2.subheader("Integrantes:")
        cl2.write("Carlos Javier Saenz Ortega")
        cl2.write("Leonel David Doria Cantero")
        cl2.write("Luis Alfredo García Nisperuza")
        cl2.write("Kevin Andres Anaya Correa")
        cl2.write("Maria Angel Garcia Rodriguez")      
    

if __name__ == '__main__':
    main()