import media
import requests
import fresh_tomatoes

api_key = "ee5ec991a3f24dcfa6353abd3c234966"

def request_movie_id(query):
    r = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" + api_key +
                        "&query=" + query)
    return r.json()["results"][0]["id"]

def get_movie_data(name):
    id = str(request_movie_id(name))
    details = requests.get("https://api.themoviedb.org/3/movie/" + id +
                        "?api_key=" + api_key +
                        "&language=en-US").json()
    image_path = "https://image.tmdb.org/t/p/w1280"

    videos = requests.get("https://api.themoviedb.org/3/movie/" + id +
                          "/videos?api_key=" + api_key +
                          "&language=en-US").json()
    video_path = "https://youtu.be/"

    for i in videos["results"]:
        if (i["type"] == "Trailer"):
            trailer = i["key"]
            break

    return {
        'title': details["title"],
        'storyline' : details["overview"],
        'poster' : image_path + details["poster_path"],
        'trailer' : video_path + trailer}

def create_movie(name):
    data = get_movie_data(name)

    return media.Movie(data["title"],
                       data["storyline"],
                       data["poster"],
                       data["trailer"])


interstellar = create_movie("Interstellar")
spider_man_homecoming = create_movie("Spider Man: Homecoming")
gotg_vol_2 = create_movie("Guardians of the Galaxy Vol. 2")
heathers = create_movie("Heathers")
star_wars_tlj = create_movie("Star Wars: The Last Jedi")
bh6 = create_movie("Big Hero 6")

movies = [interstellar, spider_man_homecoming, gotg_vol_2, heathers, star_wars_tlj, bh6]
fresh_tomatoes.open_movies_page(movies)


