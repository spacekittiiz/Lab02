# This creates the page for displaying data visualizations.
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")

data = pd.read_json("data.json", typ="series")
creatures = pd.json_normalize(data["data_points"])

# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---

fig, ax = plt.subplots()

ax.pie(
    creatures["value"],
    labels=creatures["label"]
)

ax.set_title("Magical Creature Power Levels")

st.pyplot(fig)

st.subheader("Explore Creature Power Levels")

if "creature_type" not in st.session_state:
    st.session_state.creature_type = "All"

creature_type = st.selectbox(
    "Choose a creature type:",
    ["All", "Water", "Land", "Shadows"]
)

st.session_state.creature_type = creature_type

if creature_type == "All":
    filtered_creatures = creatures
else:
    filtered_creatures = creatures[creatures["type"] == creature_type]

st.bar_chart(
    filtered_creatures,
    x="label",
    y="value"
)



# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---

survey_data = pd.read_csv("data.csv")
creature_counts = survey_data["Creature"].value_counts()

fig, ax = plt.subplots()

ax.barh(creature_counts.index, creature_counts.values)

ax.set_title("Most Popular Magical Creatures")
ax.set_xlabel("Number of Votes")
ax.set_ylabel("Magical Creature")

st.pyplot(fig)

if "creature_choice" not in st.session_state:
    st.session_state.creature_choice = "Mermaid"
    
creature_choice = st.selectbox(
    "Choose a magical creature:",
    survey_data["Creature"].unique(),
    key="creature_choice"
)

filtered_data = survey_data[survey_data["Creature"] == creature_choice]

fig, ax = plt.subplots()

ax.scatter(filtered_data["Creature"], filtered_data["Strength"])

ax.set_title("Magical Creature Strength Ratings")
ax.set_xlabel("Creature")
ax.set_ylabel("Strength (1-10)")

st.pyplot(fig)




