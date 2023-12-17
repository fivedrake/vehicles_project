import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Venta de coches :car: :pickup_truck:', divider='blue')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button:
    st.write('Histrograma de venta de coches')
fig = px.histogram(car_data, x="odometer")
st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Gráfico de dispersión') # crear un botón
        
if scatter_button:
    st.write('Venta de coches en gráfico de dispersión')
fig = px.scatter(car_data, x="odometer")
st.plotly_chart(fig, use_container_width=True) 

st.write('¿Cual es la condición que buscas?')

excellent = st.checkbox('Excelente')
like_new = st.checkbox('Como nuevo')
good = st.checkbox('Bueno')
fair = st.checkbox('Justo')

if excellent:
    car_data[car_data['condition'] == 'excellent']

if like_new:
    car_data[car_data['condition'] == 'like new']

if good:
    car_data[car_data['condition'] == 'good']

if fair:
    car_data[car_data['condition'] == 'fair']
