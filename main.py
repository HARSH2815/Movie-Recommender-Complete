import pickle
import streamlit as st
import requests
import gdown
import os

# -----------------------------------
# 🎬 Convert IMDB → TMDB + Fetch Poster
# -----------------------------------
def fetch_poster(imdb_id):
    try:
        # ✅ Convert numeric → IMDB format
        imdb_id = "tt" + str(imdb_id).zfill(7)

        # Step 1: IMDB → TMDB
        url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&external_source=imdb_id"
        data = requests.get(url).json()

        if not data['movie_results']:
            return None

        tmdb_id = data['movie_results'][0]['id']

        # Step 2: TMDB → Poster
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        data = requests.get(url).json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        return None

    except:
        return None


# -----------------------------------
# 🎯 Recommendation Function
# -----------------------------------


# -----------------------------------
# 📥 Load Data
# -----------------------------------
st.header('🎬 Movie Recommender System')

movies = pickle.load(open('movie_list.pkl', 'rb'))

# ✅ Fix column names
movies.columns = movies.columns.str.replace(' ', '_')


# @st.cache_data
def load_similarity():
    url="https://drive.google.com/uc?id=1gZR5ix4q66N3mqKfIAnOuBaK-iQI1d77"
    output = "similarity.pkl"
    gdown.download(url, output, quiet=False)
    return pickle.load(open(output, 'rb'))

similarity = load_similarity()


def recommend(movie):
    if movie not in movies['movie_title'].values:
        return [], []

    index = movies[movies['movie_title'] == movie].index[0]

    # ✅ Directly use stored similarities
    distances = similarity[index]

    names = []
    posters = []

    for i in distances[:5]:
        row = movies.iloc[i[0]]

        movie_name = row['movie_title']
        imdb_id = row['imdb_id']

        poster = fetch_poster(imdb_id)

        names.append(movie_name)
        posters.append(poster)

    return names, posters


# -----------------------------------
# 🎛️ UI
# -----------------------------------
movie_list = movies['movie_title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


# -----------------------------------
# 🎯 Show Recommendation
# -----------------------------------
if st.button('Show Recommendation'):

    selected_row = movies[movies['movie_title'] == selected_movie].iloc[0]

    selected_imdb_id = selected_row['imdb_id']
    selected_poster = fetch_poster(selected_imdb_id)

    st.subheader("Selected Movie")
    st.text(selected_movie)

    if selected_poster:
        st.image(selected_poster, width=200)
    else:
        st.text("Poster not available")

    names, posters = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            if i < len(names):
                st.text(names[i])
                if posters[i]:
                    st.image(posters[i])
                else:
                    st.text("No Image")
