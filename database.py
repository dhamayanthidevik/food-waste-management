# import pyodbc
import pandas as pd
import streamlit as st
# def get_connection():
#     return pyodbc.connect(
#             "DRIVER={ODBC Driver 17 for SQL Server};"
#             "SERVER=INBOOK_X1_SLIM\\SQLEXPRESS;"
#             "DATABASE=FoodWasteDB;"
#             "Trusted_Connection=yes;"
#         )
    
@st.cache_data
def load_data():
    # conn = get_connection()
    # cursor=conn.cursor()
    food_df = pd.read_csv("Food_listing_clean.csv")

    provider_df = pd.read_csv("clean_Providers.csv")

    receiver_df = pd.read_csv("clean_Receivers.csv")

    claim_df = pd.read_csv("clean_Claims.csv")
        
    promerged_df = food_df.merge(
        provider_df, 
        on='Provider_ID'
    )
    clamerged_df = food_df.merge(
                 claim_df, 
                 on='Food_ID'
    )
    recmerge_df=receiver_df.merge(
               clamerged_df,
               on ='Receiver_ID'
    )
    # conn.close()
   
    return {
        "food_df": food_df,
        "provider_df": provider_df,
        "receiver_df": receiver_df,
        "claim_df": claim_df,
        "promerged_df":promerged_df,
        "clamerged_df":clamerged_df,
        "recmerge_df":recmerge_df
    }
# =====================CURD operation Provider===============================
# def get_providers():
#      return pd.read_csv("providers_clean.csv")

# def add_provider(name, provider_type,Address, city, contact):
#     conn = get_connection()
#     cursor=conn.cursor()
#     query = """
#     INSERT INTO clean_Providers
#     (Name, Type, Address,City, Contact)
#     VALUES (?, ?, ?, ?,?)
#     """

#     cursor.execute(
#         query,
#         (name, provider_type,Address, city, contact)
#     )

#     conn.commit()
#     conn.close()
    
# def update_provider(provider_id, city):
#     conn = get_connection()
#     cursor=conn.cursor()
#     query = """
#     UPDATE clean_Providers
#     SET City = ?
#     WHERE Provider_ID = ?
#     """

#     cursor.execute(
#         query,
#         (city, provider_id)
#     )

#     conn.commit()
#     conn.close()

# def delete_provider(provider_id):
#     conn = get_connection()
#     cursor=conn.cursor()
#     query = """
#     DELETE FROM clean_Providers
#     WHERE Provider_ID = ?
#     """

#     cursor.execute(
#         query,
#         (provider_id,)
#     )

#     conn.commit()
#     conn.close()
    
# # ===================== CRUD Operation Food Listing ======================

# def get_food_listings():
#     return pd.read_csv("Food_listing_clean.csv")


# def add_food(food_name, quantity, expiry_date,
#              provider_id,provider_type,location, food_type, meal_type):
#     conn = get_connection()
#     cursor=conn.cursor()

#     query = """
#     INSERT INTO clean_Food_Listings
#     (Food_Name, Quantity, Expiry_Date,
#      Provider_ID,Provider_Type,Location, Food_Type, Meal_Type)
#     VALUES (?, ?, ?, ?, ?, ?,?,?)
#     """

#     cursor.execute(
#         query,
#         (
#             food_name,
#             quantity,
#             expiry_date,
#             provider_id,
#             provider_type,
#             location,
#             food_type,
#             meal_type
#         )
#     )

#     conn.commit()
#     conn.close()


# def update_food(food_id, quantity):
#     conn = get_connection()
#     cursor=conn.cursor()
#     query = """
#     UPDATE clean_Food_Listings
#     SET Quantity = ?
#     WHERE Food_ID = ?
#     """

#     cursor.execute(
#         query,
#         (quantity, food_id)
#     )

#     conn.commit()
#     conn.close()


# def delete_food(food_id):
#     conn = get_connection()
#     cursor=conn.cursor()
#     query = """
#     DELETE FROM clean_Food_Listings
#     WHERE Food_ID = ?
#     """

#     cursor.execute(
#         query,
#         (food_id,)
#     )

#     conn.commit()
#     conn.close()
# # ===================CURD operation for Receiver===========================
# def get_receivers():
#     return pd.read_csv("reciever_clean.csv")

# def add_receiver(name, receiver_type, city, contact):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     INSERT INTO clean_Receivers
#     (Name, Type, City, Contact)
#     VALUES (?, ?, ?, ?)
#     """

#     cursor.execute(
#         query,
#         name,
#         receiver_type,
#         city,
#         contact
#     )

#     conn.commit()
#     conn.close()
# def update_receiver(receiver_id,name,receiver_type,city,contact):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     UPDATE clean_Receivers
#     SET Name = ?,
#         Type = ?,
#         City = ?,
#         Contact = ?
#     WHERE Receiver_ID = ?
#     """

#     cursor.execute(
#         query,
#         name,
#         receiver_type,
#         city,
#         contact,
#         receiver_id
#     )

#     conn.commit()
#     conn.close()
    
# def delete_receiver(receiver_id):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     DELETE FROM clean_Receivers
#     WHERE Receiver_ID = ?
#     """

#     cursor.execute(query, receiver_id)

#     conn.commit()
#     conn.close()
# # ================================CURD operation for Claim========================================
# def get_claims():
#     return pd.read_csv("claim_clean.csv")

# def add_claim(
#     food_id,
#     receiver_id,
#     status,
#     timestamp
# ):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     INSERT INTO clean_Claims
#     (Food_ID, Receiver_ID, Status, Timestamp)
#     VALUES (?, ?, ?, ?)
#     """

#     cursor.execute(
#         query,
#         food_id,
#         receiver_id,
#         status,
#         timestamp
#     )

#     conn.commit()
#     conn.close()
    
# def update_claim(claim_id,food_id,receiver_id,status,timestamp):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     UPDATE clean_Claims
#     SET Food_ID = ?,
#         Receiver_ID = ?,
#         Status = ?,
#         Timestamp = ?
#     WHERE Claim_ID = ?
#     """

#     cursor.execute(
#         query,
#         food_id,
#         receiver_id,
#         status,
#         timestamp,
#         claim_id
#     )

#     conn.commit()
#     conn.close()
    
# def delete_claim(claim_id):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     DELETE FROM clean_Claims
#     WHERE Claim_ID = ?
#     """

#     cursor.execute(query, claim_id)

#     conn.commit()
#     conn.close()

    
    
