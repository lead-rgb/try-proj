import streamlit as st
from pathlib import Path
import json

# 🌐 Font Size Options
zoom_map = {
    "➖ Small": "14px",
    "🔍 Medium": "16px",
    "➕ Large": "18px"
}

BACKGROUND_IMAGE = "kk.jpg"
USER_DB_FILE = "users.json"

# 🎨 Enhanced Styling with Smooth Transitions
def set_background(image_file, theme):
    image_path = Path(image_file).resolve()
    font_size = zoom_map[st.session_state.zoom]

    if theme == "🌞 Light":
        bg_color = "#17f6f6"
        text_color = "#861fee"
        secondary_bg = "#27b7eb"
        button_bg = "#3182ce"
        button_text = "#a313f7"
        input_bg = "#ffffff"
        border_color = "#8911d3"
        shadow = "0 4px 6px rgba(0,0,0,0.1)"
        placeholder_color = "#718096"
    else:
        bg_color = "#10f0de"
        text_color = "#366b76"
        secondary_bg = "#1ff2c1"
        button_bg = "#D7590B"
        button_text = "#11EFCE"
        input_bg = "#ffffff"
        border_color = "#db6825"
        shadow = "0 4px 6px rgba(0,0,0,0.3)"
        placeholder_color = "#8b949e"

    st.markdown(f"""
        <style>
        /* Global forced visibility for all elements */
        *, *::before, *::after {{
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        /* Force text visibility in dark mode */
        body, html, div, span, p, a, label, input, textarea, select, button,
        h1, h2, h3, h4, h5, h6, li, ul, ol, td, th, tr, table {{
            color: {text_color} !important;
            opacity: 1 !important;
            visibility: visible !important;
            -webkit-text-fill-color: {text_color} !important;
        }}
        
        /* Streamlit specific element visibility */
        .stApp, .stApp *, .main, .main *, .block-container, .block-container *,
        [data-testid] *, .stMarkdown *, .stForm *, .stButton *, 
        .stTextInput *, .stNumberInput *, .stSelectbox *, .stRadio * {{
            color: {text_color} !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        /* Override any framework hiding */
        .sr-only, .visually-hidden, [hidden], [style*="display: none"],
        [style*="visibility: hidden"], [style*="opacity: 0"] {{
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            color: {text_color} !important;
        }}
        
        html, body, .stApp {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
            font-size: {font_size} !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        }}
        
        .stApp {{
            background-image: url("file://{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Main Container */
        .block-container, .main {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
            border-radius: 10px;
            box-shadow: {shadow};
        }}
        
        /* Header and Toolbar */
        [data-testid="stHeader"], [data-testid="stToolbar"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        
        /* Typography with Forced Visibility */
        h1, h2, h3, h4, h5, h6 {{
            color: {text_color} !important;
            font-size: calc({font_size} + 4px) !important;
            font-weight: 800 !important;
            margin-bottom: 1.2rem !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
            line-height: 1.3 !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        h1 {{
            font-size: calc({font_size} + 12px) !important;
            text-align: center !important;
            color: {text_color} !important;
            text-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
        }}
        
        p, label, .markdown-text-container, .stMarkdown, .stMarkdown p {{
            color: {text_color} !important;
            font-size: {font_size} !important;
            line-height: 1.7 !important;
            font-weight: 600 !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        /* Force all text elements to be visible */
        * {{
            color: {text_color} !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        /* Override any hidden text */
        .stTextInput label, .stNumberInput label, .stSelectbox label, 
        .stRadio label, .stForm label, label {{
            color: {text_color} !important;
            font-weight: 700 !important;
            font-size: calc({font_size} + 2px) !important;
            margin-bottom: 8px !important;
            opacity: 1 !important;
            visibility: visible !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
        }}
        
        /* Enhanced divider visibility */
        hr, .stDivider {{
            border: none !important;
            height: 3px !important;
            background: linear-gradient(90deg, transparent, {text_color}60, transparent) !important;
            margin: 2rem 0 !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        /* Input Fields with Maximum Visibility for Dark Mode */
        .stTextInput input, .stNumberInput input, .stTextArea textarea {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
            border: 2px solid {border_color} !important;
            border-radius: 8px !important;
            font-size: {font_size} !important;
            font-weight: 600 !important;
            padding: 12px !important;
            box-shadow: {shadow} !important;
            caret-color: {text_color} !important;
            -webkit-text-fill-color: {text_color} !important;
            -webkit-box-shadow: 0 0 0px 1000px {input_bg} inset !important;
            opacity: 1 !important;
        }}
        
        .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {{
            border-color: {button_bg} !important;
            box-shadow: 0 0 0 3px rgba(35, 134, 54, 0.3), inset 0 0 0px 1000px {input_bg} !important;
            outline: none !important;
            caret-color: {button_bg} !important;
            color: {text_color} !important;
            -webkit-text-fill-color: {text_color} !important;
        }}
        
        .stTextInput input::placeholder, .stNumberInput input::placeholder, .stTextArea textarea::placeholder {{
            color: {placeholder_color} !important;
            opacity: 0.8 !important;
            font-weight: 500 !important;
        }}
        
        /* Force text visibility in all browsers */
        .stTextInput input:-webkit-autofill,
        .stTextInput input:-webkit-autofill:hover,
        .stTextInput input:-webkit-autofill:focus,
        .stTextInput input:-webkit-autofill:active {{
            -webkit-box-shadow: 0 0 0px 1000px {input_bg} inset !important;
            -webkit-text-fill-color: {text_color} !important;
            caret-color: {text_color} !important;
            color: {text_color} !important;
            background-color: {input_bg} !important;
        }}
        
        /* Input container styling */
        .stTextInput > div > div, .stNumberInput > div > div {{
            background-color: {input_bg} !important;
            border-radius: 8px !important;
        }}
        
        /* Select Boxes and Radio Buttons with Enhanced Visibility */
        .stSelectbox > div, .stRadio div {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
            border-radius: 8px !important;
            border: 2px solid {border_color} !important;
        }}
        
        .stSelectbox > div > div {{
            color: {text_color} !important;
            background-color: {input_bg} !important;
        }}
        
        .stSelectbox option {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
        }}
        
        .stRadio div label {{
            color: {text_color} !important;
            font-size: {font_size} !important;
            padding: 8px 12px !important;
            border-radius: 6px !important;
            background-color: {secondary_bg} !important;
            margin: 4px !important;
            cursor: pointer !important;
        }}
        
        .stRadio div label:hover {{
            background-color: {button_bg}20 !important;
            transform: translateY(-1px) !important;
        }}
        
        /* Enhanced Form Labels */
        .stTextInput label, .stNumberInput label, .stSelectbox label {{
            color: {text_color} !important;
            font-weight: 600 !important;
            font-size: {font_size} !important;
            margin-bottom: 8px !important;
        }}
        
        /* Enhanced Buttons with High Visibility */
        .stButton > button {{
            background: linear-gradient(135deg, {button_bg}, #5dade2) !important;
            color: {button_text} !important;
            font-size: {font_size} !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
            padding: 14px 28px !important;
            border: 2px solid {button_bg} !important;
            box-shadow: {shadow}, 0 0 20px rgba(74, 144, 226, 0.2) !important;
            transform: translateY(0px) !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            cursor: pointer !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 8px 25px rgba(74, 144, 226, 0.4), 0 0 30px rgba(74, 144, 226, 0.3) !important;
            background: linear-gradient(135deg, #5dade2, {button_bg}) !important;
        }}
        
        .stButton > button:active {{
            transform: translateY(-1px) scale(0.98) !important;
            box-shadow: 0 2px 10px rgba(74, 144, 226, 0.3) !important;
        }}
        
        /* Special styling for theme toggle buttons */
        button[key*="light"], button[key*="dark"] {{
            min-width: 120px !important;
            font-size: 16px !important;
            background: linear-gradient(135deg, {button_bg}, #74b9ff) !important;
            border: 2px solid {text_color}40 !important;
            box-shadow: 0 4px 15px rgba(116, 185, 255, 0.3) !important;
        }}
        
        /* Form submit buttons enhancement */
        button[kind="formSubmit"] {{
            background: linear-gradient(135deg, #00b894, #00cec9) !important;
            border: 2px solid #00b894 !important;
            box-shadow: 0 4px 15px rgba(0, 184, 148, 0.3) !important;
        }}
        
        button[kind="formSubmit"]:hover {{
            background: linear-gradient(135deg, #00cec9, #00b894) !important;
            box-shadow: 0 8px 25px rgba(0, 184, 148, 0.4) !important;
        }}
        
        /* Sidebar with Maximum Visibility */
        [data-testid="stSidebar"] {{
            background-color: {secondary_bg} !important;
            border-radius: 0 15px 15px 0 !important;
            box-shadow: {shadow} !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        [data-testid="stSidebar"] * {{
            color: {text_color} !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        [data-testid="stSidebar"] .block-container {{
            background-color: {secondary_bg} !important;
            color: {text_color} !important;
            padding: 2rem 1rem !important;
            opacity: 1 !important;
            visibility: visible !important;
        }}
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] div {{
            color: {text_color} !important;
            opacity: 1 !important;
            visibility: visible !important;
            font-weight: 600 !important;
        }}
        
        /* Success/Error Messages */
        .stSuccess {{
            background-color: #d4edda !important;
            border-color: #c3e6cb !important;
            color: #155724 !important;
            border-radius: 8px !important;
        }}
        
        .stError {{
            background-color: #f8d7da !important;
            border-color: #f5c6cb !important;
            color: #721c24 !important;
            border-radius: 8px !important;
        }}
        
        .stWarning {{
            background-color: #fff3cd !important;
            border-color: #ffeaa7 !important;
            color: #856404 !important;
            border-radius: 8px !important;
        }}
        
        /* Theme Toggle Animation */
        .theme-toggle {{
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
        }}
        
        /* Scrollbar Customization */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {secondary_bg};
            border-radius: 4px;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: {button_bg};
            border-radius: 4px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: #5dade2;
        }}
        </style>
    """, unsafe_allow_html=True)

