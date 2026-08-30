import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# --------------------------------------------------
# SMOOTH UI TRANSITIONS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Main page fade */
    .main {
        animation: fadeIn 0.8s ease-in-out;
    }

    /* Section animation */
    .st-key-prediction-section,
    .st-key-suggestions-section,
    .st-key-action-section,
    .st-key-dashboard-section,
    .st-key-summary-section {
        animation: fadeInUp 0.8s ease-out;
    }

    /* Metric hover effect */
    div[data-testid="stMetric"] {
        transition: transform 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
    }

    /* Fade animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }

        to {
            opacity: 1;
        }
    }

    /* Slide + fade animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(25px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("student_performance_model.pkl")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎓 Student Performance Predictor")

st.markdown(
    "### AI-powered academic performance analysis & personalized guidance"
)

st.write(
    "Enter the student's details below to predict performance "
    "and receive personalized improvement suggestions."
)

st.divider()


# --------------------------------------------------
# STUDENT DETAILS
# --------------------------------------------------

st.header("📋 Student Details")

col1, col2 = st.columns(2)

with col1:

    study_hours = st.number_input(
        "📚 Study Hours per Day",
        min_value=0.0,
        max_value=24.0,
        value=6.0
    )

    attendance = st.number_input(
        "📅 Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )


with col2:

    previous_score = st.number_input(
        "📝 Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    sleep_hours = st.number_input(
        "😴 Sleep Hours",
        min_value=0.0,
        max_value=8.0,
        value=7.0
    )


st.divider()


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

if st.button(
    "🔮 Predict My Performance",
    use_container_width=True
):

    # --------------------------------------------------
    # PREPARE STUDENT DATA
    # --------------------------------------------------

    new_student = pd.DataFrame(
        [[
            study_hours,
            attendance,
            previous_score,
            sleep_hours
        ]],
        columns=[
            "study_hours",
            "attendance",
            "previous_score",
            "sleep_hours"
        ]
    )


    # --------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------

    prediction = model.predict(new_student)[0]


    # --------------------------------------------------
    # PREDICTION RESULT
    # --------------------------------------------------

    with st.container(key="prediction-section"):

        st.header("🎯 Prediction Result")

        if prediction == "High":

            st.success(
                "🌟 Predicted Performance: HIGH"
            )

            st.write(
                "Excellent! Your current academic habits are "
                "supporting good performance."
            )

        elif prediction == "Medium":

            st.warning(
                "📈 Predicted Performance: MEDIUM"
            )

            st.write(
                "Good effort! There are some areas where "
                "you can improve."
            )

        else:

            st.error(
                "🚀 Predicted Performance: LOW"
            )

            st.write(
                "There are several areas where improving "
                "your routine could help."
            )


    st.divider()


    # --------------------------------------------------
    # PERSONALIZED IMPROVEMENT SUGGESTIONS
    # --------------------------------------------------

    with st.container(key="suggestions-section"):

        st.header("💡 Personalized Improvement Suggestions")

        suggestions = []


        # Study Suggestions
        if study_hours < 3:

            suggestions.append(
                "📚 Your study time is quite low. "
                "Try building a consistent daily study routine."
            )

        elif study_hours < 5:

            suggestions.append(
                "📚 Your study time is moderate. "
                "Try adding some more focused study time."
            )

        else:

            suggestions.append(
                "✅ Good study routine! "
                "Keep maintaining your consistency."
            )


        # Attendance Suggestions
        if attendance < 75:

            suggestions.append(
                "📅 Your attendance is low. "
                "Try to attend classes more regularly."
            )

        elif attendance < 90:

            suggestions.append(
                "📅 Your attendance is okay. "
                "Try to maintain it above 90%."
            )

        else:

            suggestions.append(
                "✅ Excellent attendance! "
                "Keep maintaining it."
            )


        # Previous Score Suggestions
        if previous_score < 60:

            suggestions.append(
                "📝 Review previous topics and practice more "
                "questions to strengthen your basics."
            )

        elif previous_score < 80:

            suggestions.append(
                "📝 Review difficult topics and continue "
                "practicing regularly."
            )

        else:

            suggestions.append(
                "✅ Strong previous score! "
                "Keep up the good work."
            )


        # Sleep Suggestions
        if sleep_hours < 7:

            suggestions.append(
                "😴 Try to maintain a consistent sleep routine."
            )

        else:

            suggestions.append(
                "✅ Your sleep duration is within the target range."
            )


        # Display suggestions
        for suggestion in suggestions:

            st.info(suggestion)


    st.divider()


    # --------------------------------------------------
    # PERSONALIZED ACTION PLAN
    # --------------------------------------------------

    with st.container(key="action-section"):

        st.header("🎯 Personalized Action Plan")


        # Prediction Action
        if prediction == "High":

            st.success(
                "🌟 Your performance is predicted to be HIGH. "
                "Your main goal is to maintain your current habits."
            )

        elif prediction == "Medium":

            st.warning(
                "📈 Your performance is predicted to be MEDIUM. "
                "Focus on improving the areas identified below."
            )

        else:

            st.error(
                "🚀 Your performance is predicted to be LOW. "
                "Let's improve the important areas step by step."
            )


        # Study Action
        if study_hours < 5:

            st.write(
                "📚 **Study Action:** "
                "Increase your focused study time gradually."
            )

        else:

            st.write(
                "📚 **Study Action:** "
                "Maintain your current study routine."
            )


        # Attendance Action
        if attendance < 90:

            st.write(
                "📅 **Attendance Action:** "
                "Work toward maintaining attendance above 90%."
            )

        else:

            st.write(
                "📅 **Attendance Action:** "
                "Keep maintaining your excellent attendance."
            )


        # Academic Action
        if previous_score < 80:

            st.write(
                "📝 **Academic Action:** "
                "Revise previous topics and practice regularly."
            )

        else:

            st.write(
                "📝 **Academic Action:** "
                "Continue your strong academic performance."
            )


        # Sleep Action
        if sleep_hours < 7:

            st.write(
                "😴 **Sleep Action:** "
                "Try to maintain a consistent sleep routine."
            )

        else:

            st.write(
                "😴 **Sleep Action:** "
                "Keep maintaining your current sleep routine."
            )


    st.divider()


    # --------------------------------------------------
    # PERFORMANCE DASHBOARD
    # --------------------------------------------------

    with st.container(key="dashboard-section"):

        st.header("📊 Performance Dashboard")

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "📚 Study",
                f"{study_hours} hrs"
            )


        with col2:

            st.metric(
                "📅 Attendance",
                f"{attendance}%"
            )


        with col3:

            st.metric(
                "📝 Score",
                f"{previous_score}%"
            )


        with col4:

            st.metric(
                "😴 Sleep",
                f"{sleep_hours} hrs"
            )


        # Chart data
        chart_data = pd.DataFrame(
            {
                "Factor": [
                    "Study Hours",
                    "Attendance",
                    "Previous Score",
                    "Sleep Hours"
                ],

                "Value": [
                    (study_hours / 8) * 100,
                    attendance,
                    previous_score,
                    (sleep_hours / 8) * 100
                ]
            }
        )


        st.bar_chart(
            chart_data.set_index("Factor")
        )


        st.caption(
            "📊 Study and sleep are converted to a 0–100 scale "
            "for easier visual comparison."
        )


    st.divider()


    # --------------------------------------------------
    # STUDENT SUMMARY
    # --------------------------------------------------

    with st.container(key="summary-section"):

        st.header("👤 Student Summary")

        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "📚 Study Hours",
                study_hours
            )

            st.metric(
                "📅 Attendance",
                f"{attendance}%"
            )


        with col2:

            st.metric(
                "📝 Previous Score",
                f"{previous_score}%"
            )

            st.metric(
                "😴 Sleep Hours",
                sleep_hours
            )


    st.divider()


    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    st.caption(
        "🎓 Student Performance Predictor | "
        "Machine Learning Project"
    )

    st.caption(
        "Built with Python, Scikit-learn, Pandas & Streamlit"
    )