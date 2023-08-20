import streamlit as st
from fastai.vision.all import *

import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

import plotly.express as px


import platform

plt = platform.system()
if plt == 'Linux' : pathlib.WindowsPath = pathlib.PosixPath

# title
st.title("A model which classifies 12 types of weapons")

# Upload image
file = st.file_uploader("Upload image", type=['png', 'jpg', 'jpeg', 'gif'])
if file:
    st.image(file)
    # PIL convert
    img = PILImage.create(file)
    # model 
    model = load_learner("weapons_model.pkl")

    # prediction
    pred, pred_id, probs = model.predict(img)
    st.success(f"Prediction: {pred}")
    st.info(f"Probability: {probs[pred_id]*100:.1f}%")

    # plotting
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)


