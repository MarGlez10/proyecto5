import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Anuncios de venta de coches')

car_data = pd.read_csv('./vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Histograma para el numero de anuncios publicados por modelo del año de los vehiculos')

    # crear un histograma
    fig = px.histogram(car_data, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# creo el segundo botón
build_grafdisp = st.checkbox('Construir gráfico de dispersión')

if build_grafdisp:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    build_grafdisp = px.scatter(car_data, x='odometer', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(build_grafdisp, use_container_width=True)
