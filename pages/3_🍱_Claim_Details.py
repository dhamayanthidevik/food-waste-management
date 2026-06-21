import streamlit as st
import pandas as pd
from database import load_data

data=load_data()

food_df = data["food_df"]

reciever_df=data["receiver_df"]

claim_df = data["claim_df"]

clamerged_df = food_df.merge(claim_df, on='Food_ID')
recmerge_df=reciever_df.merge(clamerged_df,on ='Receiver_ID')

st.title("🍱 Claim Analysis")

Status =  ["All"] +sorted(recmerge_df['Status'].dropna().unique().tolist())
City =  ["All"] + sorted(recmerge_df['City'].dropna().unique().tolist())
col1,col2= st.columns(2)

with col1:
    Status = st.selectbox("🏪 Status", Status)

with col2:
    City = st.selectbox("🏪 City", City)


filtered_df = recmerge_df.copy()

if Status != "All":
    filtered_df = filtered_df[filtered_df['Status'] == Status]
    
if City != "All":
    filtered_df = filtered_df[filtered_df['City'] == City]
    
filtered_df.rename(
    columns={'Name': 'Receiver_Name',
        'Type': 'Receiver_Type',
        'Contact': 'Receiver_Contact',
        'City': 'Receiver_City'},
    inplace=True
)

st.dataframe(filtered_df[["Receiver_Name","Receiver_Type","Receiver_City","Receiver_Contact","Status","Food_Name","Quantity","Expiry_Date","Food_Type","Meal_Type"]])

# print(clamerged_df.head(20))
