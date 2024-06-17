import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import ast


movies_data = pd.read_csv('C:/Users/efeba/projects/MovieProject/movies_metadata.csv', low_memory=False)

movies_data['overview'] = movies_data['overview'].fillna('')
movies_data['tagline'] = movies_data['tagline'].fillna('')
movies_data['genres'] = movies_data['genres'].fillna('')


def extract_genres(genres_str):
    try:
        genres_list = ast.literal_eval(genres_str)
        genre_name = genres_list[0]['name']
        return genre_name
    except:
        return ''


movies_data['genres_str'] = movies_data['genres'].apply(extract_genres)

movies_data['combined_text'] = movies_data['genres_str'] + ' ' + movies_data['overview'] + ' ' + movies_data['tagline']


tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_data['combined_text'])

# Calculate cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


def recommend_movie(movie_title):
    movie_index = movies_data[movies_data['title'] == movie_title].index[0]
    list_movie = sorted(list(enumerate(cosine_sim[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies_data.iloc[i[0]].title for i in list_movie]
    return recommended_movies
