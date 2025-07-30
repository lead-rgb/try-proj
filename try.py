import streamlit as st
from pathlib import Path
import json

# 🗺️ Zoom Settings
zoom_map = {
    "➖ Small": "14px",
    "🔍 Medium": "16px",
    "➕ Large": "18px"
}

# 🖼 Background Image Setup
BACKGROUND_IMAGE = "kk.jpg"
USER_DB_FILE = "users.json"

# 🎨 Apply Background & Theme Styles
def set_background(image_file, theme):
    image_path = Path(image_file).resolve()
    if theme == "🌞 Light":
        bg_color = "#f0f0f0"
        text_color = "#000000"
        button_bg = "#ffffff"
        button_text = "#000000"
    else:
        bg_color = "#000000"
        text_color = "#ffffff"
        button_bg = "#333333"
        button_text = "#ffffff"

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            background-image: url("file://{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        html, body, [class*="css"] {{ zoom: {zoom_map[st.session_state.zoom]}; }}
        [data-testid="stSidebar"], [data-testid="stSidebar"] .block-container {{
            background-color: {bg_color};
            color: {text_color};
        }}
        h1, h2, h3, h4, h5, h6, p, label,
        .stTextInput, .stSelectbox, .stNumberInput,
        [data-testid="stSidebar"] .stRadio > div > label {{
            color: {text_color};
        }}
        .stButton > button {{
            background-color: {button_bg};
            color: {button_text};
            border: 1px solid #aaa;
            padding: 0.4em 1em;
            border-radius: 6px;
            font-weight: bold;
        }}
        </style>
    """, unsafe_allow_html=True)

# 🔐 User Data Management
def load_users():
    try:
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f)

# 🧾 Initialize Session State Defaults
for key, value in {
    "logged_in": False,
    "username": "",
    "name": "",
    "page": "Login",
    "theme": "🌞 Light",
    "zoom": "🔍 Medium",
    "signup_success": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

user_db = load_users()

# 🧭 Sidebar Navigation
if st.session_state.logged_in:
    options = [
        "Even/Odd Checker", 
        "Quadratic Solver", 
        "Area of Circle", 
        "Calculator", 
        "World Math List", 
        "Logout"
    ]
else:
    options = ["Sign Up", "Login"]

page = st.sidebar.selectbox("Navigate", options, index=options.index(st.session_state.page))

# 🎛️ Theme & Zoom Settings
if st.session_state.logged_in:
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎨 Display Settings")
    st.session_state.theme = st.sidebar.radio("Mode", ["🌞 Light", "🌙 Dark"])
    st.session_state.zoom = st.sidebar.radio("Zoom", list(zoom_map.keys()))

# 🎨 Apply Styling
set_background(BACKGROUND_IMAGE, st.session_state.theme)

# 🔐 Sign Up Page
if page == "Sign Up":
    st.title("🔐 Sign Up")

    if st.session_state.signup_success:
        st.success("✅ Successfully signed in, you can login to the page.")

    real_name = st.text_input("Full name")
    new_username = st.text_input("Choose a username")
    new_password = st.text_input("Choose a password", type="password")

    if st.button("Register"):
        if new_username in user_db:
            st.error("Username already exists.")
        elif not all([real_name, new_username, new_password]):
            st.warning("Please fill in all fields.")
        else:
            user_db[new_username] = {"name": real_name, "password": new_password}
            save_users(user_db)
            st.session_state.signup_success = True

# 🔓 Login Page
elif page == "Login":
    st.session_state.signup_success = False  # clear success message on login
    st.title("🔓 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user_info = user_db.get(username)
        if user_info and user_info["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.name = user_info["name"]
            st.session_state.page = "Even/Odd Checker"
            st.success(f"👋 Welcome back, {user_info['name']}!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

# 🔢 Even/Odd Checker
elif page == "Even/Odd Checker":
    st.title("🔢 Even or Odd Checker")
    st.write(f"👋 Hello, {st.session_state.name}!")
    number = st.number_input("Enter a number", value=0, step=1)
    if st.button("Check"):
        result = "Even ✅" if number % 2 == 0 else "Odd 🔹"
        st.success(f"{int(number)} is {result}")

# 🧮 Quadratic Solver
elif page == "Quadratic Solver":
    st.title("🧮 Quadratic Equation Solver")
    st.write("Solve ax² + bx + c = 0")
    a = st.number_input("Enter a", value=1.0)
    b = st.number_input("Enter b", value=0.0)
    c = st.number_input("Enter c", value=0.0)
    if st.button("Solve Quadratic"):
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            st.success(f"✅ Two solutions: x = {x1:.2f}, x = {x2:.2f}")
        elif d == 0:
            x = -b / (2*a)
            st.success(f"✅ One solution: x = {x:.2f}")
        else:
            st.warning("❌ No real solutions")

# 🔵 Area of Circle
elif page == "Area of Circle":
    st.title("🔵 Area of a Circle")
    radius = st.number_input("Enter radius", value=0.0)
    if st.button("Calculate Area"):
        area = 3.1416 * radius**2
        st.success(f"🟢 Area = {area:.2f}")

# ➕ Calculator
elif page == "Calculator":
    st.title("🧮 Basic Calculator")
    st.write(f"👋 Hello, {st.session_state.name}!")
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "❌ Cannot divide by zero"
        st.success(f"Result: {result}")

# 🌍 World Math List
elif page == "World Math List":
    st.title("🌍 World Math Questions")
    st.write("Explore fascinating math questions from around the globe!")

    math_questions = [
        {
            "question": "🇯🇵 What is the sum of the first 100 natural numbers?",
            "answer": "The sum is given by the formula n(n+1)/2, so 100×101/2 = **5050**"
        },
        {
            "question": "🇮🇳 What is the value of zero factorial (0!)?",
            "answer": "**0! = 1**"
        },
        {
            "question": "🇫🇷 What is the golden ratio approximately?",
            "answer": "**1.618...**, derived from (1 + √5)/2"
        },
        {
            "question": "🇺🇸 Solve for x: 2x + 5 = 13",
            "answer": "Subtract 5 then divide by 2: x = **4**"
        }
    ]

    for q in math_questions:
        st.markdown(f"**{q['question']}**  \nAnswer: {q['answer']}")
