import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ACBAC4, #ECECEC);
    font-family: 'Segoe UI', sans-serif;
}

.home {
    background: linear-gradient(135deg, #6FB1FC, #4364F7);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
}

.card {
    padding: 25px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-6px);
}

.profile-img {
    border-radius: 50%;
    border: 6px solid #6FB1FC;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
}


.gradient-text {
    font-size: 28px;
    font-weight: bold;
    background: linear-gradient(90deg, #6FB1FC, #4364F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


div.stButton > button {
    height: 140px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    white-space: pre-line;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    border: 2px solid #4364F7;
}

</style>
""", unsafe_allow_html=True)

colA, colB = st.columns([2, 1])

with colA:
    st.markdown("""
    <div class="card">
        <div class="gradient-text">👋 Welcome to My Portfolio</div>
<p>
        I am passionate about building systems like E-Clearance platforms, 
        portfolio websites, and interactive applications using Python and Streamlit.
        I enjoy turning ideas into functional and user-friendly digital solutions.
</p>

<p>
        This portfolio showcases my skills, projects, and journey in tech.
        It reflects my growth as a developer and my dedication to continuous learning.
</p>

<p>
        I am particularly interested in developing systems that help schools 
        and organizations improve efficiency.
</p>

<p>
        My goal is to become a professional developer and create impactful systems.
</p>
    </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown("""
    <div style="text-align:center;">
    """, unsafe_allow_html=True)

    st.image(
        "pages/Messenger_creation_8C673E9D-0251-473A-9639-5F6B47E3F0E2.jpeg",
        width=230
    )

    st.markdown("""
        <p style="font-weight:bold; font-size:18px;">Jenny Rose C. Cordero</p>
        <p style="color:gray;">Aspiring Developer</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>🚀</h2>
        <h3>5+</h3>
        <p>Projects Built</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>💻</h2>
        <h3>4+</h3>
        <p>Tech Skills</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>🎯</h2>
        <h3>100%</h3>
        <p>Learning Dedication</p>
    </div>
    """, unsafe_allow_html=True)