import streamlit as st
import pandas as pd

# Placeholder - Replace with your data loading functions
def load_doctor_data():
    doctor_df = pd.read_csv("doctor.csv")
    specialist_df = pd.read_csv("specialist.csv")
    return doctor_df, specialist_df 

def doctor_recommendation_logic(predicted_disease):
   
    # Filter doctors based on specialization
    specialist_df_filtered = specialist_df[specialist_df['Disease'] == predicted_disease]
    specialists = specialist_df_filtered['Specialist'].tolist()
    specialist_doctors = doctor_df[doctor_df['Specialization'].isin(specialists)]
    # print(specialist_doctors)
    if specialist_doctors.empty:
        return None
    # Calculate doctor scores (if needed)
    def doctor_score(doctor_row, preference):
            if not specialist_doctors.empty:
                                experience = doctor_row['ExperienceYears']
                                rating = doctor_row['Rating']
                                distance = doctor_row['Distance']  # Assuming distance from user's location

                # Default weights
                                w_exp = 0.3
                                w_rating = 0.3
                                w_distance = 0.3

                # Adjust weights based on user's preference
                                if preference == "ExperienceYears":
                                     w_exp = 0.4
                                elif preference == "Distance":
                                     w_distance = 0.4
                                elif preference == "rating":
                                     w_rating = 0.4

                                return w_exp * experience + w_rating * rating - w_distance * distance 
            else:
                return None 
    if not specialist_doctors.empty:
        for factor in ["Distance", "ExperienceYears", "Rating"]:
            top_doctor_by_factor = specialist_doctors.sort_values(by=factor, ascending=False).iloc[0]

            st.subheader(f"Top Recommended Doctor based on {factor}:")
            st.write(f"Name: {top_doctor_by_factor['Doctor Name']}")
            st.write(f"Speciality: {top_doctor_by_factor['Specialization']}")
            st.write(f"Experience: {top_doctor_by_factor['ExperienceYears']} years")
            st.write(f"Average Rating: {top_doctor_by_factor['Rating']}")
    else:
        st.error("No doctors found with the required specialization.")

    # top_doctor = specialist_doctors.apply(lambda row: doctor_score(row, preference), axis=1).idxmax()
    # top_doctor_info = specialist_doctors.loc[top_doctor]
    # return top_doctor_info

# --- Page Content ---
st.title("Doctor Recommendations")

if 'predicted_disease' in st.session_state:
    predicted_disease = st.session_state['predicted_disease']
    

    doctor_df, specialist_df = load_doctor_data()  # Load data here 
    doctor_recommendation_logic(predicted_disease)
else:
    st.error("Please predict a disease on the main page first.")
