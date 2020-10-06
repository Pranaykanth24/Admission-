import streamlit as st
import pickle
import pandas as pd
import numpy as np
data = pd.read_csv('admission1.csv')
data.head()
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)
def predict(GS,TS,UC,S,L,C,R):
    List = [GS,TS,UC,S,L,C,R]
    array = np.array(List,np.float64)
    prediction = model.predict([array])
    return prediction
def main():
    st.title("Admissions Prediction App")
    template = """
    <div style = "background-color : skyblue; padding : 10px;">
    <h1 style = "color:white;text-align:center;> PE Predictor <h1>
    </div>
    """
    st.markdown(template,unsafe_allow_html=True)
    GS = st.text_input("GRE_Score","Type here")
    TS = st.text_input("TOEFL_Score","Type here")
    UC = st.text_input("Univercity_Rating","Type here")
    S = st.text_input("SOP","Type here")
    L = st.text_input("LOR","Type here")
    C = st.text_input("CGPA","Type here")
    R = st.text_input("Research","Type here")

    result = " "
    if st.button("predict"):
        result = predict(GS,TS,UC,S,L,C,R)
    st.success("The output is {}".format(result))
if __name__ == "__main__":
    main()
