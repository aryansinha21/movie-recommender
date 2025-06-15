import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Hollywood data
tmdb = pd.read_csv("tmdb_5000_movies.csv")[['title', 'overview']].dropna()

# Bollywood data
bollywood = pd.read_csv("bollywood_movies.csv", encoding='utf-8', on_bad_lines='skip')[['Name', 'Overview']]
bollywood.columns = ['title', 'overview']

# Combine
movies = pd.concat([tmdb, bollywood], ignore_index=True)
movies.dropna(inplace=True)
movies.reset_index(drop=True, inplace=True)

# TF-IDF + similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
cosine_sim = cosine_similarity(tfidf_matrix)

def recommend(title):
    title = title.lower()
    titles = movies['title'].str.lower()
    if title not in titles.values:
        return ["❌ Movie not found. Try a Bollywood or Hollywood name."]
    idx = titles[titles == title].index[0]
    sim_scores = sorted(enumerate(cosine_sim[idx]), key=lambda x: x[1], reverse=True)[1:6]
    return movies['title'].iloc[[i[0] for i in sim_scores]].tolist()


