import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pydeck as pdk
import numpy as np
import seaborn as sns
import altair as alt

with st.sidebar:
  options = ["Welcome Page","Аналитические данные о жиличных комлексах"]
  selected = option_menu(
    menu_title = "Main menu",
    options = options,
)

def stats():
    artists = st.selectbox("Выберете тип отчета",['ЖК Лотос',"ЖК Гурман","ЖК Лилия"])
    if artists == "ЖК Лотос":
        st.header('''Основная сводка по ЖК "Лотос"''')
        st.metric(label="Объем трафика сегодня", value=pd.read_csv('datas.csv')['CustomerID'].count(), delta=+15,
            delta_color="normal")
        st.write("*Трафик по часам*:")
        df2 = pd.read_csv('datas.csv')
        fig = plt.figure(figsize=(20, 8))
        sns.countplot(df2['time'], palette = 'hsv')
        plt.title('By time ', fontsize = 20)
        st.pyplot(fig)
        st.header('''Портрет аудитории''')
        st.write("*Гендерный портрет*:")
        df2 = pd.read_csv('datas.csv')
        labels = ['Женщины', 'Мужчины']
        size = df2['Gender'].value_counts()
        explode = [0, 0.1]
        fig1, ax1 = plt.subplots()
        ax1.pie(size, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=95, explode=explode)
        st.pyplot(plt)
        st.write("*Возраст нашей аудитории*:")
        df2 = pd.read_csv('datas.csv')
        fig = plt.figure(figsize=(20, 8))
        sns.countplot(df2['Age'], palette = 'hsv')
        plt.title('Distribution of Age', fontsize = 20)
        st.pyplot(fig)
        st.write("*Доходы нашей аудитории в зависимости от возраста*:")
        df2 = pd.read_csv('datas.csv')
        fig = plt.figure(figsize=(40,10))
        sns.barplot(x = df2['Age'] , y = df2['Annual Income (k$)'] , palette='icefire')
        plt.title('Age vs Annual Income', fontsize = 20)
        plt.xticks(rotation=90)
        st.pyplot(fig)
        st.write("*А вот где живет наша аудитория*:")
        df = pd.DataFrame(
        np.random.randn(300, 2) / [360, 360] + [45.03723709987306, 38.99683388647596],
        columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=45.03723709987306,
            longitude=38.99683388647596,
            zoom=13,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=20,
                elevation_scale=20,
                elevation_range=[0, 30],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=7,
            ),
        ],
    ))
    else:
        st.header("Will be soon... 😴")

def calculator():
    st.write("*Hi*")


if selected == "Welcome Page":
    st.title(f"Пожалуйста выберете раздел 👈")
elif selected == "Аналитические данные о жиличных комлексах":
    stats()
elif selected == "Помещения специально для вас":
    calculator()
