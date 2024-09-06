import streamlit as st
import pickle
model = pickle.load(open("Titanic_Prediction.pkl",'rb'))

def my_model():
    st.title("Titanic Survival Prediction")
    Pclass = st.text_input("Enter the Passenger Class")
    Age = st.text_input("Enter the Passenger Age")
    Gender = st.text_input("Enter the Passenger Gender 'Male':1, 'Female':0")
    pred = st.button("Predict")


    if pred:
        result = model.predict([[int(Pclass),int(Age),int(Gender)]])
        if result:
            st.write("This person is Survived")
        else:
            st.write("This person is not Survived")
my_model()