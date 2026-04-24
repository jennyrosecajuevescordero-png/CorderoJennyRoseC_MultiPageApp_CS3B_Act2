import streamlit as st
st.set_page_config(page_title="Skills", page_icon="💡", layout="wide")

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
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.skill-label {
    font-weight: bold;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💡 Skills Dashboard</div>", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<div class="card">
    <h3>💻 Programming Skills</h3>
</div>
""", unsafe_allow_html=True)

python = st.slider("Python", 0, 100, 80)
st.progress(python)
st.write("Python")

js = st.slider("JavaScript", 0, 100, 70)
st.progress(js)
st.write("JavaScript")

php = st.slider("PHP", 0, 100, 75)
st.progress(php)
st.write("PHP")

st.write("---")

st.markdown("""
<div class="card">
    <h3>🎨 Design Skills</h3>
</div>
""", unsafe_allow_html=True)

design = st.slider("UI Design", 0, 100, 85)
st.progress(design)
st.write("UI/UX Design")

st.write("---")

st.markdown("""
<div class="card">
    <h3>🛠 Tools & Technologies</h3>
    <ul>
        <li>✔ GitHub</li>
        <li>✔ VS Code</li>
        <li>✔ Streamlit</li>
        <li>✔ HTML & CSS</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>💻</h2>
        <h3>Programming</h3>
        <p>Python, JS, PHP</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>🎨</h2>
        <h3>Design</h3>
        <p>UI/UX & Layouts</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h2>🛠</h2>
        <h3>Tools</h3>
        <p>GitHub, VS Code</p>
    </div>
    """, unsafe_allow_html=True)
