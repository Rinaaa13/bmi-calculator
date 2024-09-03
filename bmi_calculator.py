import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100.0  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kilograms (kg)", min_value=0.0, value=70.0, step=0.1)
height_cm = st.number_input("Enter your height in centimeters (cm)", min_value=0.0, value=175.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height_cm)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25.0 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")