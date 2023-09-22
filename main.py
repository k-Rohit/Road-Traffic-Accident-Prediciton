import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go
import pandas as pd
# import visualization
import mappings
import joblib

def home_page():
    st.title("Road Traffic Accident Severity Prediction")
    
    # Load the saved machine learning model
    encoding_model = joblib.load('models/label_encoder.pkl')
    rfc_model = joblib.load('models/random_forest_top_10_features.pkl')
    
    def preprocess_and_encode_inputs(user_inputs):
        # Encode the user inputs using the Label Encoder
        encoded_inputs = []
        for user_input, encoder in zip(user_inputs, [encoding_model] * len(user_inputs)):
            encoded_value = encoder.transform([user_input])[0]
            encoded_inputs.append(encoded_value)

        # Prepare the input data for the RandomForest model
        input_data = pd.DataFrame([encoded_inputs], columns=important_features)
    
        return input_data

    important_features = ['Day_of_week_encoded', 'Age_band_of_driver_encoded',
                        'Driving_experience_encoded', 'Lanes_or_Medians_encoded',
                        'Types_of_Junction_encoded', 'Cause_of_accident_encoded',
                        'Area_accident_occured_encoded', 'Hour of Accident',
                        'Number_of_casualties', 'TimeLine_encoded']

    options_day_of_week = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']

    option_age_band_of_driver = [
        '18-30', '31-50', 'Under 18', 'Over 51', 'Unknown']

    options_driving_experience = ['Below 1yr', '1-2yr', '2-5yr', '5-10yr',
                                'Above 10yr', 'No Licence', 'unknown']

    options_lanes_or_medians = ['Two-way (divided with broken lines road marking)', 'Undivided Two way',
                                'Double carriageway (median)', 'One way', 'Two-way (divided with solid lines road marking)',
                                'Unknown', 'other']

    options_types_of_junction = ['No junction', 'Y Shape', 'Crossing', 'O Shape', 'X Shape',
                                'T Shape', 'Unknown']

    options_cause_of_accident = ['Changing lane to the left', 'Changing lane to the right', 'Drunk driving', 'Driving at high speed', 'Driving carelessly', 'Driving to the left', 'Getting off the vehicle improperly', 'Improper parking', 'Moving Backward', 'No distancing', 'No priority to pedestrian', 'No priority to vehicle', 'Other', 'Overloading', 'Overturning', 'Overtaking',
                                'Overspeed', 'Turnover', 'Unknown',
                                'Driving under the influence of drugs']

    options_area_of_accident = ['Market areas', 'Recreational areas',
                                'Church areas', 'Hospital areas', 'Industrial areas',
                                'Office areas', 'Other', 'Outside rural areas',
                                'Residential areas', 'Rural village areas',
                                'Rural village areasOffice areas', 'School areas',
                                'Unknown'
                                ]

    options_hour_of_accident = [1, 2, 3, 4, 5, 6,
                                7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    options_number_of_casualties = [1, 2, 3, 4, 5, 6, 7, 8]
    
    options_time_of_day = [
        'Afternoon', 'Evening', 'Morning', 'Night'
    ]

    user_input_features = [
        ('Day_of_week_encoded', 'Enter the day of the week', options_day_of_week),
        ('Age_band_of_driver_encoded', 'Enter the age band of the driver', option_age_band_of_driver),
        ('Driving_experience_encoded', 'Select Driving Experience', options_driving_experience),
        ('Lanes_or_Medians_encoded', 'Select Lanes or Medians', options_lanes_or_medians),
        ('Types_of_Junction_encoded', 'Select Types of Junction', options_types_of_junction),
        ('Cause_of_accident_encoded', 'Select Cause of Accident', options_cause_of_accident),
        ('Area_accident_occured_encoded', 'Select Area of Accident', options_area_of_accident),
        ('TimeLine_encoded', 'Select Time of Day', options_time_of_day)
    ]

    # User inputs as a list
    user_inputs = []

    # Collect user inputs and get encoded values
    for feature_name, input_label, options in user_input_features:
        user_input = st.selectbox(input_label, options)
        user_inputs.append(mappings.get_encoded_value(feature_name, user_input))
        st.write(f"Selected {input_label}:", user_input)

    # Handle numeric inputs separately
    hour_of_accident = st.slider("Select Hour of Accident", min_value=1, max_value=17, step=1)
    user_inputs.append(hour_of_accident)
    st.write("Selected Hour of Accident:", hour_of_accident)

    number_of_casualties = st.slider("Select Number of Casualties", min_value=1, max_value=8, step=1)
    user_inputs.append(number_of_casualties)
    st.write("Selected Number of Casualties:", number_of_casualties)
    
    # Predict accident severity
    if st.button("Predict Accident Severity"):
    # Preprocess and encode user inputs
        input_data = preprocess_and_encode_inputs(user_inputs)
    
    # Make prediction
        predicted_severity = rfc_model.predict(input_data)[0]
    
    # Display the predicted severity to the user
    
        st.write(f"Predicted Accident Severity: {mappings.custom_feature_mappings['Accident Severity'][predicted_severity]}")
    
    else:
        st.write(f"Please press the button below to see prediction")
        
    

def page_data_input():
    st.title("Data Visualization Page")
    st.write("This is the data input page.")
    
    visualization.show_plots()
    
        
# Create a dictionary to map page names to their corresponding functions
pages = {
    "Home": home_page,
    "Data Input": page_data_input
}

st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox("Select Page", list(pages.keys()))

# Display the selected page
pages[selected_page]()




