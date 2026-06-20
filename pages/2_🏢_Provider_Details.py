import streamlit as st
import pandas as pd
import pyodbc


data=load_data()

food_df = data["food_df"]

provider_df = data["provider_df"]

promerged_df = food_df.merge(provider_df, on='Provider_ID')

# print(promerged_df.info())

st.title("🏢 Provider Analysis")

provider_name =  ["All"] +sorted(promerged_df['Name'].dropna().unique())


provider_type = ["All"] + sorted(promerged_df['Provider_Type'].dropna().unique())

food_name =  ["All"] +sorted(promerged_df['Food_Name'].dropna().unique())

meal_type =  ["All"] + sorted(promerged_df['Meal_Type'].dropna().unique())


food_type =  ["All"] + sorted(promerged_df['Food_Type'].dropna().unique())

city =  ["All"] + sorted(promerged_df['City'].dropna().unique())


col1, col2, col3 = st.columns(3)

with col1:
    provider_name = st.selectbox("🏪 Provider Name", provider_name)
    

with col2:
    provider_type = st.selectbox("🏢 Provider Type", provider_type)

with col3:
   food_name = st.selectbox("🍲 Food Name", food_name)
   

col4, col5, col6 = st.columns(3)

with col4:
     meal_type = st.selectbox("🍱 Meal Type", meal_type)
   

with col5:
    
    food_type = st.selectbox("🥗 Food Type", food_type)
with col6:
    city = st.selectbox("📍 City", city)

# filtered_df = promerged_df[
#     (promerged_df['City'] == city) &
#     (promerged_df['Provider_Type'] == provider_type) &
#     (promerged_df['Meal_Type'] == meal_type) &
#     (promerged_df['Food_Type'] == food_type) &
#     (promerged_df['Food_Name'] == food_name) &
#     (promerged_df['Name'] == provider_name)
# ]
filtered_df = promerged_df.copy()

if city != "All":
    filtered_df = filtered_df[filtered_df['City'] == city]

if provider_type != "All":
    filtered_df = filtered_df[filtered_df['Provider_Type'] == provider_type]

if meal_type != "All":
    filtered_df = filtered_df[filtered_df['Meal_Type'] == meal_type]

if food_type != "All":
    filtered_df = filtered_df[filtered_df['Food_Type'] == food_type]

if food_name != "All":
    filtered_df = filtered_df[filtered_df['Food_Name'] == food_name]

if provider_name != "All":
    filtered_df = filtered_df[filtered_df['Name'] == provider_name]
st.subheader("🍲 Food Details")

filtered_df.rename(columns={'Name': 'Provider_Name',
                            'Contact':'Provider_Contact'},inplace=True)


st.dataframe(
    filtered_df[['Provider_Name', 'Provider_Type','Provider_Contact', 'Food_Name', 'Quantity',  'Location', 'Food_Type', 'Meal_Type']]
    
)
