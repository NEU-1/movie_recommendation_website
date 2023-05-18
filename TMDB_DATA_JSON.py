import requests
import json

TMDB_API_KEY = 'a37782b08f823354bf51e4e5f7c07775'


def fetch_genre_data():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    return requests.get(url).json()['genres']


def genre_name(genres, genre_ids):
    genre_names = []
    for id in genre_ids:
        for genre in genres:
            if genre['id'] == id:
                genre_names.append(genre['name'])
    return genre_names


def fetch_movie_data(url, genres, page, is_active):
    result = []
    movies = requests.get(url.format(page)).json()
    for movie in movies['results']:
        if movie.get('release_date', '') and movie.get('backdrop_path', ''):
            fields = {
                'genres': genre_name(genres, movie['genre_ids']),
                'actors': [],
                'title': movie['title'],
                'released_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_average': movie['vote_average'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
            }
            result.append({
                "pk": movie['id'],
                "model": "movies.movie",
                "fields": fields
            })
    return result


def fetch_credit_data(movie_data):
    actor_data = []
    for data in movie_data:
        movie_id = data['pk']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}"
        credit_info = requests.get(url).json()
        actors = [cast['name'] for cast in credit_info['cast'][:5]]
        data['fields']['actors'] = actors
        if credit_info['crew']:
            data['fields']['director'] = credit_info['crew'][0]['name']
        
        for actor in actors:
            actor_data.append({"name": actor})

    return actor_data


def save_to_file(filename, data):
    with open(f"./{filename}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    genres = fetch_genre_data()
    genre_data = [{"pk": genre['id'], 'name': genre['name']} for genre in genres]

    movie_data = []
    for i in range(1, 20):
        popular_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        top_rated_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        is_active = 1 if i == 1 else 3
        movie_data.extend(fetch_movie_data(popular_url, genres, i, is_active))
        movie_data.extend(fetch_movie_data(top_rated_url, genres, i, is_active))

    actor_data = fetch_credit_data(movie_data)
    
    save_to_file("genre", genre_data)
    save_to_file("movies", movie_data)
    save_to_file("actors", actor_data)


if __name__ == "__main__":
    main()
