import streamlit as st

def lab_tech_converter():
    st.title("🔬 Lab Technician Unit Converter ")

    option = [
        "Blood Sugar mg/dL to mmol/L",
        "Blood Sugar mmol/L to mg/dL",
        "Cholesterol mg/dL to mmol/L",
        "Cholesterol mmol/L to mg/dL",
        "Microliters to Milliliters",
        "Milliliters to Microliters"
    ]


    conversion_choice = st.selectbox("Select Conversion Type", options=option)
    value = st.number_input("Enter the value to convert:",min_value=0.0, format="%.2f")


    conversion_functions = {
        "Blood Sugar mg/dL to mmol/L": lambda x: x / 18.0182,
        "Blood Sugar mmol/L to mg/dL": lambda x: x * 18.0182,
        "Cholesterol mg/dL to mmol/L": lambda x: x / 38.67,
        "Cholesterol mmol/L to mg/dL": lambda x: x * 36.67,
        "Milliliters to Microliters": lambda x: x / 1000,
        "Microliters to Milliliters": lambda x: x * 1000,
    }

    if st.button("Convert"):
        result = conversion_functions[conversion_choice](value)
        st.success(f"Converted value: {result:.2f}")


   
if __name__ == "__main__":
    lab_tech_converter()


