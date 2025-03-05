import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1518837695005-2083093ee35b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080');
        background-size: cover;
        color: white;
    }
    .stApp {
        background: rgba(20, 20, 40, 0.85); /* Dark transparent background for readability */
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 40px;
        color: white; /* Title text color updated to white */
    }
    p {
        color: white; /* Paragraph text color updated to white */
    }
    .stButton > button {
        background: linear-gradient(45deg, #1E90FF, #00BFFF); /* DodgerBlue to DeepSkyBlue gradient */
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border-radius: 12px;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 5px 20px rgba(30, 144, 255, 0.4); /* Blue shadow */
    }
    .stButton > button:hover {
        transform: scale(1.08);
        background: linear-gradient(45deg, #FFD700, #FF8C00); /* Gold to DarkOrange gradient */
        color: black;
    }
    .result-box {
        color: white;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0px 5px 20px rgba(255, 140, 0, 3); /* DarkOrange shadow */
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: white; /* Footer text color updated to white */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown("<h1>🌟 Enhanced Unit Converter using Python and Streamlit 🌟</h1>", unsafe_allow_html=True)
st.write("🚀 Now with a sleek design and an even more interactive experience! 📏✨")  # Text color set to white

# Sidebar menu
conversion_type = st.sidebar.selectbox("🔄 Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert 🌟", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("📏 From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("📏 To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("⚖️ From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("⚖️ To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("🌡️ From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("🌡️ To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value
    
# Conversion button
convert_button = st.button("✨ Convert Now!")
if convert_button:
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_conversion(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)
    st.session_state["converted"] = True

if "converted" in st.session_state and st.session_state["converted"]:
    st.write("<p style='color: white;'>✅ Conversion successful!</p>", unsafe_allow_html=True)
    st.session_state["converted"] = False

st.markdown("<div class='footer'>Made with ❤️Taimoor Hassan❤️ using Streamlit and Cursor 🚀</div>", unsafe_allow_html=True)
