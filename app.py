import streamlit as st
import pickle
import numpy as np
import pandas as pd

# load model
pipe = pickle.load(open('pipe.pkl','rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand', ['Dell','HP','Lenovo','Acer','Asus','Apple','MSI','Toshiba','Samsung'])

# type
type = st.selectbox('Type', ['Notebook','Gaming','Ultrabook','2 in 1 Convertible','Workstation','Netbook'])

# ram
ram = st.selectbox('RAM (GB)', [2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of Laptop')

# touchscreen
touchscreen = st.selectbox('Touchscreen', ['No','Yes'])

# IPS
ips = st.selectbox('IPS', ['No','Yes'])

# screen size
screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.0)

# resolution
resolution = st.selectbox('Resolution', [
    '1920x1080','1366x768','1600x900','3840x2160',
    '3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'
])

# cpu
cpu = st.selectbox('CPU', [
    'Intel Core i3','Intel Core i5','Intel Core i7',
    'Other Intel Processor','AMD Processor'
])

# storage
hdd = st.selectbox('HDD (GB)', [0,128,256,512,1024,2048])
ssd = st.selectbox('SSD (GB)', [0,8,128,256,512,1024])

# gpu
gpu = st.selectbox('GPU', ['Intel','AMD','Nvidia'])

# os
os = st.selectbox('OS', ['Windows','Mac','Others/Linux'])

# prediction
if st.button('Predict Price'):

    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

    query = pd.DataFrame([{
        'Company': company,
        'TypeName': type,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])

    prediction = np.exp(pipe.predict(query)[0])

    st.title(f"💰 Price: ₹ {int(prediction)}")