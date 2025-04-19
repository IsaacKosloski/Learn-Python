import streamlit as st
import numpy as np
from streamlit import dataframe

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

