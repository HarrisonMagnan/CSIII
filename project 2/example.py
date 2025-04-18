import streamlit as st
st.title('My First Streamlit App')
import pandas as pd
import numpy as np
import os

#how to start streamlit (put in terminal) streamlit run example.py
#Local URL: http://localhost:8501
#Network URL: http://192.168.1.222:8501

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


# ---------- Custom Styling ---------- 
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
        color: #1e1e1e;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-family: 'Georgia', serif;
        font-size: 42px;
        color: #003366;
        padding-bottom: 10px;
    }
    h2, h3 {
        color: #003366;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stButton>button {
        background-color: #336699;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #2a4d7c;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------- Header ----------
st.markdown(
    "<div class='title'>✨📖 Welcome to the Ultimate Study Tracker! 🎓📊</div>",
    unsafe_allow_html=True
)

# ---------- Friends Seminary Logo and URL ----------
st.markdown(
    """
    <a href="https://www.friendsseminary.org" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/en/a/a6/FriendsSeminary225Logo.jpg" width="200"/>
    </a>
    """,
    unsafe_allow_html=True
)
# ---------- Data Setup ----------
DATA_FILE = "students.csv"

def preload_data():
    data = [
        ["001", 5, "Yes", "Evening", "Often", 6, "Flashcards", "Yes", 2, 3, 2.8],
        ["002", 0, "No", "Late Night", "Rarely", 3, "Watching Videos", "Yes", 5, 1, 1.2],
        ["003", 20, "Yes", "Afternoon", "Always", 10, "Practice Problems", "Yes", 0, 9, 4.0],
        ["004", 7, "No", "Morning", "Sometimes", 5, "Group Study", "No", 3, 2, 2.5],
        ["005", 16, "Yes", "Evening", "Always", 9, "Reading", "Yes", 1, 8, 3.7],
        ["006", 1, "No", "Evening", "Never", 2, "Flashcards", "No", 6, 0, 1.0],
        ["007", 8, "Yes", "Morning", "Often", 7, "Practice Problems", "Yes", 2, 4, 3.1],
        ["008", 2, "Yes", "Afternoon", "Rarely", 3, "Reading", "Yes", 5, 1, 1.6],
        ["009", 18, "No", "Late Night", "Always", 10, "Watching Videos", "No", 0, 10, 3.9],
        ["010", 6, "Yes", "Evening", "Often", 8, "Flashcards", "Yes", 2, 3, 3.2],
        ["011", 3, "No", "Morning", "Sometimes", 4, "Practice Problems", "Yes", 4, 2, 2.3],
        ["012", 22, "Yes", "Afternoon", "Always", 10, "Group Study", "Yes", 0, 9, 4.0],
        ["013", 0, "No", "Late Night", "Sometimes", 2, "Reading", "No", 6, 0, 1.4],
        ["014", 9, "No", "Evening", "Rarely", 5, "Watching Videos", "Yes", 3, 2, 2.6],
        ["015", 11, "Yes", "Afternoon", "Rarely", 8, "Practice Problems", "No", 1, 0, 3.4]
    ]
    columns = ["Student ID", "Study Hours", "Fixed Schedule", "Productive Time", "Notes Review",
               "Focus (1-10)", "Preferred Method", "Uses Apps", "Breaks", "Prep Days", "GPA"]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(DATA_FILE, index=False)

def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except Exception:
        preload_data()
        return pd.read_csv(DATA_FILE)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

df = load_data()

# ---------- Student Class ----------
class Student:
    def __init__(self, student_id, study_hours, fixed_schedule, productive_time,
                 notes_review, focus, method, uses_apps, breaks, prep_days, gpa):
        self.student_id = student_id
        self.study_hours = study_hours
        self.fixed_schedule = fixed_schedule
        self.productive_time = productive_time
        self.notes_review = notes_review
        self.focus = focus
        self.method = method
        self.uses_apps = uses_apps
        self.breaks = breaks
        self.prep_days = prep_days
        self.gpa = gpa

    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Study Hours": self.study_hours,
            "Fixed Schedule": self.fixed_schedule,
            "Productive Time": self.productive_time,
            "Notes Review": self.notes_review,
            "Focus (1-10)": self.focus,
            "Preferred Method": self.method,
            "Uses Apps": self.uses_apps,
            "Breaks": self.breaks,
            "Prep Days": self.prep_days,
            "GPA": self.gpa
        }

# ---------- Add Student ----------
st.markdown("---")
st.subheader("➕ Add a New Student")

with st.form("add_student"):
    student_id = st.text_input("Student ID")
    study_hours = st.number_input("Study Hours", 0, 24)
    fixed_schedule = st.selectbox("Fixed Schedule", ["Yes", "No"])
    productive_time = st.selectbox("Productive Time", ["Morning", "Afternoon", "Evening", "Late Night"])
    notes_review = st.selectbox("Notes Review", ["Always", "Often", "Sometimes", "Rarely", "Never"])
    focus = st.slider("Focus (1-10)", 1, 10)
    method = st.selectbox("Preferred Method", ["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"])
    uses_apps = st.selectbox("Uses Apps", ["Yes", "No"])
    breaks = st.number_input("Breaks", 0, 10)
    prep_days = st.number_input("Prep Days", 0, 30)
    gpa = st.number_input("GPA", 0.0, 4.0, step=0.1)

    submitted = st.form_submit_button("Add Student")

    if submitted:
        if student_id in df["Student ID"].values:
            st.error("Student ID already exists!")
        else:
            new_student = Student(student_id, study_hours, fixed_schedule, productive_time,
                                  notes_review, focus, method, uses_apps, breaks, prep_days, gpa)
            df = pd.concat([df, pd.DataFrame([new_student.to_dict()])], ignore_index=True)
            save_data(df)
            st.success(f"🎉 Student {student_id} added successfully!")