# 🔐 User DB Functions
def load_users():
    try:
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=2)

# 🔧 Session Initialization : memory saving
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

# 🧭 Navigation
if st.session_state.logged_in:
    options = [
        "Even/Odd Checker", "Quadratic Solver",
        "Area of Circle", "Calculator",
        "World Math List", "Logout"
    ]
else:
    options = ["Sign Up", "Login"]

page = st.sidebar.selectbox("🧭 Navigate", options, index=options.index(st.session_state.page))

# 🔓 Instant Logout
if page == "Logout":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.name = ""
    st.session_state.page = "Login"
    st.rerun()

# 🎛 Enhanced Display Settings
if st.session_state.logged_in:
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎨 Appearance")
    
    # Theme Toggle with better UX
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("☀️ Light", key="light_btn", help="Switch to light mode"):
            st.session_state.theme = "🌞 Light"
            st.rerun()
    with col2:
        if st.button("🌙 Dark", key="dark_btn", help="Switch to dark mode"):
            st.session_state.theme = "🌙 Dark"
            st.rerun()
    
    st.sidebar.write(f"Current: {st.session_state.theme}")
    
    st.sidebar.markdown("**Font Size**")
    st.session_state.zoom = st.sidebar.radio("", list(zoom_map.keys()), 
index=list(zoom_map.keys()).index(st.session_state.zoom),
label_visibility="collapsed")

