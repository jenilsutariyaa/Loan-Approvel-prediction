# # import streamlit as st
# # import pandas as pd
# # import pickle as pk

# # # Load the model and scaler
# # model = pk.load(open('D:\Darshan_university\CSE 6TH SEM\ML\loan approved pred\model.pkl', 'rb'))
# # scaler = pk.load(open('D:\Darshan_university\CSE 6TH SEM\ML\loan approved pred\scaler.pkl', 'rb'))

# # st.header('Loan Prediction App')

# # # Input fields
# # no_of_dep = st.number_input('Enter Number of Dependents', min_value=0, max_value=5, step=1)
# # grad = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
# # self_emp = st.selectbox('Self Employed?', ['Yes', 'No'])
# # Annual_Income = st.number_input('Enter Annual Income', min_value=0, max_value=10000000, step=1)
# # Loan_Amount = st.number_input('Enter Loan Amount', min_value=0, max_value=10000000, step=1)
# # Loan_Dur = st.number_input('Enter Loan Duration (in years)', min_value=0, max_value=20, step=1)
# # Cibil = st.number_input('Enter Cibil Score', min_value=0, max_value=1000, step=1)
# # Assets = st.number_input('Enter Assets Value', min_value=0, max_value=10000000, step=1)

# # # Convert categorical inputs to numerical
# # grad_s = 0 if grad == 'Graduated' else 1
# # emp_s = 0 if self_emp == 'No' else 1

# # # Prediction
# # if st.button("Predict"):
# #     pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]],
# #                              columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])
# #     pred_data = scaler.transform(pred_data)
# #     predict = model.predict(pred_data)
# #     if predict[0] == 1:
# #         st.markdown('Loan Is Approved')
# #     else:
# #         st.markdown('Loan Is Rejected')ss













# import streamlit as st
# import pandas as pd
# import pickle as pk

# # Load the model and scaler
# model = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\model.pkl', 'rb'))
# scaler = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\scaler.pkl', 'rb'))

