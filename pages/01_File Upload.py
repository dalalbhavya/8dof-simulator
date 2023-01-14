import streamlit as st
st.set_page_config(
    page_title="Upload Files",
    initial_sidebar_state="expanded"
)

st.title("File Upload")

#Add Environment File
env_config_csv = st.file_uploader("Choose Environment CSV file")

#Add Trajectory File
traj_csv = st.file_uploader("Choose Trajectory CSV file")
