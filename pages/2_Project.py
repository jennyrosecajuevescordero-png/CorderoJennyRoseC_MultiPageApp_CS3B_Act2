import streamlit as st
import random

st.set_page_config(page_title="My Project", page_icon="💼", layout="centered")

st.markdown("""
<style>
.hero {
    background: linear-gradient(to right, #BDA6CE, #9B8EC7);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

.image-card {
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    margin-top: 15px;
}

.stApp {
    background: linear-gradient(to right, #ACBAC4, #ECECEC);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>💼My Project</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ACBAC4, #ECECEC);
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎮Mini Games</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["❌⭕ Tic Tac Toe", "✊✋✌️ Rock Paper Scissors"])


with tab1:

    st.markdown("## ❌⭕ Tic Tac Toe")

    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.winner = None

    def check_winner(board):
        combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]

        for i, j, k in combos:
            if board[i] == board[j] == board[k] and board[i] != "":
                return board[i]

        if "" not in board:
            return "Draw"
        return None

    def ai_move():
        board = st.session_state.board

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                if check_winner(board) == "O":
                    return i
                board[i] = ""

        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                if check_winner(board) == "X":
                    board[i] = ""
                    return i
                board[i] = ""

        empty = [i for i in range(9) if board[i] == ""]
        return random.choice(empty) if empty else None

    def make_move(i):
        if st.session_state.board[i] == "" and not st.session_state.winner:
            st.session_state.board[i] = "X"
            st.session_state.winner = check_winner(st.session_state.board)

            if not st.session_state.winner:
                ai = ai_move()
                if ai is not None:
                    st.session_state.board[ai] = "O"
                    st.session_state.winner = check_winner(st.session_state.board)

    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            i = row * 3 + col
            val = st.session_state.board[i]

            display = "❌" if val == "X" else "⭕" if val == "O" else " "

            with cols[col]:
                st.button(display, key=f"t{i}", on_click=make_move, args=(i,))

    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.warning("😅 It's a Draw!")
        else:
            st.success(f"🏆 {st.session_state.winner} Wins!")

    if st.button("🔄 Restart Tic Tac Toe"):
        st.session_state.board = [""] * 9
        st.session_state.winner = None
        st.rerun()

with tab2:

    st.markdown("## ✊✋✌️ Rock Paper Scissors")

    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
        st.session_state.computer_score = 0

    choices = ["Rock ✊", "Paper ✋", "Scissors ✌️"]

    user_choice = st.radio("Choose:", choices, horizontal=True)

    if st.button("🔥 Play RPS"):

        computer_choice = random.choice(choices)

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"🙋 You: {user_choice}")

        with col2:
            st.warning(f"💻 Computer: {computer_choice}")

        if user_choice == computer_choice:
            st.markdown("### 🤝 Tie!")

        elif (
            (user_choice.startswith("Rock") and computer_choice.startswith("Scissors")) or
            (user_choice.startswith("Paper") and computer_choice.startswith("Rock")) or
            (user_choice.startswith("Scissors") and computer_choice.startswith("Paper"))
        ):
            st.markdown("### 🎉 You Win!")
            st.session_state.user_score += 1
        else:
            st.markdown("### 😢 You Lose!")
            st.session_state.computer_score += 1

    st.markdown("## 📊 Scoreboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🙋 You", st.session_state.user_score)

    with col2:
        st.metric("💻 Computer", st.session_state.computer_score)

    if st.button("🔄 Reset Score"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.rerun()