import streamlit as st
import pandas as pd

from database import (
    load_data,
    add_provider,
    update_provider,
    delete_provider, 
    get_providers,
    get_food_listings,
    add_food,
    update_food,
    delete_food,
    get_receivers,
    add_receiver,
    update_receiver,
    delete_receiver,
    get_claims,
    add_claim,
    update_claim,
    delete_claim,
)
claim_df = get_claims()
food_df = get_food_listings()
receiver_df = get_receivers()

# from database import get_food_listings
# from database import (
#     add_food,
#     update_food,
#     delete_food,
#     get_food_listings
# )

st.title("CRUD Operations")

table = st.selectbox(
    "Select Table",
    ["Providers", "Receivers", "Food Listings", "Claims"]
)

operation = st.radio(
    "Select Operation",
    ["Create", "Read", "Update", "Delete"],
    horizontal=True
)

if table == "Providers":

    if operation == "Create":
        st.subheader("Add Providers")
        name = st.text_input("Name")
        provider_type = st.text_input("Type")
        Address = st.text_input("Address")
        city = st.text_input("City")
        contact = st.text_input("Contact")

        if st.button("Add"):
            add_provider(
                name,
                provider_type,
                Address,
                city,
                contact
            )
            st.success("Provider Added")

    elif operation == "Read":
        st.subheader("View Providers")
        st.dataframe(get_providers())

    elif operation == "Update":
        st.subheader("Update Providers")
        provider_id = st.number_input(
        "Provider ID",
        min_value=1
        )

        city = st.text_input("New City")

        if st.button("Update"):
            update_provider(provider_id, city)
            st.success("Provider Updated")

    elif operation == "Delete":
        st.subheader("Delete Providers")
        provider_id = st.number_input(
        "Provider ID",
        min_value=1
        )

        if st.button("Delete"):
            delete_provider(provider_id)
            st.success("Provider Deleted")
        
    # ====================Food listing=====================
if table == "Food Listings":
    if operation == "Create":

        st.subheader("Add Food Item")

        food_name = st.text_input("Food Name")
        quantity = st.number_input("Quantity", min_value=1)
        expiry_date = st.date_input("Expiry Date")
        provider_df = get_providers()

        provider_id = st.selectbox(
            "Provider ID",
            provider_df["Provider_ID"]
        )

        selected_provider = provider_df[
            provider_df["Provider_ID"] == provider_id
        ].iloc[0]

        provider_type = selected_provider["Type"]
        location = selected_provider["City"]

        st.text_input(
            "Provider Type",
            value=provider_type,
            disabled=True
        )

        st.text_input(
            "Location",
            value=location,
            disabled=True
        )

        food_type = st.selectbox(
            "Food Type",
            ["Vegetarian", "Non-Vegetarian"]
        )

        meal_type = st.selectbox(
            "Meal Type",
            ["Breakfast", "Lunch", "Dinner", "Snacks"]
        )

        if st.button("Add Food"):
            add_food(food_name, quantity, expiry_date,
            provider_id,provider_type,location, food_type, meal_type)

            st.success("Food Item Added Successfully!")
    
    elif operation == "Read":
        st.subheader("View Food Listing")
        # st.dataframe(get_providers())
        st.dataframe(get_food_listings())
        
    elif operation == "Update":
        food_df=get_food_listings()
        food_ids = food_df["Food_ID"].tolist()

        selected_food_id = st.selectbox(
            "Select Food ID",
            food_ids
        )

        row = food_df[
            food_df["Food_ID"] == selected_food_id
        ].iloc[0]

        food_name = st.text_input(
            "Food Name",
            value=row["Food_Name"]
        )

        quantity = st.number_input(
            "Quantity",
            value=int(row["Quantity"]),
            min_value=1
        )

        expiry_date = st.date_input(
            "Expiry Date",
            value=row["Expiry_Date"]
        )

        if st.button("Update"):
            update_food(
                selected_food_id,
                food_name,
                quantity,
                expiry_date
            )

            st.success("Food item updated successfully")
    

    elif operation == "Delete":

        st.subheader("Delete Food Item")
        food_df=get_food_listings()
        food_ids = food_df["Food_ID"].tolist()

        selected_food_id = st.selectbox(
            "Select Food ID",
            food_ids
        )

        if st.button("Delete Food Item"):

            delete_food(selected_food_id)

            st.success("Food item deleted successfully!")
