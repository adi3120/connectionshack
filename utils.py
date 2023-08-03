from connections import * 
import pandas as pd
def display_cast_names(cast_names):
    cast_df = pd.DataFrame({'Cast': cast_names})
    st.dataframe(cast_df)
    
def display_genres(genres):
    genre_df = pd.DataFrame({'Genres': genres})
    st.dataframe(genre_df)
    
def display_movies(tmdb_conn, movies, more_container, page):
    i=0
    if movies:
        for movie in movies:
            cast_info = tmdb_conn.get_movie_cast(movie['id'])
            cast_names = [actor['name'] for actor in cast_info.get('cast', [])]
            genres = movie['genre_ids']
            names = [list(genre_id.keys())[list(genre_id.values()).index(i)] for i in genres]
            col1, col2,col3,col4 = st.columns(4)
            with col1:
                st.image(tmdb_conn.get_movie_thumnail(movie), caption=movie['title'], width=200)
            with col2:
                   st.subheader(movie['title'])
                   show_movie_details(movie, tmdb_conn)
            with col3:
                  display_cast_names(cast_names)
            with col4:
                 display_genres(names)
            st.markdown("<hr>", unsafe_allow_html=True)
        i+=1

def show_movie_details(movie, tmdb_conn):
    movie_details = {
        'Release Date': movie['release_date'],
        # 'Overview': movie['overview'],
        'Language': [movie['original_language']],
        'Popularity Score': movie['popularity'],
        'Average votes': movie['vote_average'],
        'Vote count': movie['vote_count'],
    }
    st.write(f"Release Date : {movie_details['Release Date']}")
    st.write(f"Language : {movie['original_language']}")
    st.write(f"Popularity Score : {movie['popularity']}")
    st.write(f"Average votes : {movie['vote_average']}")
    st.write(f"Vote count : {movie['vote_count']}")
    
    