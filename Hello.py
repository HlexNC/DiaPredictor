import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

@st.cache_data
def open_database():
    data = pd.read_csv("cat_to_num.csv")
    return data

data = open_database()
# Display data as a table
st.write("### Data Table")
st.dataframe(data)

# Display statistics
st.write("### Data Statistics")
st.write("Basic descriptive statistics for the data:")
st.write(data.describe())

# Custom statistics
st.write("### Custom Statistics")
st.write("Median values of each column:")
st.write(data.median())

st.write("Mode values of each column:")
st.write(data.mode().iloc[0])  # mode() returns a DataFrame

# Optional: Correlation matrix for numerical data
st.write("### Correlation Matrix")
st.write(data.corr())

