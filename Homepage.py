import streamlit as st
st.set_page_config(
    page_title="Top Gear",
    initial_sidebar_state="expanded"
)
readme_path = "README.md"
readme_file = open(readme_path, "r")

while True:
    line = readme_file.readline()
    st.markdown(line)

    if not line:
        break

readme_file.close()

st.title("Top Gear by IVDC Club IIT Indore")
st.image("data/full_width.png")
st.markdown("![foo](README.md, 'title')")

st.text("This page contains how to use this webapp to simulate the robotic arm")

st.sidebar.success("Select a page above.")