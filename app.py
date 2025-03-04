import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import time
import plotly.express as px

# Add this at the beginning of your script, right after the imports
def show_loading_screen():
    """Display a loading animation for 3 seconds"""
    # Check if we've already shown the loading screen in this session
    if 'loading_complete' not in st.session_state:
        # Create the loading animation HTML
        loading_html = """
        <style>
        .loading-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            background: linear-gradient(135deg, #1a2b4d 0%, #162238 100%);
            z-index: 9999;
            transition: opacity 0.5s ease-out;
        }
        
        .loader {
            border: 5px solid rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            border-top: 5px solid #2196F3;
            width: 70px;
            height: 70px;
            animation: spin 1s linear infinite, glow 2s ease-in-out infinite;
            margin-bottom: 20px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @keyframes glow {
            0% { box-shadow: 0 0 5px rgba(33, 150, 243, 0.5); }
            50% { box-shadow: 0 0 20px rgba(33, 150, 243, 0.8); }
            100% { box-shadow: 0 0 5px rgba(33, 150, 243, 0.5); }
        }
        
        .loading-text {
            color: white;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
        
        .hide-loading {
            opacity: 0;
            pointer-events: none;
        }
        </style>
        
        <div id="loading-screen" class="loading-container">
            <div class="loader"></div>
            <div class="loading-text">Smart Loan Advisor</div>
            <div style="color: #64B5F6; margin-top: 10px;">Loading resources...</div>
        </div>
        
        <script>
            // Hide the loading screen after 3 seconds
            setTimeout(function() {
                document.getElementById('loading-screen').classList.add('hide-loading');
                // After fade-out animation completes, remove the element entirely
                setTimeout(function() {
                    document.getElementById('loading-screen').style.display = 'none';
                }, 500);
            }, 3000);
        </script>
        """
        
        # Display the loading animation
        st.markdown(loading_html, unsafe_allow_html=True)
        
        # Set the flag that loading has been shown
        st.session_state.loading_complete = True
        
        # Force a rerun after 3.5 seconds to ensure the script above has time to execute
        # This is needed because Streamlit can't execute client-side scripts directly
        if 'load_time' not in st.session_state:
            st.session_state.load_time = time.time()
            time.sleep(0.1)  # Small delay to ensure the page reruns
            st.rerun()
        elif time.time() - st.session_state.load_time < 3.5:
            # Keep waiting if less than 3.5 seconds have passed
            time.sleep(0.1)
            st.rerun()

def load_models():
    """Load the trained model and scaler"""
    try:
        model = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\model.pkl', 'rb'))
        scaler = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\scaler.pkl', 'rb'))
        return model, scaler
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None, None

def calculate_loan_details(principal, years, rate=10.5):
    """Calculate EMI and generate amortization schedule"""
    rate_monthly = rate / (12 * 100)
    n_payments = years * 12
    emi = (principal * rate_monthly * (1 + rate_monthly)**n_payments) / ((1 + rate_monthly)**n_payments - 1)
    
    balance = principal
    schedule = []
    total_interest = 0
    
    for i in range(n_payments):
        interest = balance * rate_monthly   
        principal_paid = emi - interest
        balance = balance - principal_paid
        total_interest += interest
        
        schedule.append({
            'Month': i + 1,
            'EMI': emi,
            'Principal': principal_paid,
            'Interest': interest,
            'Balance': balance
        })
    
    return emi, schedule, total_interest

def create_emi_breakdown_chart(principal, total_interest):
    """Create a pie chart showing the EMI breakdown"""
    labels = ['Principal', 'Interest']
    values = [principal, total_interest]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.3,
        marker_colors=['#1976D2', '#64B5F6']
    )])
    
    fig.update_layout(
        title="Loan Amount Breakdown",
        showlegend=True,
        height=300,
        margin=dict(t=30, b=0, l=0, r=0)
    )
    
    return fig

def create_payment_schedule_chart(schedule):
    """Create a line chart showing the payment schedule"""
    df = pd.DataFrame(schedule)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Month'],
        y=df['Balance'],
        mode='lines',
        name='Balance',
        line=dict(color='#1976D2')
    ))
    
    fig.update_layout(
        title="Balance Over Time",
        xaxis_title="Month",
        yaxis_title="Balance",
        height=300,
        margin=dict(t=30, b=0, l=0, r=0)
    )
    
    return fig

