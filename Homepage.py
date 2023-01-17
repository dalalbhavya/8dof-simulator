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

st.sidebar.success("Select a page above.")

#Add all button to download all the formats

with open("data/test_input.csv", "rb") as file:
    st.markdown("Input CSV File")
    btn = st.download_button(
            label="Download",
            data=file,
            file_name="test_input.csv"
          )
    
with open("data/test_env_config.csv", "rb") as file:
    st.markdown("Environment Configuration CSV File")
    btn = st.download_button(
            label="Download",
            data=file,
            file_name="test_env_config.csv"
          )
with open("data/test_traj.csv", "rb") as file:
    st.markdown("Trajectory CSV File")
    btn = st.download_button(
            label="Download",
            data=file,
            file_name="test_traj.csv"
          )