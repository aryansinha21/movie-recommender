import streamlit as st
from recommender import recommend

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.markdown("Get movie suggestions based on your favorite film!")

movie_name = st.text_input("Enter a movie title (e.g., Avatar):")

if st.button("Recommend"):
    with st.spinner("Searching for similar movies..."):
        results = recommend(movie_name)

    st.subheader("Top 5 Recommendations:")
    for i, title in enumerate(results):
        st.markdown(f"**{i + 1}.** {title}")
