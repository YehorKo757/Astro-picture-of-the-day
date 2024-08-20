import os
import streamlit as st
import requests


def get_image():
    api_key = st.secrets["NASA_API"]
    url = (f"https://api.nasa.gov/planetary/apod?"
           f"api_key={api_key}")
    request = requests.get(url)
    content = request.json()
    if "title" in content.keys():
        title = content["title"]
    else:
        title = "[No title]"
    if "copyright" in content.keys():
        copyright_ = content["copyright"]
    else:
        copyright_ = "[No author]"
    if "explanation" in content.keys():
        explanation = content["explanation"]
    else:
        explanation = "There is no description provided, sorry."
    img_url = content["url"]
    ext = img_url.split(".")[-1]
    image_of_the_day = requests.get(img_url).content
    with open(f"image_of_the_day.{ext}", "wb") as file:
        file.write(image_of_the_day)
    return title, copyright_, explanation, ext
