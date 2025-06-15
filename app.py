import streamlit as st
from recommender import recommend, movies

# Set page title and layout
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Optional custom CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🎥 Movie Recommendation System")
st.markdown("Find similar movies based on your favorite Bollywood or Hollywood films!")

# Sidebar Filter
st.sidebar.header("🔍 Filter Options")
source_option = st.sidebar.radio("Select Movie Source:", ["Both", "Bollywood", "Hollywood"])

# Filter movies based on source
if source_option == "Both":
    filtered_movies = movies
else:
    filtered_movies = movies[movies['source'] == source_option]

movie_list = sorted(filtered_movies['title'].unique())

# Movie Selection
selected_movie = st.selectbox("🎞️ Choose a Movie:", movie_list)

# Recommend Button
if st.button("Get Recommendations 🎯"):
    with st.spinner("🔎 Finding similar movies..."):
        results = recommend(selected_movie)

    st.subheader(f"📍 Recommendations based on **{selected_movie}**")

    # Layout as cards
    cols = st.columns(2)
    for i, movie in enumerate(results):
        with cols[i % 2]:
            st.markdown(f"""
                <div style='
                    background-color:#f0f2f6;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
                '>
                <h4>🎬 {movie}</h4>
                </div>
            """, unsafe_allow_html=True)

# Footer Credit
st.markdown("<div class='footer'>Made with ❤️ by <strong>Shreyam Dwivedi</strong></div>", unsafe_allow_html=True)