def create_gauge_chart(probability):
    """Create a gauge chart showing loan approval probability"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Approval Probability"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1976D2"},
            'steps': [
                {'range': [0, 30], 'color': "#EF5350"},
                {'range': [30, 70], 'color': "#FFEE58"},
                {'range': [70, 100], 'color': "#66BB6A"}
            ]
        }
    ))
    
    fig.update_layout(height=300)
    return fig

def create_model_comparison_chart():
    """Create a bar chart comparing different ML algorithms performance"""
    algorithms = [
        'Random Forest', 
        'Gradient Boosting', 
        'Logistic Regression', 
        'SVM', 
        'XGBoost'
    ]
    
    # Example accuracy values - replace with your actual values
    base_accuracy = [0.82, 0.80, 0.76, 0.78, 0.84]
    tuned_accuracy = [0.88, 0.86, 0.78, 0.81, 0.92]
    
    fig = go.Figure(data=[
        go.Bar(name='Base Model', x=algorithms, y=base_accuracy, marker_color='#64B5F6'),
        go.Bar(name='Hypertuned Model', x=algorithms, y=tuned_accuracy, marker_color='#1976D2')
    ])
    
    fig.update_layout(
        title="Model Performance Comparison",
        xaxis_title="Algorithm",
        yaxis_title="Accuracy",
        legend_title="Model Type",
        yaxis=dict(range=[0.70, 1.0]),
        height=400,
        barmode='group'
    )
    
    return fig

# Initialize session state variables
if 'loan_history' not in st.session_state:
    st.session_state.loan_history = []

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Page configuration
st.set_page_config(
    page_title="Smart Loan Advisor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Show the loading screen
show_loading_screen()

# Enhanced Custom CSS with professional animations and navigation
st.markdown("""
<style>
    /* Animated Background */
    @keyframes gradientBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 5px rgba(33, 150, 243, 0.3); }
        50% { box-shadow: 0 0 20px rgba(33, 150, 243, 0.5); }
        100% { box-shadow: 0 0 5px rgba(33, 150, 243, 0.3); }
    }

    @keyframes buttonGlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Main App Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #1a2b4d 0%,
            #162238 25%,
            #1c2c4f 50%,
            #1e3255 75%,
            #1a2b4d 100%
        );
        background-size: 400% 400%;
        animation: gradientBackground 15s ease infinite;
    }

    /* Containers Animation */
    .element-container {
        animation: fadeInUp 0.6s ease-out forwards;
    }

    /* Input Fields Styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(33, 150, 243, 0.2) !important;
        border-radius: 8px !important;
        color: white !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:hover,
    .stNumberInput > div > div > input:hover,
    .stSelectbox > div > div:hover {
        border-color: rgba(33, 150, 243, 0.5) !important;
        animation: pulseGlow 2s infinite;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div:focus {
        border-color: #2196F3 !important;
        box-shadow: 0 0 10px rgba(33, 150, 243, 0.3) !important;
        transform: translateY(-2px);
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #1976D2, #2196F3, #1976D2) !important;
        background-size: 200% 200% !important;
        animation: buttonGlow 3s ease infinite !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        transform: translateY(0);
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(33, 150, 243, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Cards and Containers */
    .css-1d391kg, .css-12w0qpk {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(33, 150, 243, 0.1) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        animation: fadeInUp 0.6s ease-out forwards;
    }

    /* Success/Error Messages */
    .stAlert {
        animation: slideInLeft 0.5s ease-out forwards !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(33, 150, 243, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }

    /* Metrics Animation */
    .css-1wivap2 {
        animation: fadeInUp 0.6s ease-out forwards;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: rgba(26, 43, 77, 0.5) !important;
        border-right: 1px solid rgba(33, 150, 243, 0.1) !important;
    }

    /* Headers */
    h1, h2, h3 {
        color: #2196F3 !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        animation: fadeInUp 0.6s ease-out forwards;
    }

    /* Progress Bar */
    .stProgress > div > div {
        background-color: #2196F3 !important;
        background-image: linear-gradient(45deg, 
            rgba(255,255,255,.15) 25%, 
            transparent 25%, 
            transparent 50%, 
            rgba(255,255,255,.15) 50%, 
            rgba(255,255,255,.15) 75%, 
            transparent 75%, 
            transparent) !important;
        background-size: 1rem 1rem !important;
        animation: buttonGlow 3s linear infinite !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(33, 150, 243, 0.05) !important;
        border: 1px solid rgba(33, 150, 243, 0.1) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    .streamlit-expanderHeader:hover {
        background-color: rgba(33, 150, 243, 0.1) !important;
    }

    /* Footer */
    .footer {
        background: rgba(26, 43, 77, 0.5) !important;
        border: 1px solid rgba(33, 150, 243, 0.1) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        animation: fadeInUp 0.6s ease-out forwards;
        padding: 20px;
        margin-top: 30px;
        text-align: center;
    }
    
    /* Navigation */
    .nav-container {
        display: flex;
        justify-content: left;
        padding: 10px;
        margin-bottom: 20px;
        background-color: rgba(26, 43, 77, 0.5);
        border-radius: 12px;
        border: 1px solid rgba(33, 150, 243, 0.1);
        backdrop-filter: blur(5px);
    }
    
    .nav-link {
        display: inline-block;
        padding: 10px 20px;
        margin: 0 10px;
        text-decoration: none;
        font-weight: bold;
        color: white;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    
    .nav-link:hover {
        background-color: rgba(33, 150, 243, 0.2);
        transform: translateY(-2px);
    }
    
    .nav-link.active {
        background-color: #2196F3;
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.3);
    }
    
    /* About page section styling */
    .about-section {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(33, 150, 243, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .tech-card {
        background: rgba(26, 43, 77, 0.5);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid rgba(33, 150, 243, 0.2);
        transition: all 0.3s ease;
    }
    
    .tech-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(33, 150, 243, 0.2);
    }
    
    /* Add animation classes for content reveal after loading */
    .content-reveal {
        opacity: 0;
        animation: fadeInUp 0.6s ease-out forwards;
        animation-delay: 3s; /* Start after loading animation */
    }
</style>
""", unsafe_allow_html=True)

# Load models
model, scaler = load_models()

# Navigation function
def nav_to(page):
    st.session_state.current_page = page
    st.rerun()

# Inject custom CSS for button styling
st.markdown("""
    <style>
        .nav-container {
            display: flex;
            gap: 5px;
        }
        .nav-container button {
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Create navigation bar
nav_html = f"""

"""
st.markdown(nav_html, unsafe_allow_html=True)

# Create a div to wrap all content with the delayed reveal animation
st.markdown('<div class="content-reveal">', unsafe_allow_html=True)

# Hidden buttons to handle navigation
col_nav1, col_nav2 = st.columns([1,10])
with col_nav1:
    st.markdown("<div style='text-align: center, padding:0rem;'>", unsafe_allow_html=True)
    if st.button("Home", key="home-btn", help="Go to home page", type="primary"):
        nav_to('home')
    st.markdown("</div>", unsafe_allow_html=True)
with col_nav2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("About", key="about-btn", help="Go to about page", type="secondary"):
        nav_to('about')
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar with EMI calculator (visible for both pages)
with st.sidebar:
    st.markdown("### 💰 Loan EMI Calculator")
    with st.container():
        calc_loan_amount = st.number_input("Loan Amount (₹)", min_value=0, max_value=10000000, value=0, step=1000)
        loan_tenure = st.number_input("Loan Tenure (Years)", min_value=0, max_value=30, value=0, step=1)
        
        if st.button("Calculate EMI", key="calc_emi"):
            if calc_loan_amount > 0 and loan_tenure > 0:
                emi, schedule, total_interest = calculate_loan_details(calc_loan_amount, loan_tenure)
                
                st.markdown(f"### Monthly EMI: ₹{emi:,.2f}")
                
                # EMI Breakdown Chart
                st.markdown("#### Payment Breakdown")
                st.plotly_chart(create_emi_breakdown_chart(calc_loan_amount, total_interest), use_container_width=True)
                
                # Payment Schedule Chart
                st.markdown("#### Payment Schedule")
                st.plotly_chart(create_payment_schedule_chart(schedule), use_container_width=True)
                
                # Key Statistics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Interest", f"₹{total_interest:,.2f}")
                with col2:
                    st.metric("Total Payment", f"₹{(calc_loan_amount + total_interest):,.2f}")
            else:
                st.error("Please enter valid loan amount and tenure")

    # Loan History
    st.markdown("### 📈 Loan History")
    if st.session_state.loan_history:
        for idx, history in enumerate(st.session_state.loan_history[-5:]):
            with st.expander(f"Application {idx + 1}"):
                st.write(f"Amount: ₹{history['amount']:,}")
                st.write(f"Duration: {history['duration']} years")
                st.write(f"Status: {'Approved' if history['approved'] else 'Rejected'}")
    else:
        st.info("No previous applications")

# Display content based on current page
if st.session_state.current_page == 'home':
    # Main content for home page
    st.markdown('<h1 class="main-header">🏦 Smart Loan Advisor</h1>', unsafe_allow_html=True)

    # Create columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        no_of_dep = st.number_input(
            'Number of Dependents',
            min_value=0,
            max_value=5,
            value=0,
            step=1,
            help="Include spouse and children"
        )
        
        education = st.selectbox(
            'Education Level',
            ['Graduate', 'Not Graduate'],
            help="Highest education qualification"
        )
        
        employment = st.selectbox(
            'Employment Status',
            ['Self Employed', 'Not Employed'],
            help="Current employment status"
        )

    with col2:
        Annual_Income = st.number_input(
            'Annual Income (₹)',
            min_value=0,
            max_value=10000000,
            value=0,
            step=10000,
            help="Gross annual income"
        )
        
        Assets = st.number_input(
            'Assets Value (₹)',
            min_value=0,
            max_value=10000000,
            value=0,
            step=10000,
            help="Total value of assets owned"
        )
        
        Cibil = st.number_input(
            'CIBIL Score',
            min_value=300,
            max_value=900,
            value=300,
            step=1,
            help="Your credit score (300-900)"
        )

    with col3:
        Loan_Amount = st.number_input(
            'Loan Amount (₹)',
            min_value=0,
            max_value=10000000,
            value=0,
            step=10000,
            help="Amount you wish to borrow"
        )
        
        Loan_Dur = st.number_input(
            'Loan Duration (Years)',
            min_value=0,
            max_value=30,
            value=0,
            step=1,
            help="Loan tenure in years"
        )

    # Input validation
    all_inputs_valid = all([
        no_of_dep >= 0,
        Annual_Income > 0,
        Assets > 0,
        Loan_Amount > 0,
        Loan_Dur > 0,
        Cibil >= 300
    ])

    # Calculate and display EMI if inputs are valid
    if all_inputs_valid and Loan_Amount > 0 and Loan_Dur > 0:
        emi, _, _ = calculate_loan_details(Loan_Amount, Loan_Dur)
        st.info(f"Estimated Monthly EMI: ₹{emi:,.2f}")

    # Predict button with validation
    if st.button("Predict Loan Eligibility", use_container_width=True):
        if not all_inputs_valid:
            st.error("Please provide valid inputs in all fields. Values must be greater than zero.")
        else:
            with st.spinner('Analyzing your application...'):
                # Add progress bar
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                # Convert categorical variables
                education_encoded = 1 if education == 'Not Graduate' else 0
                employment_encoded = 1 if employment == 'Not Employed' else 0
                
                # Create prediction DataFrame
                pred_data = pd.DataFrame(
                    [[no_of_dep, education_encoded, employment_encoded, Annual_Income,
                      Loan_Amount, Loan_Dur, Cibil, Assets]],
                    columns=['no_of_dependents', 'education', 'self_employed', 'income_annum',
                             'loan_amount', 'loan_term', 'cibil_score', 'Assets']
                )
                
                # Make prediction
                pred_data_scaled = scaler.transform(pred_data)
                prediction = model.predict(pred_data_scaled)
                probability = model.predict_proba(pred_data_scaled)[0][1]
                
                # Store in history
                st.session_state.loan_history.append({
                    'amount': Loan_Amount,
                    'duration': Loan_Dur,
                    'approved': bool(prediction[0])
                })
                
                # Display result
                col_result1, col_result2 = st.columns(2)
                
                with col_result1:
                    st.plotly_chart(create_gauge_chart(probability), use_container_width=True)
                
                with col_result2:
                    if prediction[0] == 1:
                        st.success("🎉 Congratulations! Your loan application is likely to be approved.")
                        st.markdown("""
                            ### Next Steps:
                            1. Prepare required documents
                            2. Visit nearest branch
                            3. Complete formal verification
                        """)
                    else:
                        st.error("⚠️ Your loan application might need improvements.")
                        st.markdown("""
                            ### Recommendations:
                            1. Improve CIBIL score
                            2. Increase down payment
                            3. Add a co-applicant
                            4. Provide additional collateral
                        """)

elif st.session_state.current_page == 'about':
    # About page content
    st.markdown('<h1 class="main-header">ℹ️ About Smart Loan Advisor</h1>', unsafe_allow_html=True)
    
    # Project overview section
    st.markdown("""
    <div class="about-section">
        <h2>📊 Project Overview</h2>
        <p>Smart Loan Advisor is an advanced machine learning application designed to predict loan eligibility 
        based on various financial and personal parameters. This project uses a combination of traditional and 
        advanced ML algorithms to provide accurate predictions and financial insights.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technologies used
    st.markdown("""
    <div class="about-section">
        <h2>🔧 Technologies Used</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        <div class="tech-card">
            <h3>🐍 Python Libraries</h3>
            <ul>
                <li>Pandas & NumPy</li>
                <li>Scikit-learn</li>
                <li>Streamlit</li>
                <li>Plotly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div class="tech-card">
            <h3>🤖 ML Algorithms</h3>
            <ul>
                <li>Random Forest</li>
                <li>Gradient Boosting</li>
                <li>XGBoost</li>
                <li>Logistic Regression</li>
                <li>Support Vector Machines</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col3:
        st.markdown("""
        <div class="tech-card">
            <h3>🧰 Other Tools</h3>
            <ul>
                <li>Hyperparameter Tuning</li>
                <li>Cross-Validation</li>
                <li>Feature Engineering</li>
                <li>Data Preprocessing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
# Model performance section
    st.markdown("""
    <div class="about-section">
        <h2>📈 Model Performance</h2>
        <p>We compared multiple machine learning algorithms to identify the best model for loan eligibility prediction.
        After extensive testing and hyperparameter tuning, we achieved significant improvements in model accuracy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show the model comparison chart
    st.plotly_chart(create_model_comparison_chart(), use_container_width=True)
    
    # Implementation details
    st.markdown("""
    <div class="about-section">
        <h2>🛠️ Implementation Details</h2>
        <p>This application was implemented using the following approach:</p>
        <ol>
            <li><strong>Data Collection and Preprocessing</strong>: Gathering financial data, handling missing values, 
            encoding categorical variables, and normalizing numerical features.</li>
            <li><strong>Feature Engineering</strong>: Creating relevant features that improve model performance.</li>
            <li><strong>Model Development</strong>: Training multiple ML models and selecting the best performer.</li>
            <li><strong>Hyperparameter Tuning</strong>: Using GridSearchCV and RandomizedSearchCV to optimize model parameters.</li>
            <li><strong>Model Evaluation</strong>: Using cross-validation to ensure robust performance.</li>
            <li><strong>Web Application Development</strong>: Building an interactive interface using Streamlit.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Close the content reveal div
st.markdown('</div>', unsafe_allow_html=True)

# Footer (visible for both pages)
st.markdown(f"""
<div class='footer content-reveal'>
    <p>💡 This is a prediction tool and final loan approval is subject to bank verification.</p>
    <p style='font-weight: bold; color: #00ff87;'>🚀 Developed by Jenil Patel</p>
    <p style='font-style: italic;'>Last updated: {datetime.now().strftime("%B %d, %Y")}</p>
</div>
""", unsafe_allow_html=True)