# 🎨 Apply Styles
set_background(BACKGROUND_IMAGE, st.session_state.theme)

# 🔐 Enhanced Sign Up Page
if page == "Sign Up":
    # Page-specific theme toggle for Sign Up
    st.markdown("### 🎨 **Theme Control Panel**")
    st.markdown("*Choose your preferred visual mode*")
    
    theme_container = st.container()
    with theme_container:
        theme_col1, theme_col2, theme_col3 = st.columns([1, 1, 1])
        with theme_col1:
            if st.button("☀️ **LIGHT MODE**", key="signup_light", help="Switch to bright light theme", use_container_width=True):
                st.session_state.theme = "🌞 Light"
                st.rerun()
        with theme_col2:
            if st.button("🌙 **DARK MODE**", key="signup_dark", help="Switch to elegant dark theme", use_container_width=True):
                st.session_state.theme = "🌙 Dark"
                st.rerun()
        with theme_col3:
            st.markdown(f"**Current:** {st.session_state.theme}")
    
    st.divider()
    st.title("🔐 **CREATE ACCOUNT**")
    st.markdown("### *Join our exclusive math community today!*")

    # Show success message if signup just happened
    if st.session_state.signup_success:
        st.success("✅ **ACCOUNT CREATED SUCCESSFULLY!** Please login below.")
        if st.button("**GO TO LOGIN →**", use_container_width=True):
            st.session_state.page = "Login"
            st.session_state.signup_success = False
            st.rerun()

    if not st.session_state.signup_success:
        st.markdown("#### **Registration Form**")
        with st.form("signup_form"):
            real_name = st.text_input("📝 **FULL NAME**", placeholder="Enter your complete name here")
            new_username = st.text_input("👤 **USERNAME**", placeholder="Create your unique username")
            new_password = st.text_input("🔒 **PASSWORD**", type="password", placeholder="Create a strong password (min 6 chars)")
            
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                submit_button = st.form_submit_button("🚀 **CREATE ACCOUNT**", use_container_width=True)
            with col2:
                if st.form_submit_button("← **BACK TO LOGIN**", use_container_width=True):
                    st.session_state.page = "Login"
                    st.rerun()
            
            if submit_button:
                if new_username in user_db:
                    st.error("❌ **USERNAME ALREADY EXISTS!** Please choose another.")
                elif len(new_username) < 3:
                    st.error("❌ **USERNAME TOO SHORT!** Must be at least 3 characters.")
                elif len(new_password) < 6:
                    st.error("❌ **PASSWORD TOO SHORT!** Must be at least 6 characters.")
                elif not all([real_name.strip(), new_username.strip(), new_password]):
                    st.warning("⚠️ **PLEASE FILL ALL FIELDS!**")
                else:
                    user_db[new_username] = {
                        "name": real_name.strip(),
                        "password": new_password
                    }
                    save_users(user_db)
                    st.session_state.signup_success = True
                    st.rerun()

