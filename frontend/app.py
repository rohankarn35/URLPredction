import streamlit as st
from features import main
import pickle
import numpy  as np

model = pickle.load(open('model_phish.pkl','rb'))
st.title("URL Prediction",)
yy=st.text_input("Enter")
def predict():
    pred = model.predict(np.array(main(yy)).reshape((1,-1)))

    if  int(pred[0]) == 0:
        st.success('Safe URL')
    elif int(pred[0]) == 3:
        st.success('Safe URL')
    else:
        st.error('Unsafe URL')
st.button("Predict", on_click=predict)