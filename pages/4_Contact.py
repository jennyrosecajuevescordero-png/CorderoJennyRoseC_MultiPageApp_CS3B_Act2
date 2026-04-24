import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ACBAC4, #ECECEC);
    font-family: 'Segoe UI', sans-serif;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #4A90E2;
}

.card {
    background: rgba(255,255,255,0.9);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

input, textarea {
    background-color: #f0fff0 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    border: 1px solid #ccc !important;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    background: #4A90E2;
    color: white;
    font-weight: bold;
    padding: 10px;
}

div.stButton > button:hover {
    background: #357ABD;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📞 Contact Me</div>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="card">
        <h3>💬 Send a Message</h3>
    """, unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    email = st.text_input("📧 Email")
    message = st.text_area("💬 Message")

    if st.button("🚀 Send Message"):
        if name and email and message:
            st.success(f"Thanks {name}! Your message has been sent ✅")
        else:
            st.error("Please complete all fields.")

    st.markdown("</div>", unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    <div class="card">
        <h3>🌐 Connect With Me</h3>
        <p>📍 Philippines</p>
        <p>📧 your.email@gmail.com</p>
        <p>📱 09XXXXXXXXX</p>
    </div>
    """, unsafe_allow_html=True)
    
st.write("---")
