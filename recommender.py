import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and prepare movie data
movies = pd.read_csv("tmdb_5000_movies.csv")[['title', 'overview']].dropna().reset_index(drop=True)

# Convert overview text to TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation logic
def recommend(title):
    title = title.lower()
    if title not in movies['title'].str.lower().values:
        return ["❌ Movie not found. Please check the spelling."]
    
    idx = movies[movies['title'].str.lower() == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].tolist()
