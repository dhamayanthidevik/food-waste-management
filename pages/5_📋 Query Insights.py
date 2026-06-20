import streamlit as st
from database import load_data

data=load_data()

provider_df=data["provider_df"]
receiver_df=data["receiver_df"]
promerged_df=data["promerged_df"]
recmerge_df=data["recmerge_df"]
food_df=data["food_df"]
clamerged_df=data["clamerged_df"]

claim_df=data["claim_df"]


query_option = st.selectbox(
     "Select a Query",
    [
        "Providers by City",
        "Receivers by City",
        "Most Contributing Provider",
        "Most Claimed Food",
        "Total Food Quantity",
        "Top City by Food Listing",
        "Most Common Food Type",
        "Claims per Food Item",
        "Provider with Most Successful Claims",
        "Claim Status %",
        "Average Quantity Claimed",
        "Most Claimed Meal Type",
        "Total Donated Quantity by Provider"
    ]
)

if query_option=="Providers by City":
    result=provider_df.groupby("City").size().reset_index(name="Privider Count")
    st.dataframe(result)

if query_option=="Receivers by City":
    result=receiver_df.groupby("City").size().reset_index(name="Receiver Count")
    st.dataframe(result)
if query_option=="Most Contributing Provider":
    result=promerged_df.groupby("Name")["Quantity"].sum().reset_index()
    top_provider=result.loc[result["Quantity"].idxmax()]
    st.write(top_provider)
if query_option=="Most Claimed Food":
    result=recmerge_df.groupby("Name")["Quantity"].sum().reset_index()
    # st.dataframe(result)
    top_receiver=result.loc[result["Quantity"].idxmax()]
    st.write(top_receiver)
if query_option=="Total Food Quantity":
    result=food_df["Quantity"].sum()
    st.write(result)
if query_option=="Top City by Food Listing":
    result=food_df.groupby("Location").size().reset_index(name="Food Listing")
    top_city=result.loc[result["Food Listing"].idxmax()]
    # st.write(top_city)
    # st.dataframe(top_city)
    st.success(
        f"Top City: {top_city['Location']} ({top_city['Food Listing']} listings)"
    )
if query_option=="Most Common Food Type":
    result=food_df.groupby("Food_Type").size().reset_index(name="FoodType_Count")
    # st.dataframe(result)
    max_foodtype=result.loc[result["FoodType_Count"].idxmax()]
    # st.dataframe(max_foodtype)
    st.success(
        f"Food Type: {max_foodtype['Food_Type']} ({max_foodtype['FoodType_Count']} listings)"
    )
if query_option=="Claims per Food Item":
    result=clamerged_df.groupby("Food_Name").size().reset_index(name="Count")
    st.dataframe(result)
if query_option=="Provider with Most Successful Claims":
    provider_claims = promerged_df.merge(
    claim_df,
    on="Food_ID"
    )
    result=provider_claims[clamerged_df["Status"]=="Completed"]
    successful_provider=result.groupby("Name").size().reset_index(name="Successful Claims")
    top_provider=successful_provider.loc[successful_provider["Successful Claims"].idxmax()]
    st.success(
        f"Food Type: {top_provider['Name']} ({top_provider['Successful Claims']} listings)"
    )
if query_option=="Claim Status %":
    status_percent=(claim_df["Status"].value_counts(normalize=True)*100).reset_index()
    st.dataframe(status_percent)
    
if query_option=="Average Quantity Claimed":
    avg_quantity = clamerged_df["Quantity"].mean()

    st.metric(
        label="Average Quantity Claimed",
        value=f"{avg_quantity:.2f}"
    )
if query_option=="Most Claimed Meal Type":
    most_claim_mealtype=clamerged_df["Meal_Type"].value_counts().idxmax()
    st.metric(
    label="Most Claimed Meal Type",
    value=most_claim_mealtype
    )
if query_option=="Total Donated Quantity by Provider":
    qty_provider=promerged_df.groupby("Name")["Quantity"].sum().reset_index(name="Count")
    st.dataframe(qty_provider)

    