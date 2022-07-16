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
    menores =  [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Edad < 18)]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Edad < 18)]),
    ]

    mayores =  [
        len(df[(df.Tipo_obesidad == "Peso_normal") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_I") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Sobrepeso_Nivel_II") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_I") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_II") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Obesidad_Tipo_III") & (df.Edad >= 18)]),
        len(df[(df.Tipo_obesidad == "Peso_insuficiente") & (df.Edad >= 18)]),
    ]

    labels =list(df.Tipo_obesidad.unique())

    night_colors = ['#53BF9D', '#F94C66', '#BD4291', '#FFC54D', '#005F99', '#FFF5B7', '#3AB4F2']

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=mayores, name="Mayor Edad", marker_colors=night_colors), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=menores, name="Menor Edad", marker_colors=night_colors), 1, 2)


    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
            
        annotations=[dict(text='', x=0.18, y=0.5, font_size=20, showarrow=False),
                    dict(text='', x=0.82, y=0.5, font_size=20, showarrow=False)])
    c2.write(fig)


def grafS(co2):

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

    fig2.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
    co2.write(fig2)


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
        c2.subheader('Relación entre el Peso y la Edad')
        grafP(c2)
        c2.write("""Se podría afirmar según la gráfica, que el tipo de peso que mayormente padecen las personas independientemente de 
        cuál sea su edad, es el de obesidad. La moda para la población mayor de edad es obesidad tipo III, siendo la que tiene los 
        mayores índices de riesgos para la salud, en el caso de la población menor de edad, la obesidad tipo I y II son más comunes, 
        donde la primera es más frecuente que la segunda.""")

        co1, co2, co3 = st.columns([1,3,1])
        
        c2.subheader('')
        # tipo_trans_options = df['Medio_transporte'].unique().tolist()
        # tipo_trans = c2.selectbox("Elija el tipo de transporte que desea visualizar", tipo_trans_options)
        co2.subheader('Medio de Transporte Utilizado Segun su Peso')
        grafS(co2)
        co2.write("""Basados en los datos reportados através de las gráficas podemos concluir que un transporte usual como la bicicleta 
        de las personas registradas utilizan(51.7%) poseen un peso normal  y el resto de los datos distribuidos entre las personas 
        con obesidad tipo 2 y sobre peso nivel 1. En cambio si observamos la gráfica de las personas que caminan y como se relaciona con su peso el porcentaje 
        connotativo esta dado por las personas que sufren sobre peso nivel 2 , seguido por la obesidad tipo 1; 
        solo la minoría representada en un 3.6% tienen un peso normal.""")
        co2.write("""En medios terrestres como la moto existe mucho contraste con las 
        personas de peso normal (54.5%), el (27.3%) que figuran las personas con sobre peso nivel 1 y el (9.1%) que comparten las Personas 
        con sobre peso nivel 1 y la obesidad tipo 1. Por lo tanto , podemos decir que este no es un medio favorecedor en cuestión de 
        transporte para los ciudadanos que presentan cualquier tipo de obesidad o sobrepeso.""")
        co1.title('')
        co1.title('')

        col1, col2, col3, col4 = st.columns([1,5,5,1])
        col1.title('')
        col2.subheader('¿Cual es el promedio de litros de agua consumida por categorías de obesidad ?')
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