import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def grafS(col2):

    Transporte_Publico = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Medio_transporte == "Transporte_Publico")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Medio_transporte == "Transporte_Publico")]),
    ]

    Caminar = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Medio_transporte == "Caminar")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Medio_transporte == "Caminar")]),
    ]

    Automovil = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Medio_transporte == "Automovil")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Medio_transporte == "Automovil")]),
    ]

    Moto = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Medio_transporte == "Moto")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Medio_transporte == "Moto")]),
    ]

    Bicicleta = [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Medio_transporte == "Bicicleta")]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Medio_transporte == "MoBicicletato")]),
    ]

    x=list(df.Tipo_obesidad.unique())
    fig2 = go.Figure(go.Bar(x=x, y=Transporte_Publico,  marker_color='#53BF9D', name='Transporte Publico'))
    fig2.add_trace(go.Bar(x=x, y=Caminar, name='Caminar',  marker_color='#F94C66'))
    fig2.add_trace(go.Bar(x=x, y=Automovil, name='Automovil',  marker_color='#BD4291'))
    fig2.add_trace(go.Bar(x=x, y=Moto, name='Moto',  marker_color='#FFC54D'))
    fig2.add_trace(go.Bar(x=x, y=Bicicleta, name='Bicicleta',  marker_color='#005F99'))

    fig2.update_layout(title='Medio de Transporte Utilizado Segun su Peso',barmode='stack', xaxis={'categoryorder':'category ascending'})
    col2.write(fig2)

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

    menu = ["Datos", "Exploración", "Predicción", "About",]
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
        grafS(col2)
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

    elif choice == 'Predicción':
        cl1, cl2, cl3 = st.columns([1,4,1])
        cl2.title("Predicción - Niveles de obesidad en personas de México, Perú y Colombia.")
        cl2.title('')
        cl2.title('')
        cl2.subheader("Ingrese los datos para realizar la prediccion de su tipo de peso:")
        cl2.title('')
        c1, c2, c3, c4 , c5, c6 = st.columns([1,2,2,2,2,1])
        c2.selectbox("Genero:", {"Femenino ", "Masculino"})
        c3.slider("Edad:", min_value=5, max_value=120)
        c4.selectbox("Familiar con sobrepeso ?", {"Si", "No"})
        c5.selectbox("Consume alimentos ricos en calorias?", {"Si", "No"})
        c2.slider("Numero de comidas", min_value=1, max_value=8)
        c3.selectbox("Merienda ?", {"No", "Algunas veces", "Frecuentemente", "Siempre"})
        c4.selectbox("Fuma ?", {"Si", "No"})
        c5.slider("Frecuencia en actividades Fisicas", min_value=0, max_value=4)
        c2.selectbox("Sigues tu consumo de calorias?", {"Si", "No"})
        c3.slider("Tiempo de uso en dispositivos electronicos", min_value=0, max_value=3)
        c4.selectbox("Consume alcohol ?", {"No", "Algunas veces", "Frecuentemente", "Siempre"})
        c5.selectbox("Que medio de transporte usa?", {"Bicicleta", "Caminar", "Moto", "Automovil", "Transporte Publico"})
        c2.button('Predecir')

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