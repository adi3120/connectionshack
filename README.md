[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://experimentalconnectionmovierecommendation.streamlit.app/)
# Usage 
## Search movies by Genre
![Screenshot 2023-08-03 171505](https://github.com/adi3120/connectionshack/assets/83342917/f5cbd44b-f0d5-445d-93f5-84f96aac390a)
## Search movies by Name
![Screenshot 2023-08-03 171545](https://github.com/adi3120/connectionshack/assets/83342917/bf2e3fd0-54bd-45ac-a03a-7485fb04edc7)
## Search movies by Actor 
![Screenshot 2023-08-03 171701](https://github.com/adi3120/connectionshack/assets/83342917/bad69480-9844-4b18-870c-96ddfbda2c3b)
## Search movies by Director
![Screenshot 2023-08-03 171743](https://github.com/adi3120/connectionshack/assets/83342917/4c94fbde-ef7c-4300-9d65-45b00de82cc5)

### Behind the scenes
> TmdbConnection class 
```
class TmdbConnection(ExperimentalBaseConnection):

```

> _connect implementation
```
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
```
> getting movies from genres selected
```
def get_movie_from_genre(self,genre,page):
         ids=[]
         for i in genre:
              ids.append(str(genre_id[i]))
         ids="%2C".join(ids)
         endpoint=f"discover/movie?with_genres={ids}&sort_by:popularity.desc&page={page}"
         return self._request("GET",endpoint)
```

> getting movies by name
```
def search_movie_by_name(self, movie_name, page=1):
        endpoint = f"search/movie?query={movie_name}&page={page}"
        return self._request("GET", endpoint)
```

> getting movies by actor name
```
def search_movie_by_actor(self, actor_name, page=1):
        endpoint = f"search/person?query={actor_name}&page={page}"
        response = self._request("GET", endpoint)
        actor_id = response.get("results", [])[0].get("id") if response.get("results") else None
        if actor_id:
            endpoint = f"discover/movie?with_cast={actor_id}&sort_by=popularity.desc&page={page}"
            return self._request("GET", endpoint)
        return {"results": []}
```

> getting movies by director name
```
def search_movie_by_director(self, director_name, page=1):
        endpoint = f"search/person?query={director_name}&page={page}"
        response = self._request("GET", endpoint)
        director_id = response.get("results", [])[0].get("id") if response.get("results") else None
        if director_id:
            endpoint = f"discover/movie?with_crew={director_id}&sort_by=popularity.desc&page={page}"
            return self._request("GET", endpoint)
        return {"results": []}
```
> get cast information for a movie
```
def get_movie_cast(self, movie_id):
        endpoint = f"movie/{movie_id}/credits"
        return self._request("GET", endpoint)
```

> get thumbnail of a movie
```
def get_movie_thumnail(self,movie):
         return f"https://image.tmdb.org/t/p/w200{movie['poster_path']}"
```