# # Custom background and button styling
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: linear-gradient(135deg, 
#             rgba(45, 96, 125, 0.8), 
#             rgba(55, 67, 47, 0.8), 
#             rgba(115, 60, 62, 0.8),
#             rgba(40, 80, 120, 0.8)
#         );
#         background-size: 400% 400%;
#         background-position: 0% 50%;
#         animation: gradient-animation 15s ease infinite;
#         backdrop-filter: blur(10px);
#         color: white;
#     }

#     @keyframes gradient-animation {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }

#     .stTextInput, .stNumberInput, .stSelectbox {
#         background-color: rgba(255, 255, 255, 0.2);
#         backdrop-filter: blur(5px);
#         border-radius: 15px;
#         padding: 10px;
#         margin-bottom: 15px;
#     }

#     .stButton>button {
#         background-color: rgba(255, 165, 0, 0.8); /* Orange background */
#         color: white; /* White text */
#         border: none;
#         backdrop-filter: blur(5px);
#         transition: all 0.3s ease;
#         border-radius: 15px;
#         font-weight: bold;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         font-size: 1.2rem; /* Larger text */
#         padding: 10px 20px; /* More padding */
#         display: flex;
#         justify-content: center;
#         margin: 0 auto; /* Center horizontally */
#     }

#     .stButton>button:hover {
#         background-color: black; /* Black background on hover */
#         color: white; /* White text on hover */
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
#     }

#     .stButton>button:active, .stButton>button.clicked, .stButton>button:focus {
#         background-color: white; /* White background after click */
#         color: black; /* Black text after click */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
    
#     .stButton>button:focus {
#         outline: none;
#     }

#     h1 {
#         font-size: 3rem;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#         text-align: center;
#         color: white;
#         letter-spacing: 2px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Page title
# st.markdown('<h1>🏦 Loan Prediction Assistant</h1>', unsafe_allow_html=True)

# # Create two columns for layout
# col1, col2 = st.columns(2)

# with col1:
#     # Input fields
#     no_of_dep = st.number_input('Number of Dependents', 
#                                 min_value=0, 
#                                 max_value=5, 
#                                 step=1,
#                                 help="Total family dependents")

#     grad = st.selectbox('Education Level', 
#                         ['Graduated', 'Not Graduated'],
#                         help="Highest qualification")

#     self_emp = st.selectbox('Employment Status', 
#                             ['No', 'Yes'],
#                             help="Self-employment status")

#     Assets = st.number_input('Assets Value', 
#                              min_value=0, 
#                              max_value=10000000, 
#                              step=1,
#                              help="Total asset value")

# with col2:
#     Annual_Income = st.number_input('Annual Income', 
#                                     min_value=0, 
#                                     max_value=10000000, 
#                                     step=1,
#                                     help="Total yearly income")

#     Loan_Amount = st.number_input('Loan Amount', 
#                                   min_value=0, 
#                                   max_value=10000000, 
#                                   step=1,
#                                   help="Loan amount requested")

#     Loan_Dur = st.number_input('Loan Duration (Years)', 
#                                min_value=0, 
#                                max_value=20, 
#                                step=1,
#                                help="Desired loan term")

#     Cibil = st.number_input('Cibil Score', 
#                             min_value=0, 
#                             max_value=1000, 
#                             step=1,
#                             help="Credit score")

# # Centered Prediction Button
# st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
# if st.button("Predict Loan Eligibility"):
#     # Convert input values to the correct format for prediction
#     grad_s = 0 if grad == 'Graduated' else 1
#     emp_s = 0 if self_emp == 'No' else 1

#     pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]], 
#                              columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])

#     pred_data = scaler.transform(pred_data)
#     predict = model.predict(pred_data)

#     # Display the result
#     if predict[0] == 1:
#         st.success(' Congratulations! Your Loan is Approved.')
#     else:
#         st.error(' Sorry, Your Loan Application has been Rejected.')
# st.markdown('</div>', unsafe_allow_html=True)












# import streamlit as st
# import pandas as pd
# import pickle as pk

# # Load the model and scaler
# model = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\model.pkl', 'rb'))
# scaler = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\scaler.pkl', 'rb'))

# # Custom background and button styling
# st.markdown(
#     """
#     <style>
#     @keyframes gradient-animation {
#         0% { background-position: 0% 50%; }
#         25% { background-position: 50% 0%; }
#         50% { background-position: 100% 50%; }
#         75% { background-position: 50% 100%; }
#         100% { background-position: 0% 50%; }
#     }

#     .stApp {
#         background-image: linear-gradient(135deg, 
#             rgba(200, 50, 50, 0.8),  /* Darker red */
#             rgba(200, 100, 50, 0.8), /* Darker orange */
#             rgba(50, 150, 200, 0.8), /* Darker blue */
#             rgba(150, 50, 200, 0.8)  /* Darker purple */
#         );
#         background-size: 200% 200%;
#         background-position: 0% 50%;
#         animation: gradient-animation 8s ease infinite;
#         backdrop-filter: blur(10px);
#         color: white;
#     }

#     .stTextInput, .stNumberInput, .stSelectbox {
#         background-color: rgba(255, 255, 255, 0.3);
#         backdrop-filter: blur(5px);
#         border-radius: 15px;
#         padding: 10px;
#         margin-bottom: 15px;
#     }

#     .stButton>button {
#         background-color: rgba(255, 87, 34, 0.9);  /* Deep orange */
#         color: white;
#         border: none;
#         backdrop-filter: blur(5px);
#         transition: all 0.3s ease;
#         border-radius: 15px;
#         font-weight: bold;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         font-size: 1.2rem;
#         padding: 10px 20px;
#         display: flex;
#         justify-content: center;
#         margin: 0 auto;
#     }

#     .stButton>button:hover {
#         background-color: rgba(255, 165, 0, 0.9);  /* Orange */
#         color: white;
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
#     }

#     .stButton>button:active, .stButton>button.clicked, .stButton>button:focus {
#         background-color: rgba(255, 193, 7, 0.9);  /* Amber */
#         color: black;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
    
#     .stButton>button:focus {
#         outline: none;
#     }

#     h1 {
#         font-size: 3rem;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#         text-align: center;
#         color: white;
#         letter-spacing: 2px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Page title
# st.markdown('<h1>🏦 Loan Prediction Assistant</h1>', unsafe_allow_html=True)

# # Create two columns for layout
# col1, col2 = st.columns(2)

# with col1:
#     # Input fields
#     no_of_dep = st.number_input('Number of Dependents', 
#                                 min_value=0, 
#                                 max_value=5, 
#                                 step=1,
#                                 help="Total family dependents")

#     grad = st.selectbox('Education Level', 
#                         ['Graduated', 'Not Graduated'],
#                         help="Highest qualification")

#     self_emp = st.selectbox('Employment Status', 
#                             ['No', 'Yes'],
#                             help="Self-employment status")

#     Assets = st.number_input('Assets Value', 
#                              min_value=0, 
#                              max_value=10000000, 
#                              step=1,
#                              help="Total asset value")

# with col2:
#     Annual_Income = st.number_input('Annual Income', 
#                                     min_value=0, 
#                                     max_value=10000000, 
#                                     step=1,
#                                     help="Total yearly income")

#     Loan_Amount = st.number_input('Loan Amount', 
#                                   min_value=0, 
#                                   max_value=10000000, 
#                                   step=1,
#                                   help="Loan amount requested")

#     Loan_Dur = st.number_input('Loan Duration (Years)', 
#                                min_value=0, 
#                                max_value=20, 
#                                step=1,
#                                help="Desired loan term")

#     Cibil = st.number_input('Cibil Score', 
#                             min_value=0, 
#                             max_value=1000, 
#                             step=1,
#                             help="Credit score")

# # Centered Prediction Button
# st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
# if st.button("Predict Loan Eligibility"):
#     # Convert input values to the correct format for prediction
#     grad_s = 0 if grad == 'Graduated' else 1
#     emp_s = 0 if self_emp == 'No' else 1

#     pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]], 
#                              columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])

#     pred_data = scaler.transform(pred_data)
#     predict = model.predict(pred_data)

#     # Display the result
#     if predict[0] == 1:
#         st.success(' Congratulations! Your Loan is Approved.')
#     else:
#         st.error(' Sorry, Your Loan Application has been Rejected.')
# st.markdown('</div>', unsafe_allow_html=True)








# import streamlit as st
# import pandas as pd
# import pickle as pk

# # Load the model and scaler
# model = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\model.pkl', 'rb'))
# scaler = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\scaler.pkl', 'rb'))

# # Custom background and button styling
# st.markdown(
#     """
#     <style>
#     @keyframes gradient-animation {
#         0% { background-position: 0% 50%; }
#         25% { background-position: 50% 0%; }
#         50% { background-position: 100% 50%; }
#         75% { background-position: 50% 100%; }
#         100% { background-position: 0% 50%; }
#     }

#     .stApp {
#         background-image: linear-gradient(135deg, 
#             rgba(200, 50, 50, 0.8),  /* Darker red */
#             rgba(200, 100, 50, 0.8), /* Darker orange */
#             rgba(50, 150, 200, 0.8), /* Darker blue */
#             rgba(150, 50, 200, 0.8)  /* Darker purple */
#         );
#         background-size: 200% 200%;
#         background-position: 0% 50%;
#         animation: gradient-animation 8s ease infinite;
#         backdrop-filter: blur(10px);
#         color: white;
#     }

#     .stTextInput, .stNumberInput, .stSelectbox {
#         background-color: rgba(255, 255, 255, 0.3);
#         backdrop-filter: blur(5px);
#         border-radius: 15px;
#         padding: 10px;
#         margin-bottom: 15px;
#     }

#     .stButton>button {
#         background-color: rgba(255, 87, 34, 0.9);  /* Deep orange */
#         color: white;
#         border: none;
#         backdrop-filter: blur(5px);
#         transition: all 0.3s ease;
#         border-radius: 15px;
#         font-weight: bold;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         font-size: 1.2rem;
#         padding: 10px 20px;
#         display: flex;
#         justify-content: center;
#         margin: 0 auto;
#     }

#     .stButton>button:hover {
#         background-color: rgba(255, 165, 0, 0.9);  /* Orange */
#         color: white;
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
#     }

#     .stButton>button:active, .stButton>button.clicked, .stButton>button:focus {
#         background-color: rgba(255, 193, 7, 0.9);  /* Amber */
#         color: black;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
    
#     .stButton>button:focus {
#         outline: none;
#     }

#     h1 {
#         font-size: 3rem;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#         text-align: center;
#         color: white;
#         letter-spacing: 2px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Page title
# st.markdown('<h1>🏦 Loan Prediction Assistant</h1>', unsafe_allow_html=True)

# # Create two columns for layout
# col1, col2 = st.columns(2)

# with col1:
#     # Input fields
#     no_of_dep = st.number_input('Number of Dependents', 
#                                 min_value=0, 
#                                 max_value=5, 
#                                 step=1,
#                                 help="Total family dependents")

#     grad = st.selectbox('Education Level', 
#                         ['Graduated', 'Not Graduated'],
#                         help="Highest qualification")

#     self_emp = st.selectbox('Employment Status', 
#                             ['No', 'Yes'],
#                             help="Self-employment status")

#     Assets = st.number_input('Assets Value', 
#                              min_value=0, 
#                              max_value=10000000, 
#                              step=1,
#                              help="Total asset value")

# with col2:
#     Annual_Income = st.number_input('Annual Income', 
#                                     min_value=0, 
#                                     max_value=10000000, 
#                                     step=1,
#                                     help="Total yearly income")

#     Loan_Amount = st.number_input('Loan Amount', 
#                                   min_value=0, 
#                                   max_value=10000000, 
#                                   step=1,
#                                   help="Loan amount requested")

#     Loan_Dur = st.number_input('Loan Duration (Years)', 
#                                min_value=0, 
#                                max_value=20, 
#                                step=1,
#                                help="Desired loan term")

#     Cibil = st.number_input('Cibil Score', 
#                             min_value=0, 
#                             max_value=1000, 
#                             step=1,
#                             help="Credit score")

# # Centered Prediction Button
# st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
# if st.button("Predict Loan Eligibility"):
#     # Convert input values to the correct format for prediction
#     grad_s = 0 if grad == 'Graduated' else 1
#     emp_s = 0 if self_emp == 'No' else 1

#     pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]], 
#                              columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])

#     pred_data = scaler.transform(pred_data)
#     predict = model.predict(pred_data)

#     # Display the result
#     if predict[0] == 1:
#         st.success(' Congratulations! Your Loan is Approved.')
#     else:
#         st.error(' Sorry, Your Loan Application has been Rejected.')
# st.markdown('</div>', unsafe_allow_html=True)




















import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import time
import plotly.express as px

def load_models():
    """Load the trained model and scaler"""
    try:
        model = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\model.pkl', 'rb'))
        scaler = pk.load(open('D:\\Darshan_university\\CSE_6TH_SEM\\ML\\LAP\\scaler.pkl', 'rb'))
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

# Initialize session state for loan history
if 'loan_history' not in st.session_state:
    st.session_state.loan_history = []

# Page configuration
st.set_page_config(
    page_title="Smart Loan Advisor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Enhanced Custom CSS with professional animations
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
    /* Animated Background */
    @keyframes gradientBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

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

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #1976D2, #2196F3, #1976D2) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }

    /* Headers */
    h1, h2, h3 {
        color: #2196F3 !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }

    /* Footer */
    .footer {
        background: rgba(26, 43, 77, 0.5) !important;
        border: 1px solid rgba(33, 150, 243, 0.1) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        animation: fadeInUp 0.6s ease-out forwards;
    }
</style>
""", unsafe_allow_html=True)


# Load models
model, scaler = load_models()

# Sidebar with EMI calculator
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

# Main content
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

# Footer
st.markdown(f"""
<div class='footer' style='text-align: center; margin-top: 30px; padding: 20px;'>
    <p>💡 This is a prediction tool and final loan approval is subject to bank verification.</p>
    <p style='font-weight: bold; color: #00ff87;'>🚀 Developed by Your Name</p>
    <p style='font-style: italic;'>Last updated: {datetime.now().strftime("%B %d, %Y")}</p>
</div>
""", unsafe_allow_html=True)