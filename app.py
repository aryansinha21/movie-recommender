import streamlit as st
from recommender import recommend

# Page Config
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="centered", initial_sidebar_state="collapsed")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #F63366;'>🎬 Movie Recommender</h1>
    <h4 style='text-align: center; color: #AAAAAA;'>Made with ❤️ by Shreyam Dwivedi</h4>
    <br>
""", unsafe_allow_html=True)

# Input
movie_input = st.text_input("🔍 Enter a movie name (Bollywood or Hollywood):", placeholder="e.g., 3 Idiots, Inception")

# Button + Output
if st.button("Recommend"):
    if not movie_input.strip():
        st.warning("⚠️ Please enter a movie name.")
    else:
        recommendations = recommend(movie_input)
        if isinstance(recommendations, list) and recommendations[0].startswith("❌"):
            st.error(recommendations[0])
        else:
            st.markdown(f"### 📍 Recommendations based on **{movie_input.title()}**")
            cols = st.columns(2)
            for i, movie in enumerate(recommendations):
                with cols[i % 2]:
                    st.markdown(f"🎬 **{movie}**")

# Footer
st.markdown("""
    <hr style="margin-top: 30px; border-top: 1px solid #555;">
    <div style='text-align: center; font-size: 0.85em; color: #888;'>
        Built with ❤️ using Streamlit · Movie content from TMDB and public Bollywood data
    </div>
""", unsafe_allow_html=True)
