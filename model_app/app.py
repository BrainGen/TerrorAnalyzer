import joblib
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_resource
def load_model():
  return joblib.load(r"linear_regression_model.pkl")

model = load_model()
st.title("Try out TerrorPredictor: A Linear Regression Project")
st.write("Enter your values to generate a prediction below. Each value is country specific. For example, No. of terrorism victims in the previous year refers to only one country's data")
st.write("Disclaimer: This is an independent data science exploration and hobbyist project utilizing historical open-source conflict data. The predictive outputs are experimental, lack real-world validation, and are strictly intended for academic and technical demonstration. They must not be used for security analysis, operational forecasting, or decision-making. All data used in the training of this project is open-source. This model is known to be inaccurate, and hence must be used for mundane purposes only.")
with st.form("prediction-form"):
  
    nkilldelay1 = st.number_input("No. of terrorism victims (deaths) in the previous year")
    nkilldelay2 = st.number_input("No of terrorism victims (deaths) in the year before last")
    deaths_civilians = st.number_input("No. of civilian killings (intentional, by combatants) in the previous year")
    submitted = st.form_submit_button("Run Prediction")

if submitted:
    input_data = pd.DataFrame([{
      'deaths_civilians': np.log1p(deaths_civilians),
      'nkilldelay1': np.log1p(nkilldelay1),
      'nkilldelay2': np.log1p(nkilldelay2)
  }])
    try:
    # Extract and explicitly cast to a Python scalar float
        raw_pred = model.predict(input_data)
        prediction = float(np.ravel(np.expm1(raw_pred))[0])

        st.success(f"### Predicted Terrorism Victims: {prediction:.4f}")

        st.caption("Input passed to model:")
        st.dataframe(input_data)

    except Exception as e:
        st.error(f"Inference failed: {e}")
  