if table == "Receivers":

    if operation == "Create":
        st.subheader("Add Receiver")

        name = st.text_input("Name")
        receiver_type = st.text_input("Type")
        city = st.text_input("City")
        contact = st.text_input("Contact")

        if st.button("Add Receiver"):

            add_receiver(
                name,
                receiver_type,
                city,
                contact
            )

            st.success("Receiver added successfully")
            
    elif operation == "Read":

        st.subheader("Receiver Details")
        receiver_df=get_receivers()
        st.dataframe(receiver_df)
    
    elif operation == "Update":

        st.subheader("Update Receiver")
        receiver_df=get_receivers()
        receiver_id = st.selectbox(
            "Select Receiver ID",
            receiver_df["Receiver_ID"]
        )

        row = receiver_df[
            receiver_df["Receiver_ID"] == receiver_id
        ].iloc[0]

        name = st.text_input(
            "Name",
            value=row["Name"]
        )

        receiver_type = st.text_input(
            "Type",
            value=row["Type"]
        )

        city = st.text_input(
            "City",
            value=row["City"]
        )

        contact = st.text_input(
            "Contact",
            value=str(row["Contact"])
        )

        if st.button("Update Receiver"):

            update_receiver(
                receiver_id,
                name,
                receiver_type,
                city,
                contact
            )

            st.success("Receiver updated successfully")
            
    elif operation == "Delete":

        st.subheader("Delete Receiver")
        receiver_df=get_receivers()
        receiver_id = st.selectbox(
            "Select Receiver ID",
            receiver_df["Receiver_ID"]
        )

        row = receiver_df[
            receiver_df["Receiver_ID"] == receiver_id
        ].iloc[0]

        st.write("Name:", row["Name"])
        st.write("City:", row["City"])

        if st.button("Delete Receiver"):

            delete_receiver(receiver_id)

            st.success("Receiver deleted successfully")
# =========================CURD operation for Claim================================================
if table == "Claims":
    if operation == "Create":

        st.subheader("Add Claim")

        food_id = st.selectbox(
            "Food ID",
            food_df["Food_ID"]
        )

        receiver_id = st.selectbox(
            "Receiver ID",
            receiver_df["Receiver_ID"]
        )

        status = st.selectbox(
            "Status",
            ["Pending", "Completed", "Cancelled"]
        )

        timestamp = st.datetime_input(
            "Timestamp"
        )

        if st.button("Add Claim"):

            add_claim(
                food_id,
                receiver_id,
                status,
                timestamp
            )

            st.success("Claim added successfully")
            st.rerun()
    elif operation == "Read":

        st.subheader("Claim Details")

        st.dataframe(claim_df)
    elif operation == "Update":

        st.subheader("Update Claim")

        claim_id = st.selectbox(
            "Select Claim ID",
            claim_df["Claim_ID"]
        )

        row = claim_df[
            claim_df["Claim_ID"] == claim_id
        ].iloc[0]

        food_id = st.selectbox(
            "Food ID",
            food_df["Food_ID"],
            index=food_df["Food_ID"].tolist().index(row["Food_ID"])
        )

        receiver_id = st.selectbox(
            "Receiver ID",
            receiver_df["Receiver_ID"],
            index=receiver_df["Receiver_ID"].tolist().index(row["Receiver_ID"])
        )

        status = st.selectbox(
            "Status",
            ["Pending", "Completed", "Cancelled"],
            index=["Pending", "Completed", "Cancelled"].index(row["Status"])
        )

        timestamp = st.datetime_input(
            "Timestamp",
            value=row["Timestamp"]
        )

        if st.button("Update Claim"):

            update_claim(
                claim_id,
                food_id,
                receiver_id,
                status,
                timestamp
            )

            st.success("Claim updated successfully")
            st.rerun()
        
    elif operation == "Delete":

        st.subheader("Delete Claim")

        claim_id = st.selectbox(
            "Select Claim ID",
            claim_df["Claim_ID"]
        )

        row = claim_df[
            claim_df["Claim_ID"] == claim_id
        ].iloc[0]

        st.write("Food ID:", row["Food_ID"])
        st.write("Receiver ID:", row["Receiver_ID"])
        st.write("Status:", row["Status"])

        if st.button("Delete Claim"):

            delete_claim(claim_id)

            st.success("Claim deleted successfully")
            st.rerun()