import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

genre_id = {
    'Action':28,
    'Adventure':12,
    'Animation':16,
    'Comedy':35,
    'Crime':80,
    'Documentary':99,
    'Drama':18,
    'Family':10751,
    'Fantasy':14,
    'History':36,
    'Horror':27,
    'Music':10402,
    'Mystery':9648,
    'Romance':10749,
    'Science Fiction':878,
    'TV Movie':10770,
    'Thriller':53,
    'War':10752,
    'Western':37   
}


class TmdbConnection(ExperimentalBaseConnection):
    def _connect(self):
        # Your TMDB API key and base URL
        api_key = "b1f4c14647b54d6f5b1a496ae02d486c"
        self.base_url = "https://api.themoviedb.org/3"
        self.headers = {
    		"accept": "application/json",
    		"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMWY0YzE0NjQ3YjU0ZDZmNWIxYTQ5NmFlMDJkNDg2YyIsInN1YiI6IjYyNWEzYTdhZDM4YjU4MDA5YzQ3MWRkOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DDNzwwmoe2wajypyCTHyA4A9n07hlXsYHl1mSE6xiuU"
		}
    def _request(self, method, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()
    def get_movie_from_genre(self,genre,page):
         ids=[]
         for i in genre:
              ids.append(str(genre_id[i]))
         ids="%2C".join(ids)
         endpoint=f"discover/movie?with_genres={ids}&sort_by:popularity.desc&page={page}"
         return self._request("GET",endpoint)
    def get_movie_thumnail(self,movie):
         return f"https://image.tmdb.org/t/p/w200{movie['poster_path']}"
    def get_auth_stat(self):
         endpoint="authentication"
         return self._request("GET",endpoint)
         
