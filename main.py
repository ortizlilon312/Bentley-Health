import streamlit as st
import pandas as pd
import datetime

# Set up Streamlit app
st.title("Bentley University Healthy Lifestyle Recommendations")
st.write("Provide your health and fitness data to receive personalized recommendations for healthy campus activities.")

# Load or initialize data
if 'health_data' not in st.session_state:
    st.session_state['health_data'] = pd.DataFrame(columns=['date', 'steps', 'active_minutes', 'time_in_bed', 'screen_time', 'most_used_app', 'most_used_app_time', 'other_apps', 'walk_days', 'walk_hours', 'run_days', 'run_hours', 'gym_days', 'gym_hours', 'age', 'height', 'weight', 'affiliation'])

# User Input: Personal Information
st.write("### Please provide your personal information:")
age = st.number_input("Enter your age:", min_value=0, step=1)
height = st.number_input("Enter your height (in cm):", min_value=0.0, step=0.1)
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
affiliation = st.selectbox("Select your affiliation to Bentley University:", ["Undergraduate Student", "Graduate Student", "Faculty", "Staff", "Other"])

# User Input: Manual Entry of Health and Activity Information
st.write("### Please fill out the following health and activity information:")

# Get user inputs
date = st.date_input("Select the date:", min_value=datetime.date(2023, 1, 1), max_value=datetime.date.today())
steps = st.number_input("Enter your average daily steps:", min_value=0, step=100)
active_minutes = st.number_input("Enter your average active minutes per day:", min_value=0, step=5)
time_in_bed = st.number_input("Enter your average time spent in bed daily (in hours):", min_value=0.0, step=0.5)
total_screen_time = st.number_input("Enter your average daily screen time (in hours):", min_value=0.0, step=0.5)
most_used_app = st.text_input("What is your most used app?")
most_used_app_time = st.number_input(f"How long do you use {most_used_app} daily (in hours):", min_value=0.0, step=0.5)
other_apps = st.text_area("List other apps you use frequently and their usage times (e.g., Instagram - 1.5 hours, TikTok - 2 hours):")

# User Input: Activity Information
st.write("### Activity Information")
walk_days = st.number_input("How many days a week do you go for a walk?", min_value=0, max_value=7, step=1)
walk_hours = st.number_input("How many hours do you spend walking weekly?", min_value=0.0, step=0.5)
run_days = st.number_input("How many days a week do you go for a run?", min_value=0, max_value=7, step=1)
run_hours = st.number_input("How many hours do you spend running weekly?", min_value=0.0, step=0.5)
gym_days = st.number_input("How many days a week do you go to the gym?", min_value=0, max_value=7, step=1)
gym_hours = st.number_input("How many hours do you spend at the gym weekly?", min_value=0.0, step=0.5)

if st.button("Submit Health Data"):
    # Save data
    new_data = pd.DataFrame({
        'date': [date],
        'steps': [steps],
        'active_minutes': [active_minutes],
        'time_in_bed': [time_in_bed],
        'screen_time': [total_screen_time],
        'most_used_app': [most_used_app],
        'most_used_app_time': [most_used_app_time],
        'other_apps': [other_apps],
        'walk_days': [walk_days],
        'walk_hours': [walk_hours],
        'run_days': [run_days],
        'run_hours': [run_hours],
        'gym_days': [gym_days],
        'gym_hours': [gym_hours],
        'age': [age],
        'height': [height],
        'weight': [weight],
        'affiliation': [affiliation]
    })
    st.session_state['health_data'] = pd.concat([st.session_state['health_data'], new_data], ignore_index=True)
    st.success("Health data submitted successfully!")

# Display historical data and statistics
st.write("### Your Health Data Summary")
view_option = st.selectbox("View your data by:", ["Day", "Week", "Month", "Year"])

if not st.session_state['health_data'].empty:
    health_data = st.session_state['health_data']
    health_data['date'] = pd.to_datetime(health_data['date'])

    numeric_columns = health_data.select_dtypes(include='number').columns
    health_data[numeric_columns] = health_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

    if view_option == "Day":
        st.write(health_data)
    elif view_option == "Week":
        weekly_data = health_data.set_index('date').resample('W-Mon').mean().reset_index().sort_values(by='date', ascending=False)
        st.write(weekly_data)
    elif view_option == "Month":
        monthly_data = health_data.set_index('date').resample('M').mean().reset_index().sort_values(by='date', ascending=False)
        st.write(monthly_data)
    elif view_option == "Year":
        yearly_data = health_data.set_index('date').resample('Y').mean().reset_index().sort_values(by='date', ascending=False)
        st.write(yearly_data)

    # Visual Representation of Data
    st.write("### Visual Representation of Your Health Data")
    if view_option == "Day":
        chart_data = health_data.set_index('date')
    elif view_option == "Week":
        chart_data = weekly_data.set_index('date')
    elif view_option == "Month":
        chart_data = monthly_data.set_index('date')
    elif view_option == "Year":
        chart_data = yearly_data.set_index('date')

    st.line_chart(chart_data[['steps', 'active_minutes', 'screen_time']])

    # Analysis and Recommendations
    st.write("### Recommendations Based on Health and Activity Data")
    avg_screen_time = health_data['screen_time'].mean()
    if avg_screen_time > 4:
        st.warning(f"Your average daily screen time is {avg_screen_time:.2f} hours, which is quite high. Here are some recommendations to reduce screen time:")
        st.write("- Join an activity or club to reduce your time on the phone. Check out Bentley's CampusGroup app for activities that might interest you!")
        st.write("- Go for a walk around campus. Bentley's gym facilities and outdoor spaces are great options to help you be active!")
        st.write("- Consider attending a wellness event - there are workshops on stress management and yoga hosted by student services.")
    else:
        st.success(f"Great job! Your average daily screen time is {avg_screen_time:.2f} hours, which is in a healthy range!")
        st.write("- Check out upcoming fitness classes on Bentley CampusGroup to stay active and meet new people!")
        st.write("- Try adding some mindfulness practices to your routine, like a meditation session at the gym.")

    avg_activity_days = (health_data['walk_days'] + health_data['run_days'] + health_data['gym_days']).mean()
    if avg_activity_days < 3:
        st.warning("Your weekly physical activity could be increased for better health. Consider adding more walks, runs, or gym sessions to your week.")
        st.write("- Bentley's Fitness Center offers group classes that could make exercise more engaging.")
        st.write("- Join a recreational sports team through CampusGroup to stay active and have fun!")
    else:
        st.success("Great job staying active! Keep up the good work with your regular physical activities.")
        st.write("- Continue attending fitness classes or exploring new activities through Bentley's CampusGroup to maintain your healthy lifestyle.")

st.write("---")
st.write("We care about your well-being! Please use this application to track your lifestyle and be mindful of your health. Stay connected, stay healthy!")
