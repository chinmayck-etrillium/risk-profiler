import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Risk Profiling Tool", layout="centered")
st.title("🧠 Risk Profiling & Portfolio Recommendation")


st.header("📋 Investment Preferences Questionnaire")

# Questions (No default selected)
q1 = st.radio(
    "1️⃣ What's your investment horizon?",
    ["<1 year", "1-3 years", "3-5 years", "5-10 years", ">10 years"],
    index=None
)

q2 = st.radio(
    "2️⃣ How would you react to a 20% market crash?",
    ["Sell everything", "Sell some", "Hold", "Buy more", "Buy aggressively"],
    index=None
)

q3 = st.radio(
    "3️⃣ What's your main investment goal?",
    ["Protect capital", "Income", "Balanced", "Growth", "Max growth"],
    index=None
)

q4 = st.radio(
    "4️⃣ What's your age group?",
    ["60+", "50-59", "40-49", "30-39", "<30"],
    index=None
)

q5 = st.radio(
    "5️⃣ How stable is your income?",
    ["Very unstable", "Unstable", "Average", "Stable", "Very stable"],
    index=None
)

# Submit button
if st.button("✅ Submit & Get My Portfolio Suggestion"):

    # Check all questions answered
    if None in [q1, q2, q3, q4, q5]:
        st.warning("⚠️ Please answer all the questions before submitting.")
    else:
        # Calculate total score
        total_score = (
            ["<1 year", "1-3 years", "3-5 years", "5-10 years", ">10 years"].index(q1) +
            ["Sell everything", "Sell some", "Hold", "Buy more", "Buy aggressively"].index(q2) +
            ["Protect capital", "Income", "Balanced", "Growth", "Max growth"].index(q3) +
            ["60+", "50-59", "40-49", "30-39", "<30"].index(q4) +
            ["Very unstable", "Unstable", "Average", "Stable", "Very stable"].index(q5) + 5
        )

        # Risk profile logic
        if total_score <= 10:
            profile = "🟢 Conservative"
            allocation = {"Equity": 20, "Debt": 70, "Gold": 10}
        elif total_score <= 15:
            profile = "🟡 Moderate"
            allocation = {"Equity": 50, "Debt": 40, "Gold": 10}
        else:
            profile = "🔴 Aggressive"
            allocation = {"Equity": 80, "Debt": 10, "Gold": 10}

        # Display result
        st.success(f"Your Risk Profile: {profile}")
        st.write("💡 Suggested Portfolio Allocation:")

        for asset, pct in allocation.items():
            st.write(f"- {asset}: {pct}%")

        # Plot Pie Chart
        fig, ax = plt.subplots()
        ax.pie(allocation.values(), labels=allocation.keys(), autopct="%1.1f%%", startangle=90)
        ax.axis("equal") 
        st.pyplot(fig)

