import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import  LogisticRegression

def estadisticas():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    URL = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    dfIris = pd.read_csv(URL)

    st.title("Análisis estadistico de Iris Dataset")

    components.html(
        """<hr style="height:3px;border:none; color:#333;background-color:#333" />""")
    print(dfIris.head())

    st.header("Estadisticas")
    st.write("Filas, Columnas:")
    st.write(dfIris.shape)

    st.write("Describe:")
    st.dataframe(dfIris.describe())

    st.write("Clases:")
    st.write(dfIris["variety"].value_counts())

def graficas():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title("Visualizacion de graficas")
    components.html(
        """<hr style="height:3px;border:none; color:#333;background-color:#333" />""")

    URL= 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    dfIris= pd.read_csv(URL)

    fig = px.box(dfIris, y="variety")
    #dfIris.plot(kind='box', )
    st.plotly_chart(fig, use_container_width=True)


    st.subheader("Histogramas")
    for i in range(0, len(dfIris.columns)):
        fig = px.histogram(dfIris, x=dfIris.columns[i])
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Gráfica de correlación")
    fig = px.scatter_matrix(dfIris,
    dimensions=dfIris.columns[0:4],
    color="variety")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Correlación - Mapa de color")
    df_corr=dfIris.corr()
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
        x= df_corr.columns,
        y= df_corr.index,
        z= np.array(df_corr)
        )
    )

    st.plotly_chart(fig, use_container_width=True)

def modelos():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
    st.title("Visualizacion del modelo")

    df = pd.read_csv(url, names=names)

    x_train, x_test, y_train, y_test = train_test_split(df[df.columns[0:4]], df[df.columns[-1]], test_size=0.2)

    # print(train.shape)
    # print(test.shape)

    modelos = []

    modelo = LogisticRegression(random_state=0).fit(x_train, y_train)

    print(modelo.score(x_test, y_test))
    st.subheader("Precision:")
    st.write(modelo.score(x_test, y_test))

    print(modelo.predict(x_test))
    st.subheader("Prediccion:")
    st.write(modelo.predict(x_test))


# Crear una lista de opciones
options = ["Estadisticas", "Graficas", "Modelos"]

# Crear un sidebar con la lista de opciones
selection = st.sidebar.selectbox("Selecciona una opción", options, index=0)

# Llamar a diferentes funciones según la opción seleccionada
if selection == "Estadisticas":
    estadisticas()
elif selection == "Graficas":
    graficas()
else:
    modelos()