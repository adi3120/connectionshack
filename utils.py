from connections import * 
def display_movies(tmdb_conn,movies,more_container,page):
     if movies:
        with more_container:
              for movie in movies:
                    col1,col2=st.columns(2)
                    with col1:
                           st.subheader(movie['title'])
                           genres=movie['genre_ids']
                           names=[]
                           for i in genres:
                                  names.append(list(genre_id.keys())[list(genre_id.values()).index(i)])
                                
                           st.json(
                                {
                                     'Release Date':movie['release_date'],
                                     'Overview':movie['overview'],
                                     'Language':movie['original_language'],
                                     'Popularity Score':movie['popularity'],
                                     'Average votes':movie['vote_average'],
                                     'Vote count':movie['vote_count'],
                                     'Genres':names
                                     
								}
						   )
                           
                    with col2:
                          st.image(tmdb_conn.get_movie_thumnail(movie), caption=movie['title'], width=400)
		