import streamlit as st
import pandas as pd

# Set up Streamlit app
st.title("Bentley University Healthy Lifestyle Recommendations")
st.write("Provide your health and fitness data to receive personalized recommendations for healthy campus activities.")

# User Input: Manual Entry of Health and Activity Information
st.write("### Please fill out the following information:")

# Get user inputs
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
    # Display user input summary
    st.write("### Your Health Data Summary")
    st.write(f"- Daily steps: {steps} steps")
    st.write(f"- Active minutes: {active_minutes} minutes")
    st.write(f"- Time in bed: {time_in_bed} hours")
    st.write(f"- Average daily screen time: {total_screen_time} hours")
    st.write(f"- Most used app: {most_used_app} ({most_used_app_time} hours)")
    st.write(f"- Other apps usage: {other_apps}")

    # Analysis and Recommendations
    st.write("### Recommendations Based on Health and Activity Data")
    if total_screen_time > 4:
        st.warning(f"Your average daily screen time is {total_screen_time:.2f} hours, which is quite high. Here are some recommendations to reduce screen time:")
        st.write("- Join an activity or club to reduce your time on the phone. Check out Bentley's CampusGroup app for activities that might interest you!")
        st.write("- Go for a walk around campus. Bentley's gym facilities and outdoor spaces are great options to help you be active!")
        st.write("- Consider attending a wellness event - there are workshops on stress management and yoga hosted by student services.")
    else:
        st.success(f"Great job! Your average daily screen time is {total_screen_time:.2f} hours, which is in a healthy range!")
        st.write("- Check out upcoming fitness classes on Bentley CampusGroup to stay active and meet new people!")
        st.write("- Try adding some mindfulness practices to your routine, like a meditation session at the gym.")

    if walk_days + run_days + gym_days < 3:
        st.warning("Your weekly physical activity could be increased for better health. Consider adding more walks, runs, or gym sessions to your week.")
        st.write("- Bentley's Fitness Center offers group classes that could make exercise more engaging.")
        st.write("- Join a recreational sports team through CampusGroup to stay active and have fun!")
    else:
        st.success("Great job staying active! Keep up the good work with your regular physical activities.")
        st.write("- Continue attending fitness classes or exploring new activities through Bentley's CampusGroup to maintain your healthy lifestyle.")

st.write("---")
st.write("We care about your well-being! Please use this application to track your lifestyle and be mindful of your health. Stay connected, stay healthy!")


