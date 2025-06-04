import streamlit as st
import pickle

# Load model
with open(r"C:\Users\ASUS\Desktop\akira\project_model.pkl", 'rb') as file:
    Regressor = pickle.load(file)

# Page settings
st.set_page_config(page_title="AQI Predictor 🌫️", page_icon="🌿", layout="centered")

# ---------- Custom CSS for background and font styling ----------
st.markdown("""
    <style>
    /* Background image with gradient overlay */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,80,120,0.7)),
                    url("https://images.unsplash.com/photo-1535905748047-14b8f1e9df4d?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        color: white;
    }

    /* Title and layout tweaks */
    h1, h3, .stMetric {
        color: #ffffff;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }

    .block-container {
        padding-top: 2rem;
    }

    .css-1r6slb0 {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 10px;
    }

    .stSidebar > div:first-child {
        background-color: rgba(255,255,255,0.1);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- App Title ----------
st.title("🌿 AQI Prediction ")
st.markdown("### Enter atmospheric gas levels to estimate Air Quality Index (AQI)")

# ---------- Sidebar Input ----------
st.sidebar.header("🧪 Enter Environmental Data")
SO2 = st.sidebar.number_input("🟣 SO₂ (Sulfur Dioxide)", min_value=0.0, format="%.2f", help="Concentration in µg/m³")
CO = st.sidebar.number_input("🔴 CO (Carbon Monoxide)", min_value=0.0, format="%.2f")
NO = st.sidebar.number_input("🟡 NO (Nitric Oxide)", min_value=0.0, format="%.2f")
NO2 = st.sidebar.number_input("🟠 NO₂ (Nitrogen Dioxide)", min_value=0.0, format="%.2f")
NOX = st.sidebar.number_input("🧡 NOₓ (Nitrogen Oxides)", min_value=0.0, format="%.2f")
NH3 = st.sidebar.number_input("💚 NH₃ (Ammonia)", min_value=0.0, format="%.2f")
O3 = st.sidebar.number_input("🔵 O₃ (Ozone)", min_value=0.0, format="%.2f")
WS = st.sidebar.number_input("💨 Wind Speed", min_value=0.0, format="%.2f", help="in m/s")
WD = st.sidebar.number_input("🧭 Wind Direction", min_value=0.0, format="%.2f")
RH = st.sidebar.number_input("💧 Humidity (RH)", min_value=0.0, format="%.2f", help="%")
SR = st.sidebar.number_input("🌞 Solar Radiation", min_value=0.0, format="%.2f")
TC = st.sidebar.number_input("🌡️ Temperature", min_value=0.0, format="%.2f", help="°C")

# ---------- Predict Button ----------
if st.button("🔍 Predict AQI"):
    features = [[SO2, CO, NO, NO2, NOX, NH3, O3, WS, WD, RH, SR, TC]]
    prediction = Regressor.predict(features)[0]
    rounded_pred = round(prediction, 2)

    # Display prediction
    st.markdown("## 📈 Predicted AQI")
    st.metric(label="🌫️ AQI Score", value=rounded_pred)

    # Interpretation
    if rounded_pred <= 50:
        st.success("✅ *Good Air Quality* 🌿\nEnjoy your outdoor activities!")
    elif rounded_pred <= 100:
        st.info("🟡 *Moderate Air Quality* 😷\nSensitive individuals should take care.")
    elif rounded_pred <= 150:
        st.warning("⚠️ *Unhealthy for Sensitive Groups* 😵‍💫\nLimit prolonged exposure outdoors.")
    elif rounded_pred <= 200:
        st.error("🔴 *Unhealthy* 🚨\nMinimize outdoor activity.")
    else:
        st.error("☠️ *Hazardous* 💀\nStay indoors and use air purifiers if possible.")

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:white;'>Built with ❤️ using Streamlit | © 2025 Akira AQI Project</div>",
    unsafe_allow_html=True
)
