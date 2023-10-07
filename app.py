import requests
import streamlit as st
import pandas as pd


def main():
    st.set_page_config(page_title="Bangalore Price Prediction App", page_icon=":house:")

    # Navigation bar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About"])

    if page == "Home":
        show_home()
    elif page == "About":
        show_about()


def show_home():
    st.title("Bangalore Price Prediction App")

    total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1500)
    location = st.text_input("Location")
    bhk = st.number_input("BHK", min_value=1, max_value=5, value=3, step=1, format="%d")
    bath = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2, step=1, format="%d")

    if st.button("Predict Price"):
        estimated_price = predict_price(location, total_sqft, bhk, bath)
        estimated_price_display = format_price(abs(estimated_price))
        st.success(f"Estimated Price: {estimated_price_display}")


def format_price(price):
    if price > 100:
        return f"{price / 100:.2f} Crores INR"
    else:
        return f"{price} Lacks INR"


def show_about():
    st.title("About Bangalore Price Prediction App")

    st.write(
        "Welcome to the Bangalore Price Prediction App! This app uses a Linear Regression model to predict house "
        "prices in Bangalore.")

    st.subheader("Model Information")
    st.write("The model used here is Linear Regression.")

    st.subheader("Dataset Information")
    st.write("The dataset used for training the model is the Bangalore house dataset.")

    st.subheader("Model Comparison")
    comparison_data = {
        'Model': ['Linear Regression', 'Lasso', 'Decision Tree'],
        'Best Score': [0.819001, 0.687464, 0.715887],
    }
    st.write(pd.DataFrame(comparison_data).set_index('Model'))


def predict_price(location, total_sqft, bhk, bath):
    payload = {
        'total_sqft': total_sqft,
        'location': location,
        'bhk': bhk,
        'bath': bath
    }

    response = requests.post("https://house-price-prediction-nrcv.streamlit.app/predict_home_price", data=payload)
    data = response.json()
    return data['estimated_price']


if __name__ == '__main__':
    main()
