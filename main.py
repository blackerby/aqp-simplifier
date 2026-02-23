import aqpy
import streamlit as st


TITLE = "Legislation Text Query Simplifier"

st.set_page_config(TITLE, layout="wide")
st.title(TITLE)

query = st.text_input("Query", "+hello +world")
try:
    simplified = aqpy.simplify(query)
    st.write("Simplified query:", simplified)
except:
    st.write("Invalid query")

