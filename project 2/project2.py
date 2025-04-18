#how to start streamlit (put in terminal) streamlit run project2.py
#  Local URL: http://localhost:8501
#  Network URL: http://10.10.170.91:8501

import streamlit as st
import pandas as pd
import numpy as np
import os
import altair as alt

# ---------- Sidebar Navigation ----------
# Allows user to switch between "Home" and "Analyze" pages
st.sidebar.title("📂 Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Analyze"])

# ---------- App Instructions & Authors ---------- 
st.markdown("## 🧭 How to Use This App")
st.markdown("""
Welcome to the Ultimate Study Tracker! Here's what you can do with this app:


- **Add a New Student** with their study habits, GPA, and preferences.
- **View All Students** in a sortable and scrollable table.
- **Update a Student's Data** to reflect changes in study behavior or performance.
- **Delete a Student** from the dataset if needed.
- **Analyze the Data** using built-in tools to find the max GPA, lowest study hours, or average focus levels.
- **Visualize Trends** in GPA and study time using charts and interactive graphs.


> 🎯 Use this tool to better understand how study habits relate to academic performance!
""")


st.markdown("#### 👨‍💻 Created by: Benjamin Jeong, Harrison Magnan, Eric Gomez, Zen Ze Chen")


# ---------- Custom Page Styling ----------
# CSS injected to customize font, background, and button appearance
# ---------- Floating YouTube Video ----------  
st.markdown(
    """
    <style>
    .video-container {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        width: 320px;
        height: 210px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        border-radius: 8px;
        overflow: hidden;
    }
    </style>

    <div class="video-container">
        <iframe width="320" height="210" src="https://www.youtube.com/embed/WW9CoY7xf7s?autoplay=1&mute=1&loop=1&playlist=WW9CoY7xf7s"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Data File Configuration ----------
# This is the CSV file where student data is stored
DATA_FILE = "students.csv"

# Preloads sample data into the CSV if the file doesn’t already exist
def preload_data():
    data = [
        ["001", 5, "Yes", "Evening", "Often", 6, "Flashcards", "Yes", 2, 3, 2.8],
        # ... other sample students
    ]
    columns = ["Student ID", "Study Hours", "Fixed Schedule", "Productive Time", "Notes Review",
               "Focus (1-10)", "Preferred Method", "Uses Apps", "Breaks", "Prep Days", "GPA"]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(DATA_FILE, index=False)

# Loads data from CSV, or preloads if the file doesn’t exist
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except:
        preload_data()
        return pd.read_csv(DATA_FILE)

# Saves updated student data to CSV
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Load the current data into a DataFrame
df = load_data()

# ---------- Student Class ----------
# Represents a student with their study habits and GPA
class Student:
    def __init__(self, student_id, study_hours, fixed_schedule, productive_time,
                 notes_review, focus, method, gpa):
        self.student_id = student_id
        self.study_hours = study_hours
        self.fixed_schedule = fixed_schedule
        self.productive_time = productive_time
        self.notes_review = notes_review
        self.focus = focus
        self.method = method
        #self.uses_apps = uses_apps
        #self.breaks = breaks
        #self.prep_days = prep_days
        self.gpa = gpa

    # Converts student data to a dictionary (used for adding to the DataFrame)
    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Study Hours": self.study_hours,
            "Fixed Schedule": self.fixed_schedule,
            "Productive Time": self.productive_time,
            "Notes Review": self.notes_review,
            "Focus (1-10)": self.focus,
            "Preferred Method": self.method,
            #"Uses Apps": self.uses_apps,
            #"Breaks": self.breaks,
            #"Prep Days": self.prep_days,
            "GPA": self.gpa
        }

# ============ HOME PAGE ============ #
if page == "Home":
    # Header and intro
    st.markdown("<div class='title'>✨📖 Welcome to the Ultimate Study Tracker!</div>", unsafe_allow_html=True)
    st.markdown("#### 👨‍💻 Created by: Benjamin Jeong, Harrison Magnan, Eric Gomez, Zen Ze Chen")

    # App usage instructions (you can expand this section)
    st.markdown("## 🧭 How to Use This App")
    st.markdown("""...""")

    # ------- Add Student Form -------
    st.subheader("➕ Add a New Student")
    with st.form("add_student"):
        # Input fields for each data attribute
        student_id = st.text_input("Student ID")
        study_hours = st.number_input("Study Hours", 0, 24)
        fixed_schedule = st.selectbox("Fixed Schedule", ["Yes", "No"])
        productive_time = st.selectbox("Productive Time", ["Morning", "Afternoon", "Evening", "Late Night"])
        notes_review = st.selectbox("Notes Review", ["Always", "Often", "Sometimes", "Rarely", "Never"])
        focus = st.slider("Focus (1-10)", 1, 10)
        method = st.selectbox("Preferred Method", ["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"])
        #uses_apps = st.selectbox("Uses Apps", ["Yes", "No"])
        #breaks = st.number_input("Breaks", 0, 10)
        #prep_days = st.number_input("Prep Days", 0, 30)
        gpa = st.number_input("GPA", 0.0, 4.0, step=0.1)
        submitted = st.form_submit_button("Add Student")

        # Adds student if ID is unique
        if submitted:
            if student_id in df["Student ID"].values:
                st.error("Student ID already exists!")
            else:
                new_student = Student(student_id, study_hours, fixed_schedule, productive_time,
                                      notes_review, focus, method, uses_apps, breaks, prep_days, gpa)
                df = pd.concat([df, pd.DataFrame([new_student.to_dict()])], ignore_index=True)
                save_data(df)
                st.success(f"🎉 Student {student_id} added successfully!")

    # ------- View All Students -------
    st.subheader("📋 View All Students")
    st.dataframe(df)

    # ------- Update Student Section -------
    st.subheader("✏️ Update Student")
    update_id = st.selectbox("Select Student ID to Update", df["Student ID"].unique() if not df.empty else [])
    if update_id:
        student_data = df[df["Student ID"] == update_id].iloc[0]
        with st.form("update_student"):
            # Pre-fills inputs with current values
            study_hours = st.number_input("Study Hours", 0, 24, value=int(student_data["Study Hours"]))
            fixed_schedule = st.selectbox("Fixed Schedule", ["Yes", "No"], index=["Yes", "No"].index(student_data["Fixed Schedule"]))
            productive_time = st.selectbox("Productive Time", ["Morning", "Afternoon", "Evening", "Late Night"], index=["Morning", "Afternoon", "Evening", "Late Night"].index(student_data["Productive Time"]))
            notes_review = st.selectbox("Notes Review", ["Always", "Often", "Sometimes", "Rarely", "Never"], index=["Always", "Often", "Sometimes", "Rarely", "Never"].index(student_data["Notes Review"]))
            focus = st.slider("Focus (1-10)", 1, 10, value=int(student_data["Focus (1-10)"]))
            method = st.selectbox("Preferred Method", ["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"], index=["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"].index(student_data["Preferred Method"]))
            #uses_apps = st.selectbox("Uses Apps", ["Yes", "No"], index=["Yes", "No"].index(student_data["Uses Apps"]))
            #breaks = st.number_input("Breaks", 0, 10, value=int(student_data["Breaks"]))
            #prep_days = st.number_input("Prep Days", 0, 30, value=int(student_data["Prep Days"]))
            gpa = st.number_input("GPA", 0.0, 4.0, step=0.1, value=float(student_data["GPA"]))
            updated = st.form_submit_button("Update Student")

            if updated:
                # Update the DataFrame with new values
                df.loc[df["Student ID"] == update_id, [
                    "Study Hours", "Fixed Schedule", "Productive Time", "Notes Review",
                    "Focus (1-10)", "Preferred Method", "GPA"
                ]] = [study_hours, fixed_schedule, productive_time, notes_review,
                      focus, method, gpa]
                save_data(df)
                st.success(f"✅ Student {update_id} updated!")

    # ------- Delete Student Section -------
    st.subheader("❌ Delete Student")
    delete_id = st.selectbox("Select Student ID to Delete", df["Student ID"].unique() if not df.empty else [])
    if delete_id:
        if st.button("Delete Student"):
            df = df[df["Student ID"] != delete_id]
            save_data(df)
            st.success(f"🗑️ Student {delete_id} deleted.")

# ============ ANALYZE PAGE ============ #
elif page == "Analyze":
    st.markdown("<div class='title'>📊 Analyze Study Habits</div>", unsafe_allow_html=True)

    st.markdown("Use the buttons below to analyze GPA, Focus, and Study Hours using NumPy.")

    # Stats using NumPy functions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 Max GPA"):
            max_gpa = np.nanmax(df["GPA"])
            st.info(f"📚 The highest GPA recorded is **{max_gpa}**.")

    with col2:
        if st.button("📉 Min Study Hours"):
            min_hours = np.nanmin(df["Study Hours"])
            st.warning(f"🕐 The fewest study hours is **{min_hours}** hour(s).")

    with col3:
        if st.button("📊 Average Focus Level"):
            avg_focus = np.nanmean(df["Focus (1-10)"])
            st.success(f"🧠 Average focus level across all students is **{avg_focus:.2f}/10**.")

    st.markdown("---")
    st.subheader("📈 GPA Visualizations")

    # GPA Histogram
    if st.checkbox("Show GPA Distribution Histogram"):
        st.write("### GPA Distribution")
        st.bar_chart(df["GPA"].value_counts().sort_index())

    # Average GPA by preferred study method
    if st.checkbox("Show Average GPA by Study Method"):
        st.write("### Average GPA by Preferred Study Method")
        avg_gpa_by_method = df.groupby("Preferred Method")["GPA"].mean().sort_values(ascending=False)
        st.bar_chart(avg_gpa_by_method)

    st.markdown("---")
    st.subheader("🕒 Study Time Visualizations")

    # Study hours per student (basic)
    if st.checkbox("Show Study Hours per Student"):
        st.write("### Study Hours by Student")
        st.bar_chart(df.set_index("Student ID")["Study Hours"])

    # Interactive Altair bar chart for study hours
    if st.checkbox("Show Study Hours per Student (Altair Chart)"):
        st.write("### Study Hours by Student (Interactive)")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('Student ID:N', title='Student ID'),
            y=alt.Y('Study Hours:Q', title='Hours Studied'),
            tooltip=['Student ID', 'Study Hours'],
            color=alt.Color('Study Hours:Q', scale=alt.Scale(scheme='blues'))
        ).properties(width=600, height=400)
        st.altair_chart(chart, use_container_width=True)
