import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ACBAC4, #ECECEC);
    font-family: 'Segoe UI', sans-serif;
}

.header {
    background: linear-gradient(135deg, #30364F, #576A8F);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
}

.card {
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-6px);
}

.profile-img {
    border-radius: 50%;
    border: 5px solid #6FB1FC;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}

.skill {
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>👤 About Me</h1>
    <p>Get to know more about me</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <p style="color:gray; font-size:16px;">Aspiring Developer</p>
        <hr>
        <p style="font-size:14px;">
        Passionate about building systems and creating user-friendly applications.
        Focused on learning and improving development skills every day.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>👋 Hello!</h2>
<p>
        I am a passionate student and aspiring developer from the Philippines.
        I enjoy building systems that solve real-world problems, especially for schools.
</p>

<p>
        I work with <b>Python, Streamlit, HTML, and CSS</b> and focus on creating
        clean and user-friendly designs.
</p>

<p>
        My goal is to become a professional developer and create impactful systems
        that improve efficiency and user experience.
</p>
    </div>
    """, unsafe_allow_html=True)
    
st.write("---")

st.markdown("""
<div class="card">
    <h3>🎯 Goals</h3>
    <p>✔ Become financially successful</p>
    <p>✔ Build a peaceful and stable future</p>
    <p>✔ Travel and live a meaningful life</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<div class="card">
    <h3>🎯 Interests</h3>
    <ul>
        <li>Web Development</li>
        <li>System Design</li>
        <li>UI/UX Design</li>
        <li>Learning New Technologies</li>
    </ul>
</div>
""", unsafe_allow_html=True)

