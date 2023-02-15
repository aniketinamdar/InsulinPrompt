import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = pickle.load(open("my_classifier.pickle", "rb"))


def tell_units(blood_sugar, time):
    input = np.array([[time, blood_sugar]]).astype(np.float64)
    prediction = pickle_in.predict(input)

    return int(prediction)


def main():
    st.title('Insulin Dosage ')
    blood_sugar = st.text_input("Blood Sugar", "")
    time = st.text_input("Breakfast(0), Lunch(2), Dinner(1) : ", "")
    if st.button("Tell me the insulin units"):
        output = tell_units(blood_sugar, time)
        st.success('Units to take : {}'.format(output))


if __name__ == '__main__':
    main()
