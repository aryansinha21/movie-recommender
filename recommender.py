import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Hollywood movies
tmdb = pd.read_csv("tmdb_5000_movies.csv")[['title', 'overview']]

# Load Bollywood movies
bollywood = pd.read_csv("bollywood_movies.csv")  # make sure the file name matches
bollywood = bollywood[['Movie_Name', 'Plot']]  # adjust based on actual columns
bollywood.columns = ['title', 'overview']

# Combine both datasets
movies = pd.concat([tmdb, bollywood], ignore_index=True)
movies.dropna(inplace=True)
movies.reset_index(drop=True, inplace=True)

# Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend function
def recommend(title):
    title = title.lower()
    if title not in movies['title'].str.lower().values:
        return ["❌ Movie not found. Try a different name."]
    
    idx = movies[movies['title'].str.lower() == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices].tolist()
