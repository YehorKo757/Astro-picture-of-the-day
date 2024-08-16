import os
import streamlit as st
import requests


def get_image():
    api_key = st.secrets["NASA_API"]
    url = (f"https://api.nasa.gov/planetary/apod?"
           f"api_key={api_key}")
    request = requests.get(url)
    content = request.json()
    title = content["title"]
    copyright_ = content["copyright"]
    explanation = content["explanation"]
    img_url = content["url"]
    ext = img_url.split(".")[-1]
    image_of_the_day = requests.get(img_url).content
    with open(f"image_of_the_day.{ext}", "wb") as file:
        file.write(image_of_the_day)
    return title, copyright_, explanation, ext
