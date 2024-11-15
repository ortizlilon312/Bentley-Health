import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Set up Streamlit app
st.title("Bentley University Healthy Lifestyle Recommendations")
st.write("Connect your health and fitness data to receive personalized recommendations for healthy campus activities.")

# Fetch data from iPhone Health App, Screen Time, and WHOOP
st.write("### Connecting to Health Data Sources...")

def get_health_data():
    try:
        # Placeholder API requests to get data from Health App, Screen Time, and WHOOP
        health_data = requests.get("https://example.com/api/health/iphone-health-app").json()
        screen_time_data = requests.get("https://example.com/api/health/screen-time").json()
        whoop_data = requests.get("https://example.com/api/health/whoop").json()
        return health_data, screen_time_data, whoop_data
    except Exception as e:
        st.error(f"Error fetching health data: {str(e)}")
        return None, None, None

if st.button("Fetch Health Data"):
    health_data, screen_time_data, whoop_data = get_health_data()

    if health_data and screen_time_data and whoop_data:
        # Display health and screen time data
        st.write("### Your Health Data Summary")
        st.write(f"- Daily steps: {health_data['daily_steps']} steps")
        st.write(f"- Active minutes: {health_data['active_minutes']} minutes")
        st.write(f"- Time in bed: {health_data['time_in_bed']} hours")

        st.write("### Your Screen Time Summary")
        st.write(f"- Average daily screen time: {screen_time_data['total_hours']} hours")
        st.write(f"- Most used app: {screen_time_data['most_used_app']} ({screen_time_data['most_used_app_time']} hours)")
        st.write(f"- Other apps usage: {screen_time_data['other_apps']}")

        st.write("### WHOOP Data Summary")
        st.write(f"- Recovery score: {whoop_data['recovery_score']}")
        st.write(f"- Strain score: {whoop_data['strain_score']}")
        st.write(f"- Sleep performance: {whoop_data['sleep_performance']}%
")

        # User Input: Activity Information
        st.write("### Activity Information")
        walk_days = st.number_input("How many days a week do you go for a walk?", min_value=0, max_value=7, step=1)
        walk_hours = st.number_input("How many hours do you spend walking weekly?", min_value=0.0, step=0.5)
        run_days = st.number_input("How many days a week do you go for a run?", min_value=0, max_value=7, step=1)
        run_hours = st.number_input("How many hours do you spend running weekly?", min_value=0.0, step=0.5)
        gym_days = st.number_input("How many days a week do you go to the gym?", min_value=0, max_value=7, step=1)
        gym_hours = st.number_input("How many hours do you spend at the gym weekly?", min_value=0.0, step=0.5)

        # Analysis and Recommendations
        st.write("### Recommendations Based on Health and Activity Data")
        avg_screen_time = screen_time_data['total_hours']
        if avg_screen_time > 4:
            st.warning(f"Your average daily screen time is {avg_screen_time:.2f} hours, which is quite high. Here are some recommendations to reduce screen time:")
            st.write("- Join an activity or club to reduce your time on the phone. Check out Bentley's CampusGroup app for activities that might interest you!")
            st.write("- Go for a walk around campus. Bentley's gym facilities and outdoor spaces are great options to help you be active!")
            st.write("- Consider attending a wellness event - there are workshops on stress management and yoga hosted by student services.")
        else:
            st.success(f"Great job! Your average daily screen time is {avg_screen_time:.2f} hours, which is in a healthy range!")
            st.write("- Check out upcoming fitness classes on Bentley CampusGroup to stay active and meet new people!")
            st.write("- Try adding some mindfulness practices to your routine, like a meditation session at the gym.")

        if walk_days + run_days + gym_days < 3:
            st.warning("Your weekly physical activity could be increased for better health. Consider adding more walks, runs, or gym sessions to your week.")
        else:
            st.success("Great job staying active! Keep up the good work with your regular physical activities.")
    else:
        st.write("No health data available.")

st.write("---")
st.write("We care about your well-being! Please use this application to track your lifestyle and be mindful of your health. Stay connected, stay healthy!")

