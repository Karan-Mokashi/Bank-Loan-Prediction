import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('model_pickle.pkl'))

def run():
    img1 = Image.open('bank.jpg')
    st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction ")
