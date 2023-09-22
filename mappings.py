# Create a custom dictionary to store the mappings for specific features
custom_feature_mappings = {
    'Day_of_week_encoded': {
        'Monday': 1,
        'Sunday': 3,
        'Friday': 0,
        'Wednesday': 6,
        'Saturday': 2,
        'Thursday': 4,
        'Tuesday': 5
    },
    'Age_band_of_driver_encoded': {
        '18-30': 0,
        '31-50': 1,
        'Under 18': 3,
        'Over 51': 2,
        'Unknown': 4
    },
    'Driving_experience_encoded': {
        '1-2yr': 0,
        'Above 10yr': 3,
        '5-10yr': 2,
        '2-5yr': 1,
        'No Licence': 5,
        'Below 1yr': 4,
        'unknown': 6
    },
    'Lanes_or_Medians_encoded': {
        'Two-way (divided with broken lines road marking)': 2,
        'Undivided Two way': 4,
        'other': 6,
        'Double carriageway (median)': 0,
        'One way': 1,
        'Two-way (divided with solid lines road marking)': 3,
        'Unknown': 5
    },
    'Types_of_Junction_encoded': {
        'No junction': 1,
        'Y Shape': 7,
        'Crossing': 0,
        'O Shape': 2,
        'Other': 3,
        'Unknown': 5,
        'T Shape': 4,
        'X Shape': 6
    },
    'Cause_of_accident_encoded': {
        'Moving Backward': 9,
        'Overtaking': 16,
        'Changing lane to the left': 0,
        'Changing lane to the right': 1,
        'Overloading': 14,
        'Other': 13,
        'No priority to vehicle': 12,
        'No priority to pedestrian': 11,
        'No distancing': 10,
        'Getting off the vehicle improperly': 7,
        'Improper parking': 8,
        'Overspeed': 15,
        'Driving carelessly': 3,
        'Driving at high speed': 2,
        'Driving to the left': 4,
        'Unknown': 19,
        'Overturning': 17,
        'Turnover': 18,
        'Driving under the influence of drugs': 5,
        'Drunk driving': 6
    },
    'Area_accident_occured_encoded': {
        'Residential areas': 9,
        'Office areas': 6,
        'Recreational areas': 1,
        'Industrial areas': 4,
        'Other': 7,
        'Church areas': 2,
        'Market areas': 0,
        'Unknown': 13,
        'Rural village areas': 10,
        'Outside rural areas': 5,
        'Hospital areas': 3,
        'School areas': 12,
        'Rural village areasOffice areas': 11,
        'Recreational areas': 8
    },
    'TimeLine_encoded': {
        'Evening': 1,
        'Night': 3,
        'Afternoon': 0,
        'Morning': 2
    },
    
    'Accident Severity' : {
        0 : 'Fatal injury',
        1 : 'Serious Injury',
        2 : 'Slight Injury'
    }
}


def get_encoded_value(feature_name,user_input):
    return custom_feature_mappings[feature_name][user_input]

