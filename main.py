import streamlit as st
from astro_image_of_the_day import get_image

st.set_page_config(layout="wide")

title, copyright_, explanation,  ext = get_image()

if copyright_ != "[No author]":
    st.title(f"{title} by {copyright_}")
else:
    st.title(f"{title}")

st.image(f"image_of_the_day.{ext}")
st.write(f"<div style='text-align: justify'>{explanation}. </div>",
         unsafe_allow_html=True)
