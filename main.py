import streamlit as st
import pandas as pd

# Set up Streamlit app
st.title("Bentley University Healthy Lifestyle Recommendations")
st.write("Provide your screen time details to receive recommendations on healthy campus activities.")

# User Input: Questionnaire for Screen Time Data
st.write("### Please fill out the following information:")

# Get user inputs
total_screen_time = st.number_input("Enter your average daily screen time (in hours):", min_value=0.0, step=0.5)
time_in_bed = st.number_input("Enter your average time spent in bed daily (in hours):", min_value=0.0, step=0.5)
most_used_app = st.text_input("What is your most used app?")
most_used_app_time = st.number_input(f"How long do you use {most_used_app} daily (in hours):", min_value=0.0, step=0.5)
other_apps = st.text_area("List other apps you use frequently and their usage times (e.g., Instagram - 1.5 hours, TikTok - 2 hours):")

if st.button("Submit Screen Time Data"):
    # Display user input summary
    st.write("### Your Screen Time Summary")
    st.write(f"- Average daily screen time: {total_screen_time} hours")
    st.write(f"- Time in bed: {time_in_bed} hours")
    st.write(f"- Most used app: {most_used_app} ({most_used_app_time} hours)")
    st.write(f"- Other apps usage: {other_apps}")

    # Analysis and Recommendations
    st.write("### Recommendations Based on Screen Time")
    if total_screen_time > 4:
        st.warning(f"Your average daily screen time is {total_screen_time:.2f} hours, which is quite high. Here are some recommendations to reduce screen time:")
        st.write("- Join an activity or club to reduce your time on the phone. Check out Bentley's CampusGroup app for activities that might interest you!")
        st.write("- Go for a walk around campus. Bentley's gym facilities and outdoor spaces are great options to help you be active!")
        st.write("- Consider attending a wellness event - there are workshops on stress management and yoga hosted by student services.")
    else:
        st.success(f"Great job! Your average daily screen time is {total_screen_time:.2f} hours, which is in a healthy range!")
        st.write("- Check out upcoming fitness classes on Bentley CampusGroup to stay active and meet new people!")
        st.write("- Try adding some mindfulness practices to your routine, like a meditation session at the gym.")

st.write("---")
st.write("We care about your well-being! Please use this application to track your lifestyle and be mindful of your health. Stay connected, stay healthy!")
