from database import load_data
import streamlit as st

data = load_data()

food_df=data["food_df"]
promerged_df=data["promerged_df"]
recmerge_df=data["recmerge_df"]
clamerged_df=data["clamerged_df"]
claim_df=data["claim_df"]


st.title("📊 Food Wastage Analysis")

# 1. Food Availability
city_food = food_df.groupby('Location')['Quantity'].sum().reset_index()
top_city = city_food.loc[city_food['Quantity'].idxmax()]

# 2. Food Waste
meal_waste = food_df.groupby('Meal_Type')['Quantity'].sum().reset_index()
top_meal = meal_waste.loc[meal_waste['Quantity'].idxmax()]

# 3. Provider Analysis
provider_food = promerged_df.groupby('Name')['Quantity'].sum().reset_index()
top_provider = provider_food.loc[provider_food['Quantity'].idxmax()]

# 4. Receiver Analysis
receiver_claims = recmerge_df.groupby('Name')['Quantity'].sum().reset_index()
top_receiver = receiver_claims.loc[receiver_claims['Quantity'].idxmax()]

# 5. Claims Analysis
completed = claim_df[claim_df['Status'] == 'Completed'].shape[0]
total_claims = claim_df.shape[0]

completion_percentage = (completed / total_claims) * 100

# 6. Demand Analysis
city_demand = clamerged_df.groupby('Location')['Quantity'].sum().reset_index()
top_city_demand = city_demand.loc[city_demand['Quantity'].idxmax()]


def show_card(title, label1, value1, label2, value2):
# def show_card():
    # st.markdown("<h1>Hello</h1>", unsafe_allow_html=True)
    # st.markdown(f"""
    
    #     <h3>{title}</h3>

    #     <p>{label1}</p>
    #     <h1>{value1}</h1>

    #     <p>{label2}</p>
    #     <h1>{value2}</h1>
    # </div>
    # """, unsafe_allow_html=True)
    st.subheader(title)
    st.write(label1)
    st.header(value1)
    st.write(label2)
    st.header(value2)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
    <h3>🍱 Food Availability</h3>
    <p style="font-size:20px;font-weight:bold;">City with Most Food</p>
    <h6>{top_city['Location']}</h6>
    <p style="font-size:20px;font-weight:bold;">Total Quantity</p>
    <h6>{top_city['Quantity']}</h6>
    
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
    <h3>🗑️ Food Waste</h3>
    <p style="font-size:20px;font-weight:bold;">Meal type with the most food waste</p>
    <h6>{top_meal['Meal_Type']}</h6>
    <p style="font-size:20px;font-weight:bold;">Total Quantity</p>
    <h6>{int(top_meal['Quantity'])}</h6>
    
</div>
""", unsafe_allow_html=True)

    # st.subheader("🗑️ Food Waste")
    # st.metric(
    #     label="Meal type with the most food waste",
    #     value=top_meal['Meal_Type']
    # )

    # st.metric(
    #     label="Total Quantity",
    #     value=int(top_meal['Quantity'])
    # )
with col3:
     st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
    <h3>🏢 Provider Analysis</h3>
    <p style="font-size:20px;font-weight:bold;">Top Contributing Provider</p>
    <h6>{top_provider['Name']}</h6>
    <p style="font-size:20px;font-weight:bold;">Total Quantity</p>
    <h6>{int(top_provider['Quantity'])}</h6>
    
</div>
""", unsafe_allow_html=True)

   
    # st.subheader("🏢 Provider Analysis")
    # st.metric(
    #     label="Top Contributing Provider",
    #     value=top_provider['Name']
    # )

    # st.metric(
    #     label="Total Quantity",
    #     value=int(top_provider['Quantity'])
    # )
col4, col5, col6 = st.columns(3)

with col4:
    
    # st.subheader("🙋 Receiver Analysis")
    # st.metric(
    #     label="Top Receiver",
    #     value=top_receiver['Name']
    # )

    # st.metric(
    #     label="Total Quantity",
    #     value=int(top_receiver['Quantity'])
    # )
    st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
        <h3>🙋 Receiver Analysis</h3>
        <p style="font-size:20px;font-weight:bold;">Top Receiver</p>
        <h6>{top_receiver['Name']}</h6>
        <p style="font-size:20px;font-weight:bold;">Total Quantity</p>
        <h6>{int(top_receiver['Quantity'])}</h6>
        
    </div>
    """, unsafe_allow_html=True)


with col5:
    st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
        <h3>✅ Claims Analysis</h3>
        <p style="font-size:20px;font-weight:bold;">Claim Completion Rate</p>
        <h6>{f"{completion_percentage:.2f}%"}</h6>
        
    </div>
    """, unsafe_allow_html=True)

#     st.subheader("✅ Claims Analysis")
#     st.metric(
#     label="Claim Completion Rate",
#     value=f"{completion_percentage:.2f}%"
# )

with col6:
    st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
        ">
        <h3>📈 Demand Analysis</h3>
        <p style="font-size:20px;font-weight:bold;">City with Highest Food Demand</p>
        <h6>{top_city_demand['Location']}</h6>
        <p style="font-size:20px;font-weight:bold;">Total Quantity Claimed</p>
        <h6>{int(top_city_demand['Quantity'])}</h6>
        
        
    </div>
    """, unsafe_allow_html=True)

#     st.subheader("📈 Demand Analysis")
#     st.metric(
#         label="City with Highest Food Demand",
#         value=top_city_demand['Location']
#     )

#     st.metric(
#         label="Total Quantity Claimed",
#         value=int(top_city_demand['Quantity'])
#     )

    
# st.write("END OF PAGE")