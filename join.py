# import pandas as pd
# import numpy as np
# import altair as alt
# import streamlit as st
import mysql.connector

# pds = pd.read_csv('datas.csv')[['Spending Score (1-100)','CustomerID']]
# pds.columns = ['Number of customers', 'Revenue']

# df = pd.DataFrame(
#     pds,
#     columns=['Number of customers', 'Revenue'])

print("Connecting")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="n01082002",
  database = "China"
)
print("Hi")
print(mydb) 
print("end")

# st.dataframe(pds)
# st.dataframe(np.random.rand(200, 2))

# c = alt.Chart(df).mark_circle().encode(
#     x='Number of customers (thousand per month)', y='Revenue', tooltip=['Number of customers', 'Revenue'])

# st.altair_chart(c, use_container_width=True)