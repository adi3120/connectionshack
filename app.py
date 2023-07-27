from connections import *
from utils import display_movies
st.set_page_config(layout="wide")


tmdb_conn = st.experimental_connection("tmdb", TmdbConnection)
st.title("Movie Recommendation System | TMDB API | Streamlit connections hackathon")

genre = st.multiselect("Select your favorite movie genre:", list(genre_id.keys()))
page=1
movies = tmdb_conn.get_movie_from_genre(genre,page).get("results",[])

st.subheader("Movie Recommendations:")
more_container = st.container()

display_movies(tmdb_conn,movies,more_container,page)
		
more=st.button("Display more")
if(more):
	page+=1
	movies=tmdb_conn.get_movie_from_genre(genre,page).get("results",[])
	display_movies(tmdb_conn,movies,more_container,page)
		
	
footer="""<style>
.footer {
position:fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by Aditya Yadav for </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)