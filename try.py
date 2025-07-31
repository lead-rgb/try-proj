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
        bg_color = "#ffffff"
        text_color = "#2c3e50"
        secondary_bg = "#f8f9fa"
        button_bg = "#3498db"
        button_text = "#ffffff"
        input_bg = "#ffffff"
        border_color = "#dee2e6"
        shadow = "0 2px 4px rgba(0,0,0,0.1)"
    else:
        bg_color = "#1a1a1a"
        text_color = "#e9ecef"
        secondary_bg = "#2d3748"
        button_bg = "#4a90e2"
        button_text = "#ffffff"
        input_bg = "#2d3748"
        border_color = "#4a5568"
        shadow = "0 2px 4px rgba(255,255,255,0.1)"

    st.markdown(f"""
        <style>
        /* Global Styles with Transitions */
        * {{
            transition: all 0.3s ease !important;
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
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {{
            color: {text_color} !important;
            font-size: {font_size} !important;
            font-weight: 600 !important;
            margin-bottom: 1rem !important;
        }}
        
        p, label, .markdown-text-container, .stMarkdown {{
            color: {text_color} !important;
            font-size: {font_size} !important;
            line-height: 1.6 !important;
        }}
        
        /* Input Fields */
        .stTextInput input, .stNumberInput input, .stTextArea textarea {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
            border: 2px solid {border_color} !important;
            border-radius: 8px !important;
            font-size: {font_size} !important;
            padding: 12px !important;
            box-shadow: {shadow} !important;
        }}
        
        .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {{
            border-color: {button_bg} !important;
            box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1) !important;
        }}
        
        /* Select Boxes and Radio Buttons */
        .stSelectbox > div, .stRadio div {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
            border-radius: 8px !important;
            border: 2px solid {border_color} !important;
        }}
        
        .stRadio div label {{
            color: {text_color} !important;
            font-size: {font_size} !important;
            padding: 8px 12px !important;
            border-radius: 6px !important;
            background-color: {secondary_bg} !important;
            margin: 4px !important;
        }}
        
        /* Buttons */
        .stButton > button {{
            background: linear-gradient(135deg, {button_bg}, #5dade2) !important;
            color: {button_text} !important;
            font-size: {font_size} !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            border: none !important;
            box-shadow: {shadow} !important;
            transform: translateY(0px) !important;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3) !important;
        }}
        
        .stButton > button:active {{
            transform: translateY(0px) !important;
        }}
        
        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: {secondary_bg} !important;
            border-radius: 0 15px 15px 0 !important;
            box-shadow: {shadow} !important;
        }}
        
        [data-testid="stSidebar"] .block-container {{
            background-color: {secondary_bg} !important;
            color: {text_color} !important;
            padding: 2rem 1rem !important;
        }}
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {{
            color: {text_color} !important;
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

# 🔧 Session Initialization
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
    st.title("🔐 Create Account")
    st.markdown("*Join our math community today!*")

    # Show success message if signup just happened
    if st.session_state.signup_success:
        st.success("✅ Account created successfully! Please login below.")
        if st.button("Go to Login"):
            st.session_state.page = "Login"
            st.session_state.signup_success = False
            st.rerun()

    if not st.session_state.signup_success:
        with st.form("signup_form"):
            real_name = st.text_input("📝 Full Name", placeholder="Enter your full name")
            new_username = st.text_input("👤 Username", placeholder="Choose a unique username")
            new_password = st.text_input("🔒 Password", type="password", placeholder="Create a secure password")
            
            col1, col2 = st.columns(2)
            with col1:
                submit_button = st.form_submit_button("🚀 Create Account", use_container_width=True)
            with col2:
                if st.form_submit_button("← Back to Login", use_container_width=True):
                    st.session_state.page = "Login"
                    st.rerun()
            
            if submit_button:
                if new_username in user_db:
                    st.error("❌ Username already exists. Please choose another.")
                elif len(new_username) < 3:
                    st.error("❌ Username must be at least 3 characters long.")
                elif len(new_password) < 6:
                    st.error("❌ Password must be at least 6 characters long.")
                elif not all([real_name.strip(), new_username.strip(), new_password]):
                    st.warning("⚠️ Please fill in all fields.")
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
    st.title("🔓 Welcome Back")
    st.markdown("*Sign in to access your math tools*")
    
    with st.form("login_form"):
        username = st.text_input("👤 Username", placeholder="Enter your username")
        password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
        
        col1, col2 = st.columns(2)
        with col1:
            login_button = st.form_submit_button("🚀 Sign In", use_container_width=True)
        with col2:
            if st.form_submit_button("📝 Create Account", use_container_width=True):
                st.session_state.page = "Sign Up"
                st.rerun()
        
        if login_button:
            user_info = user_db.get(username)
            if user_info and user_info["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.name = user_info["name"]
                st.session_state.page = "Even/Odd Checker"
                st.success(f"🎉 Welcome back, {user_info['name']}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Please try again.")

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
