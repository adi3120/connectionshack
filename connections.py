import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests
import os

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
        access_token = os.environ.get("ACCESS_TOKEN")
        self.base_url = "https://api.themoviedb.org/3"
        self.headers = {
    		"accept": "application/json",
    		"Authorization": f"Bearer {access_token}"
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
    def search_movie_by_name(self, movie_name, page=1):
        endpoint = f"search/movie?query={movie_name}&page={page}"
        return self._request("GET", endpoint)

    def search_movie_by_actor(self, actor_name, page=1):
        endpoint = f"search/person?query={actor_name}&page={page}"
        response = self._request("GET", endpoint)
        actor_id = response.get("results", [])[0].get("id") if response.get("results") else None
        if actor_id:
            endpoint = f"discover/movie?with_cast={actor_id}&sort_by=popularity.desc&page={page}"
            return self._request("GET", endpoint)
        return {"results": []}

    def search_movie_by_director(self, director_name, page=1):
        endpoint = f"search/person?query={director_name}&page={page}"
        response = self._request("GET", endpoint)
        director_id = response.get("results", [])[0].get("id") if response.get("results") else None
        if director_id:
            endpoint = f"discover/movie?with_crew={director_id}&sort_by=popularity.desc&page={page}"
            return self._request("GET", endpoint)
        return {"results": []}
    def get_movie_cast(self, movie_id):
        endpoint = f"movie/{movie_id}/credits"
        return self._request("GET", endpoint)
         
