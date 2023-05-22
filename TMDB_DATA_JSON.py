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



def fetch_movie_data(url, page):
    result = []
    movies = requests.get(url.format(page)).json()
    for movie in movies['results']:
        youtube_key = get_youtube_key(movie)
        if movie.get('release_date', '') and movie.get('backdrop_path', ''):
            fields = {
                'genres': movie['genre_ids'],
                'actors': [],
                'title': movie['title'],
                'release_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_average': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'youtube_key': youtube_key   
            }
            result.append({
                "pk": movie['id'],
                "model": "movies.movie",
                "fields": fields
            })
    return result



def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': TMDB_API_KEY
        }
    ).json()
    # return response
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            if video.get('type') == 'Teaser':
                return video.get('key')
            elif video.get('type') == 'Trailer':
                return video.get('key')
    return 'nothing'



def fetch_credit_data(movie_data):
    actor_dict = {}
    for data in movie_data:
        movie_id = data['pk']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}"
        credit_info = requests.get(url).json()
        actors = [cast for cast in credit_info['cast'][:5]]
        data['fields']['actors'] = [actor['id'] for actor in actors]

        for actor in actors:
            if actor['id'] not in actor_dict:
                actor_dict[actor['id']] = {
                    "pk": actor['id'],
                    "model": "movies.actor",
                    "fields": {
                        "name": actor['name']
                    }
                }
        print(data.get('fields').get('title')) 
    return list(actor_dict.values())




def save_to_file(filename, data):
    with open(f"./{filename}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def main():
    genres = fetch_genre_data()
    genre_data = [{"pk": genre['id'], "model": "movies.genre", "fields": {'name': genre['name']}} for genre in genres]

    movie_data = []
    for i in range(1, 20):
        popular_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        top_rated_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movie_data.extend(fetch_movie_data(popular_url, i))
        movie_data.extend(fetch_movie_data(top_rated_url, i))

    actor_data = fetch_credit_data(movie_data)
    
    # save_to_file("genre", genre_data)
    save_to_file("movies", movie_data)
    # save_to_file("actors", actor_data)


if __name__ == "__main__":
    main()