# 🔓 Enhanced Login Page
elif page == "Login":
    st.session_state.signup_success = False
    
    # Page-specific theme toggle for Login
    st.markdown("### 🎨 **Theme Control Panel**")
    st.markdown("*Choose your preferred visual mode*")
    
    theme_container = st.container()
    with theme_container:
        theme_col1, theme_col2, theme_col3 = st.columns([1, 1, 1])
        with theme_col1:
            if st.button("☀️ **LIGHT MODE**", key="login_light", help="Switch to bright light theme", use_container_width=True):
                st.session_state.theme = "🌞 Light"
                st.rerun()
        with theme_col2:
            if st.button("🌙 **DARK MODE**", key="login_dark", help="Switch to elegant dark theme", use_container_width=True):
                st.session_state.theme = "🌙 Dark"
                st.rerun()
        with theme_col3:
            st.markdown(f"**Current:** {st.session_state.theme}")
    
    st.divider()
    st.title("🔓 **WELCOME BACK**")
    st.markdown("### *Sign in to access your premium math tools*")
    
    st.markdown("#### **Login Form**")
    with st.form("login_form"):
        username = st.text_input("👤 **USERNAME**", placeholder="Enter your registered username")
        password = st.text_input("🔒 **PASSWORD**", type="password", placeholder="Enter your secure password")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            login_button = st.form_submit_button("🚀 **SIGN IN**", use_container_width=True)
        with col2:
            if st.form_submit_button("📝 **CREATE ACCOUNT**", use_container_width=True):
                st.session_state.page = "Sign Up"
                st.rerun()
        
        if login_button:
            user_info = user_db.get(username)
            if user_info and user_info["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.name = user_info["name"]
                st.session_state.page = "Even/Odd Checker"
                st.success(f"🎉 **WELCOME BACK, {user_info['name'].upper()}!**")
                st.rerun()
            else:
                st.error("❌ **INVALID CREDENTIALS!** Please check your username and password.")

# 🔢 Enhanced Even/Odd Checker
elif page == "Even/Odd Checker":
    st.title("🔢 Even or Odd Checker")
    st.markdown(f"👋 **Hello, {st.session_state.name}!** Let's check some numbers.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        number = st.number_input("Enter any integer", value=0, step=1, format="%d")
    with col2:
        st.write("") # Spacing
        if st.button("🔍 Check Number", use_container_width=True):
            result = "Even ✅" if number % 2 == 0 else "Odd 🔹"
            color = "green" if number % 2 == 0 else "blue"
            st.markdown(f"<h3 style='color: {color};'>{int(number)} is {result}</h3>", unsafe_allow_html=True)

# 🧮 Enhanced Quadratic Solver
elif page == "Quadratic Solver":
    st.title("🧮 Quadratic Equation Solver")
    st.markdown("*Solve equations in the form: **ax² + bx + c = 0***")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Coefficient a", value=1.0, help="Coefficient of x²")
    with col2:
        b = st.number_input("Coefficient b", value=0.0, help="Coefficient of x")
    with col3:
        c = st.number_input("Constant c", value=0.0, help="Constant term")
    
    if a == 0:
        st.warning("⚠️ Coefficient 'a' cannot be zero for a quadratic equation.")
    else:
        if st.button("🧮 Solve Equation", use_container_width=True):
            st.markdown(f"**Equation:** {a}x² + {b}x + {c} = 0")
            
            discriminant = b**2 - 4*a*c
            st.write(f"**Discriminant (Δ):** {discriminant:.2f}")
            
            if discriminant > 0:
                x1 = (-b + discriminant**0.5) / (2*a)
                x2 = (-b - discriminant**0.5) / (2*a)
                st.success(f"✅ **Two real solutions:**\n- x₁ = {x1:.4f}\n- x₂ = {x2:.4f}")
            elif discriminant == 0:
                x = -b / (2*a)
                st.success(f"✅ **One real solution:** x = {x:.4f}")
            else:
                real_part = -b / (2*a)
                imag_part = (abs(discriminant)**0.5) / (2*a)
                st.info(f"🔢 **Complex solutions:**\n- x₁ = {real_part:.4f} + {imag_part:.4f}i\n- x₂ = {real_part:.4f} - {imag_part:.4f}i")

# 🔵 Enhanced Area of Circle
elif page == "Area of Circle":
    st.title("🔵 Circle Area Calculator")
    st.markdown("*Calculate the area using: **A = πr²***")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        radius = st.number_input("Radius (r)", value=0.0, min_value=0.0, help="Enter the radius of the circle")
    with col2:
        st.write("") # Spacing
        if st.button("📐 Calculate Area", use_container_width=True):
            if radius > 0:
                area = 3.14159 * radius**2
                circumference = 2 * 3.14159 * radius
                st.success(f"🟢 **Results:**\n- Area = {area:.2f} square units\n- Circumference = {circumference:.2f} units")
            else:
                st.warning("⚠️ Please enter a positive radius.")

# ➕ Enhanced Calculator
elif page == "Calculator":
    st.title("🧮 Basic Calculator")
    st.markdown(f"👋 **Hello, {st.session_state.name}!** Perform basic arithmetic operations.")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First Number", value=0.0)
    with col2:
        num2 = st.number_input("Second Number", value=0.0)
    
    operation = st.selectbox("Choose Operation", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"])
    
    if st.button("🔢 Calculate", use_container_width=True):
        try:
            if operation == "➕ Add":
                result = num1 + num2
                st.success(f"**Result:** {num1} + {num2} = **{result}**")
            elif operation == "➖ Subtract":
                result = num1 - num2
                st.success(f"**Result:** {num1} - {num2} = **{result}**")
            elif operation == "✖️ Multiply":
                result = num1 * num2
                st.success(f"**Result:** {num1} × {num2} = **{result}**")
            elif operation == "➗ Divide":
                if num2 != 0:
                    result = num1 / num2
                    st.success(f"**Result:** {num1} ÷ {num2} = **{result:.4f}**")
                else:
                    st.error("❌ Cannot divide by zero!")
        except Exception as e:
            st.error(f"❌ Calculation error: {str(e)}")

# 🌍 Enhanced World Math List
elif page == "World Math List":
    st.title("🌍 World Math Challenges")
    st.markdown("*Explore fascinating mathematical questions from around the globe!*")
    
    math_questions = [
        {
            "country": "🇯🇵 Japan",
            "question": "What is the sum of the first 100 natural numbers?",
            "answer": "The sum is given by the formula n(n+1)/2 → 100×101/2 = **5050**",
            "difficulty": "Medium"
        },
        {
            "country": "🇮🇳 India", 
            "question": "What is the value of zero factorial (0!)?",
            "answer": "**0! = 1** (by mathematical convention)",
            "difficulty": "Easy"
        },
        {
            "country": "🇫🇷 France",
            "question": "What is the golden ratio approximately?",
            "answer": "**φ ≈ 1.618...**, derived from (1 + √5)/2",
            "difficulty": "Medium"
        },
        {
            "country": "🇺🇸 United States",
            "question": "Solve for x: 2x + 5 = 13",
            "answer": "Subtract 5 from both sides, then divide by 2: x = **4**",
            "difficulty": "Easy"
        },
        {
            "country": "🇬🇷 Greece",
            "question": "What is the Pythagorean theorem?",
            "answer": "**a² + b² = c²** (for right triangles)",
            "difficulty": "Easy"
        },
        {
            "country": "🇨🇭 Switzerland",
            "question": "What is Euler's identity?",
            "answer": "**e^(iπ) + 1 = 0** - called the most beautiful equation",
            "difficulty": "Hard"
        }
    ]
    
    # Filter by difficulty
    difficulty_filter = st.selectbox("Filter by Difficulty", ["All", "Easy", "Medium", "Hard"])
    
    filtered_questions = math_questions if difficulty_filter == "All" else [q for q in math_questions if q["difficulty"] == difficulty_filter]
    
    for i, q in enumerate(filtered_questions):
        with st.expander(f"{q['country']} - {q['question']} ({q['difficulty']})"):
            st.markdown(f"**Question:** {q['question']}")
            st.markdown(f"**Answer:** {q['answer']}")
            st.markdown(f"**Difficulty:** {q['difficulty']}")
