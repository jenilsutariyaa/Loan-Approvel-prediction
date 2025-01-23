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
# #         st.markdown('Loan Is Rejected')

#########################################################animated ui
# import streamlit as st
# import pandas as pd
# import pickle as pk

# # Load the model and scaler
# model = pk.load(open('D:\Darshan_university\CSE 6TH SEM\ML\loan approved pred\model.pkl', 'rb'))
# scaler = pk.load(open('D:\Darshan_university\CSE 6TH SEM\ML\loan approved pred\scaler.pkl', 'rb'))

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
#     }

#     .stButton>button:hover {
#         transform: scale(1.1); /* Bigger scale on hover */
#         background-color: white; /* White background on hover */
#         color: black; /* Black text on hover */
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
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

#     Assets = st.number_input('Assets Value', 
#                              min_value=0, 
#                              max_value=10000000, 
#                              step=1,
#                              help="Total asset value")

# # Prediction button
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
#         st.success(' Congratulations! Your Loan is Approved ')
#     else:
#         st.error(' Sorry, Your Loan Application has been Rejected ')













import streamlit as st
import pandas as pd
import pickle as pk

# Load the model and scaler
model = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\model.pkl', 'rb'))
scaler = pk.load(open('D:\Darshan_university\CSE_6TH_SEM\ML\LAP\scaler.pkl', 'rb'))

# Custom background and button styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(135deg, 
            rgba(45, 96, 125, 0.8), 
            rgba(55, 67, 47, 0.8), 
            rgba(115, 60, 62, 0.8),
            rgba(40, 80, 120, 0.8)
        );
        background-size: 400% 400%;
        background-position: 0% 50%;
        animation: gradient-animation 15s ease infinite;
        backdrop-filter: blur(10px);
        color: white;
    }

    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stTextInput, .stNumberInput, .stSelectbox {
        background-color: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(5px);
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 15px;
    }

    .stButton>button {
        background-color: rgba(255, 165, 0, 0.8); /* Orange background */
        color: white; /* White text */
        border: none;
        backdrop-filter: blur(5px);
        transition: all 0.3s ease;
        border-radius: 15px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 1.2rem; /* Larger text */
        padding: 10px 20px; /* More padding */
    }

    .stButton>button:hover {
        background-color: black; /* Black background on hover */
        color: white; /* White text on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }

    .stButton>button:active, .stButton>button.clicked {
        background-color: white; /* White background after click */
        color: black; /* Black text after click */
    }

    .stButton>button.clicked:hover {
        background-color: white; /* White background on hover after click */
        color: black; /* Black text on hover after click */
    }

    h1 {
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        text-align: center;
        color: white;
        letter-spacing: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown('<h1>🏦 Loan Prediction Assistant</h1>', unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # Input fields
    no_of_dep = st.number_input('Number of Dependents', 
                                min_value=0, 
                                max_value=5, 
                                step=1,
                                help="Total family dependents")

    grad = st.selectbox('Education Level', 
                        ['Graduated', 'Not Graduated'],
                        help="Highest qualification")

    self_emp = st.selectbox('Employment Status', 
                            ['No', 'Yes'],
                            help="Self-employment status")

    Assets = st.number_input('Assets Value', 
                             min_value=0, 
                             max_value=10000000, 
                             step=1,
                             help="Total asset value")

with col2:
    Annual_Income = st.number_input('Annual Income', 
                                    min_value=0, 
                                    max_value=10000000, 
                                    step=1,
                                    help="Total yearly income")

    Loan_Amount = st.number_input('Loan Amount', 
                                  min_value=0, 
                                  max_value=10000000, 
                                  step=1,
                                  help="Loan amount requested")

    Loan_Dur = st.number_input('Loan Duration (Years)', 
                               min_value=0, 
                               max_value=20, 
                               step=1,
                               help="Desired loan term")

    Cibil = st.number_input('Cibil Score', 
                            min_value=0, 
                            max_value=1000, 
                            step=1,
                            help="Credit score")

# Prediction button
if st.button("Predict Loan Eligibility"):
    # Apply "clicked" class to button
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: white !important; /* White background after click */
            color: black !important; /* Black text after click */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Convert input values to the correct format for prediction
    grad_s = 0 if grad == 'Graduated' else 1
    emp_s = 0 if self_emp == 'No' else 1

    pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]], 
                             columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])

    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)

    # Display the result
    if predict[0] == 1:
        st.success(' Congratulations! Your Loan is Approved ')
    else:
        st.error(' Sorry, Your Loan Application has been Rejected ')
