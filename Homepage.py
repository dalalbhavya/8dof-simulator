import streamlit as st
st.set_page_config(
    page_title="Top Gear",
    initial_sidebar_state="expanded"
)

st.title("Top Gear by IVDC Club IIT Indore")
st.image("data/full_width.png")

st.text("This page contains how to use this webapp to simulate the robotic arm")

st.sidebar.success("Select a page above.")