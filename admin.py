from sqlalchemy import column
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from streamlit_webrtc import webrtc_streamer
import mysql.connector
import csv
import time
from datetime import datetime

with st.sidebar:
  options = ["Welcome Page","Камеры","Все камеры"]
  selected = option_menu(
    menu_title = "Main menu",
    options = options,
)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="n01082002",
    database = "China"
)


def cams():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM camera;")
    myresult = mycursor.fetchall()
    select_arr = []
    # print(myresult)
    for i in range(0,len(myresult)):
        select_arr.append(i)
    artist = st.selectbox("Выберете номер камеры для просмотра отчета", select_arr)
    st.title(f"Информация по {artist} камере")
    video_file = open('video1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes,)
    st.write("*It's a magic and it's a numbers of peoples on this cums for today*")
    # print(artists)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM camera_list where cam_id = " + str(artist+1) + ";")
    myresult = mycursor.fetchall()
    trend = 0
    today = 0
    ts = time.time()
    for i in myresult:
        if int(ts) - int(i[2]) > 86400 and int(ts) - int(i[2]) < 172800:
            trend+=1
        elif int(ts) -int(i[2]) < 86400:
            today+=1
    nn = "normal"
    if today < trend:
        nn = "reverse"
    st.metric(label="Объем трафика сегодня на этой камере", value=today, delta=today-trend,
        delta_color=nn)
    artists = st.selectbox("Выберете инфографику",['История по дням списком',"Динамика по дням"])
    if artists == "История по дням списком":
        st.header("Users by a day")
        month = st.select_slider(
            "Select month",
            ["Январь","Ферваль","Март","Апрель","Май","Июня","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
        )
        if (month == "Январь") or (month == "Март") or (month == "Май") or (month == "Июль") or (month == "Август") or (month == "Октябрь") or (month == "Декабрь"):
            day = st.select_slider(
                "Select day",
                range(0,32)
            )
        elif month == "Февраль":
            day = st.select_slider(
                "Select day",
                range(0,29)
            )
        else:
            day = st.select_slider(
                "Select day",
                range(0,31)
            )
        
        monn = ["Январь","Ферваль","Март","Апрель","Май","Июня","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
        ag = []
        k = 0
        f = 0
        for j in monn:
            if j == month:
                k= f+1
            f+=1
        # print(k)
        for i in myresult:
            if k == datetime.fromtimestamp(int(i[2])).month and day == datetime.fromtimestamp(int(i[2])).day:
                ag.append(i)
        # print(ag)
        ga = []
        for i in ag:
            ga.append((i[0],i[1],datetime.fromtimestamp(int(i[2])),i[3]))
        print(artist)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM deanon;")
        gf = mycursor.fetchall()
        gc = {}
        print(gf)
        print(ga)

        with open('first.csv','w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['cam_id','chel_id','gender',"age"])
            for row in gf:
                csv_out.writerow(row)
        with open('second.csv','w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(["id",'chel_id','time'])
            for row in ga:
                csv_out.writerow(row)
        data = pd.read_csv("first.csv")
        st.dataframe(data)
        data = pd.read_csv("second.csv")
        st.dataframe(data)
    elif "Динамика по дням" == artists:
        st.write("*Will be later*")


def dasboardik():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM camera;")
    myresult = mycursor.fetchall()
    select_arr = []
    mycursor.execute("SELECT * FROM camera_list;")
    results = mycursor.fetchall()
    ids = []
    address = []
    status = []
    count_total = []
    today_count = []
    co_us = {}
    co_cam = {}
    for i in myresult:
        ids.append(i[0])
        status.append("offline")
        if not i[0] in co_cam:
            co_cam[i[0]] = 0
        if not i[0] in co_us:
            co_us[i[0]] = 0
    print(results)
    for i in results:
        co_cam[i[3]]= co_cam[i[3]]+1
        ts = time.time()
        if ts - int(i[2]) < 86000:
            co_us[i[3]]= co_us[i[3]]+1
    for i in co_cam:
        print("key" + str(i) +  " " + "value")
    for i in ids:
        count_total.append(co_cam[i])
        today_count.append(co_us[i])
        address.append("Not specified")


    df = pd.DataFrame({
        'Camera number ': ids,
        'address' : address,
        'status': status,
        'total_count': count_total,
        'today count': today_count
    })
    st.header("Camera's list")
    st.write(df)



if selected == "Welcome Page":
    st.title(f"Пожалуйста выберете раздел 👈")
elif selected == "Камеры":
    cams()
elif selected == "Все камеры":
    dasboardik()