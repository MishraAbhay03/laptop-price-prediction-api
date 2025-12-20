import streamlit as st
import requests

API_URL = "https://laptop-price-prediction-api-production.up.railway.app/"

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Prediction")
st.markdown("Predict laptop prices using a machine learning model.")

st.divider()

# -----------------------------
# Input Fields
# -----------------------------

company = st.selectbox("Brand", ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"])
product = st.text_input("Product Name", "Inspiron 15")
typename = st.selectbox("Laptop Type", ["Notebook", "Ultrabook", "Gaming", "Workstation"])

inches = st.slider("Screen Size (inches)", 11.0, 18.0, 15.6)
screenresolution = st.selectbox(
    "Screen Resolution",
    ["1366x768", "1920x1080", "2560x1440", "3840x2160"]
)

cpu_company = st.selectbox("CPU Brand", ["Intel", "AMD", "Apple"])
cpu_type = st.selectbox("CPU Type", ["Core i3", "Core i5", "Core i7", "Ryzen 5", "Ryzen 7", "M1", "M2"])
cpu_frequency_ghz = st.slider("CPU Frequency (GHz)", 1.0, 5.0, 2.4)

ram_gb = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
memory = st.selectbox(
    "Storage",
    ["256GB SSD", "512GB SSD", "1TB SSD", "1TB HDD"]
)

gpu_company = st.selectbox("GPU Brand", ["Intel", "Nvidia", "AMD", "Apple"])
gpu_type = st.selectbox("GPU Type", ["Integrated", "GTX", "RTX"])

opsys = st.selectbox("Operating System", ["Windows 10", "Windows 11", "Mac OS", "Linux"])
weight_kg = st.slider("Weight (kg)", 0.8, 3.5, 1.9)

st.divider()

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Price", use_container_width=True):
    payload = {
    "company": company,
    "product": product,  # MUST exist
    "typename": typename,
    "inches": float(inches),
    "screenresolution": screenresolution,
    "cpu_company": cpu_company,
    "cpu_type": cpu_type,
    "cpu_frequency_ghz": float(cpu_frequency_ghz),
    "ram_gb": int(ram_gb),
    "memory": memory,
    "gpu_company": gpu_company,
    "gpu_type": gpu_type,
    "opsys": opsys,
    "weight_kg": float(weight_kg)
}

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            price = response.json()["predicted_price"]
            st.success(f"💰 Estimated Price: ₹ {price:,.0f}")
        else:
            st.error("❌ Prediction failed. Check API logs.")

    except Exception as e:
        st.error(f"🚨 Error connecting to API: {e}")
