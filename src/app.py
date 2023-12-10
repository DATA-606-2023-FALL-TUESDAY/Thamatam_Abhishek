import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load your preprocessed dataset
nyc = pd.read_csv("cleaned_nyc.csv")

# Define the Streamlit app
st.title("Health Inspection Predictive Modeling App")

# Sidebar
st.sidebar.title("Feature Selection")
selected_features = st.sidebar.multiselect("Select Features", ['SCORE','Month','Year', "BORO_Bronx", "BORO_Brooklyn", "BORO_Manhattan", "BORO_Queens", "BORO_Staten Island"])

# Get user input for feature values
st.sidebar.title("Input Features")
input_features = {}
for feature in selected_features:
    input_features[feature] = st.sidebar.number_input(f"Enter {feature}", value=0)

# Model Selection
model = st.sidebar.selectbox("Select Model", ["Random Forest", "Logistic Regression"])

# Load the trained model
if model == "Random Forest":
    clf = RandomForestClassifier(random_state=42)
    clf.fit(nyc[selected_features], nyc['CRITICAL FLAG'])
else:
    clf = LogisticRegression()
    clf.fit(nyc[selected_features], nyc['CRITICAL FLAG'])

# Calculate the probability
user_input = pd.DataFrame(input_features, index=[0])
probability = clf.predict_proba(user_input)

# Display the predicted probability
st.subheader("Predicted Probability")
st.write(f"The probability of health inspection failure is: {probability[0][1]:.2f}")
