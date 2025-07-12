import streamlit as st
import re

# Title
st.title("🔐 Smart Password Strength Checker")

st.write("Enter your password to see if it's secure and how to improve it.")

# Input field
password = st.text_input("Enter Password", type="password")

# Password rules
MIN_LENGTH = 8

# Function to evaluate password
def check_password_strength(pwd):
    rules = {
        "Minimum 8 characters": len(pwd) >= MIN_LENGTH,
        "Contains uppercase letter": re.search(r"[A-Z]", pwd) is not None,
        "Contains lowercase letter": re.search(r"[a-z]", pwd) is not None,
        "Contains number": re.search(r"[0-9]", pwd) is not None,
        "Contains special character": re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd) is not None
    }
    score = sum(rules.values())
    return score, rules

# Strength label
def get_strength_label(score):
    if score <= 2:
        return "Weak", "❌"
    elif score <= 4:
        return "Medium", "⚠️"
    else:
        return "Strong", "✅"

# Suggest improvements
def suggest_improvements(rules):
    suggestions = []
    for rule, passed in rules.items():
        if not passed:
            suggestions.append(f"➤ Add: {rule.lower()}")
    return suggestions

# Action
if st.button("Check Password"):
    if not password:
        st.warning("Please enter a password.")
    else:
        score, results = check_password_strength(password)
        label, icon = get_strength_label(score)

        st.subheader(f"{icon} Password Strength: {label}")
        st.write("### ✅ Rule Check:")
        for rule, passed in results.items():
            if passed:
                st.success(f"✅ {rule}")
            else:
                st.error(f"❌ {rule}")

        # Suggestions
        if label != "Strong":
            st.write("### 💡 Suggestions to Improve:")
            for tip in suggest_improvements(results):
                st.info(tip)
        else:
            st.balloons()
            st.success("Your password is strong! 🎉")

