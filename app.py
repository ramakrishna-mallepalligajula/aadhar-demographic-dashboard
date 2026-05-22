import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Demographic Analytics Dashboard",
    layout="wide"
)

# Title
st.title("AI-Powered Demographic Analytics Dashboard")

# Load dataset
df = pd.read_csv("api_data_aadhar_enrolment_500000_1000000.csv")

# Create total population column
df["total_population"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)

# STATE FILTER

states = df["state"].unique()

selected_state = st.sidebar.selectbox(
    "Select State",
    states
)

# Filter state data
state_df = df[df["state"] == selected_state]


# DISTRICT FILTER


districts = state_df["district"].unique()

selected_district = st.sidebar.selectbox(
    "Select District",
    districts
)

# Filter district data
district_df = state_df[state_df["district"] == selected_district]


# STATE LEVEL ANALYTICS


st.header(f"{selected_state} State Analytics")

state_total = state_df["total_population"].sum()

state_children = state_df["age_0_5"].sum()

state_teens = state_df["age_5_17"].sum()

state_adults = state_df["age_18_greater"].sum()

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Population", state_total)

col2.metric("Children", state_children)

col3.metric("Teenagers", state_teens)

col4.metric("Adults", state_adults)


# STATE AGE DISTRIBUTION

st.subheader("State Age Distribution")

fig1, ax1 = plt.subplots()

labels = ["0-5", "5-17", "18+"]

values = [
    state_children,
    state_teens,
    state_adults
]

ax1.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

st.pyplot(fig1)


# TOP DISTRICTS


st.subheader("Top 10 Districts by Population")

top_districts = (
    state_df.groupby("district")["total_population"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_districts)


# DISTRICT ANALYTICS


st.header(f"{selected_district} District Analytics")

district_total = district_df["total_population"].sum()

district_children = district_df["age_0_5"].sum()

district_teens = district_df["age_5_17"].sum()

district_adults = district_df["age_18_greater"].sum()

# District metrics
d1, d2, d3, d4 = st.columns(4)

d1.metric("Total Population", district_total)

d2.metric("Children", district_children)

d3.metric("Teenagers", district_teens)

d4.metric("Adults", district_adults)


# DISTRICT AGE DISTRIBUTION

st.subheader("District Age Distribution")

fig2, ax2 = plt.subplots()

district_values = [
    district_children,
    district_teens,
    district_adults
]

ax2.pie(
    district_values,
    labels=labels,
    autopct="%1.1f%%"
)

st.pyplot(fig2)


# TOP PINCODES


st.subheader("Top 10 Pincodes")

top_pincodes = (
    district_df.groupby("pincode")["total_population"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_pincodes)


# RAW DATA

st.subheader("Raw Dataset")

st.dataframe(district_df.head(100))