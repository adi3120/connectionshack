from connections import *
from utils import display_movies
st.set_page_config(layout="wide")

tmdb_conn = st.experimental_connection("tmdb", TmdbConnection)
st.title("TMDB API | Streamlit connections hackathon")
st.title("Movie Recommendation System")
genre=[]
search_type = st.selectbox("Search movies by:", ["Genre", "Name", "Actor", "Director"])
page=1
movies=[]
if search_type == "Name":
    movie_name = st.text_input("Enter movie name:")
    movies = tmdb_conn.search_movie_by_name(movie_name).get("results", [])
elif search_type == "Actor":
    actor_name = st.text_input("Enter actor name:")
    movies = tmdb_conn.search_movie_by_actor(actor_name).get("results", [])
elif search_type == "Director":
    director_name = st.text_input("Enter director name:")
    movies = tmdb_conn.search_movie_by_director(director_name).get("results", [])
else:
     genre = st.multiselect("Select your favorite movie genre:", list(genre_id.keys()))
     if genre:
    	 movies = tmdb_conn.get_movie_from_genre(genre, page).get("results", [])
if movies:
	st.subheader("Movie Recommendations:")
	more_container = st.container()
	if movies:
		display_movies(tmdb_conn,movies,more_container,page)
				
		more=st.button("Display more")
		if more:
				page += 1
				if search_type == "Name":
					new_movies = tmdb_conn.search_movie_by_name(movie_name, page).get("results", [])
				elif search_type == "Actor":
					new_movies = tmdb_conn.search_movie_by_actor(actor_name, page).get("results", [])
				elif search_type == "Director":
					new_movies = tmdb_conn.search_movie_by_director(director_name, page).get("results", [])
				else:
					new_movies = tmdb_conn.get_movie_from_genre(genre, page).get("results", [])
				movies=new_movies
				display_movies(tmdb_conn, movies, more_container, page)


