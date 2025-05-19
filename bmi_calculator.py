import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮")

st.title("🧮 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and see your healthy weight range based on your height.")

# Input fields
weight = st.number_input("💪 Enter your weight (kg):", min_value=10.0, max_value=200.0, step=0.1, value=0.0)
height = st.number_input("📏 Enter your height (m):", min_value=0.5, max_value=2.5, step=0.01, value=0.0)

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    min_weight = 18.5 * (height ** 2)
    max_weight = 24.9 * (height ** 2)

    st.subheader(f"📊 Your BMI is: `{bmi:.2f}`")

    if bmi < 18.5:
        st.warning("⚠️ You are **underweight**.")
    elif bmi < 25:
        st.success("✅ You are in the **normal weight** range.")
    elif bmi < 30:
        st.warning("⚠️ You are **overweight**.")
    else:
        st.error("🚨 You are **obese**.")

    st.info(f"💡 Your healthy weight range is **{min_weight:.2f} kg to {max_weight:.2f} kg**.")
