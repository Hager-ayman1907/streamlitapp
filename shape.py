import streamlit as st
import time

st.header("Shapes Calculation")

shape = st.selectbox("Choose Shape: ", ["Circle", "Rectangle"]) 


st.sidebar.title("Configuratin")

#with st.sidebar:
#   shape = st.selectbox("Choose Shape: ", ["Circle", "Rectangle"])


if shape == "Circle":
    radius = st.number_input('Radius:', min_value=0.0, max_value=100.0, step=0.01)
    area = radius * radius * 3.14
    parimeter =  2 * 3.14 * radius

if shape == "Rectangle":
    width = st.number_input("Width", 0., step=0.1)
    height = st.number_input("Hieght", 0., step=0.1)
    area = width * height
    parimeter = 2 * (width + height)

compute_btn = st.button("Compute area and parimeter")
if compute_btn:
    with st.spinner("Computing..."):
        time.sleep(1)
        st.write("Area", area)
        st.write("Parimeter", parimeter)


## streamlit run hello.py