# ---------- View Students ----------
st.markdown("---")
st.subheader("📋 View All Students")
st.dataframe(df)

# ---------- Update Student ----------
st.markdown("---")
st.subheader("✏️ Update Student")
update_id = st.selectbox("Select Student ID to Update", df["Student ID"].unique() if not df.empty else [])

if update_id:
    student_data = df[df["Student ID"] == update_id].iloc[0]
    with st.form("update_student"):
        study_hours = st.number_input("Study Hours", 0, 24, value=int(student_data["Study Hours"]))
        fixed_schedule = st.selectbox("Fixed Schedule", ["Yes", "No"], index=["Yes", "No"].index(student_data["Fixed Schedule"]))
        productive_time = st.selectbox("Productive Time", ["Morning", "Afternoon", "Evening", "Late Night"], index=["Morning", "Afternoon", "Evening", "Late Night"].index(student_data["Productive Time"]))
        notes_review = st.selectbox("Notes Review", ["Always", "Often", "Sometimes", "Rarely", "Never"], index=["Always", "Often", "Sometimes", "Rarely", "Never"].index(student_data["Notes Review"]))
        focus = st.slider("Focus (1-10)", 1, 10, value=int(student_data["Focus (1-10)"]))
        method = st.selectbox("Preferred Method", ["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"], index=["Flashcards", "Practice Problems", "Watching Videos", "Reading", "Group Study"].index(student_data["Preferred Method"]))
        uses_apps = st.selectbox("Uses Apps", ["Yes", "No"], index=["Yes", "No"].index(student_data["Uses Apps"]))
        breaks = st.number_input("Breaks", 0, 10, value=int(student_data["Breaks"]))
        prep_days = st.number_input("Prep Days", 0, 30, value=int(student_data["Prep Days"]))
        gpa = st.number_input("GPA", 0.0, 4.0, step=0.1, value=float(student_data["GPA"]))

        updated = st.form_submit_button("Update Student")

        if updated:
            df.loc[df["Student ID"] == update_id, [
                "Study Hours", "Fixed Schedule", "Productive Time", "Notes Review",
                "Focus (1-10)", "Preferred Method", "Uses Apps", "Breaks", "Prep Days", "GPA"
            ]] = [study_hours, fixed_schedule, productive_time, notes_review,
                  focus, method, uses_apps, breaks, prep_days, gpa]
            save_data(df)
            st.success(f"✅ Student {update_id} updated!")

# ---------- Analysis ----------
st.markdown("---")
st.subheader("📊 Analyze Data with NumPy")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📈 Max GPA"):
        max_gpa = np.nanmax(df["GPA"])
        st.info(f"📚 The highest GPA is **{max_gpa}**")

with col2:
    if st.button("📉 Min Study Hours"):
        min_hours = np.nanmin(df["Study Hours"])
        st.warning(f"🕐 The lowest study time is **{min_hours} hours**")

with col3:
    if st.button("📊 Average Focus Level"):
        avg_focus = np.nanmean(df["Focus (1-10)"])
        st.success(f"🧠 Average focus level is **{avg_focus:.2f}/10**")
        
# ---------- GPA Visualizations ----------
st.markdown("---")
st.subheader("📈 GPA Visualizations")

# Histogram or Bar Chart of GPA Distribution
if st.checkbox("Show GPA Distribution Histogram"):
    st.write("### GPA Distribution")
    st.bar_chart(df["GPA"].value_counts().sort_index())

# Average GPA by Preferred Method
if st.checkbox("Show Average GPA by Study Method"):
    st.write("### Average GPA by Preferred Study Method")
    avg_gpa_by_method = df.groupby("Preferred Method")["GPA"].mean().sort_values(ascending=False)
    st.bar_chart(avg_gpa_by_method)
    
# ---------- Study Hours Visualization ----------
st.markdown("---")
st.subheader("🕒 Study Time Visualization")

if st.checkbox("Show Study Hours per Student"):
    st.write("### Study Hours by Student")
    st.bar_chart(df.set_index("Student ID")["Study Hours"])

import altair as alt
if st.checkbox("Show Study Hours per Student (Altair Chart)"):
    st.write("### Study Hours by Student (Interactive)")
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Student ID:N', title='Student ID'),
        y=alt.Y('Study Hours:Q', title='Hours Studied'),
        tooltip=['Student ID', 'Study Hours'],
        color=alt.Color('Study Hours:Q', scale=alt.Scale(scheme='blues'))
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)



# ---------- Delete Student ----------
st.markdown("---")
st.subheader("❌ Delete Student")
delete_id = st.selectbox("Select Student ID to Delete", df["Student ID"].unique() if not df.empty else [])

if delete_id:
    if st.button("Delete Student"):
        df = df[df["Student ID"] != delete_id]
        save_data(df)
        st.success(f"🗑️ Student {delete_id} deleted.")
