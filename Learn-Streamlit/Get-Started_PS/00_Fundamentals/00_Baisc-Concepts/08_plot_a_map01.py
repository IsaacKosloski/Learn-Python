import streamlit as st
import pandas as pd
import numpy as np

# Convert DMS to Decimal Degrees
latitude  = - (20 + (26 / 60) + (34 / 3600))  # South = negative
longitude = - (53 + (45 / 60) + (32 / 3600))  # West = negative

# Create DataFrame centered at the specified location
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [100, 100] + [latitude, longitude],
    columns=['lat', 'lon'])

st.title("Map centered at 20°26'34\" S, 53°45'32\" W")
st.map(map_data)