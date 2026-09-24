import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"},
        "rating": 8.6, 
        "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"},
        "rating": 7.1, 
        "duration_min": 98, 
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"},
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"},
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"},
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"},
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"},
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"},
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"},
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"},
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# Этап 1
def average_rating(movies):
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    old_movie = max(ages)
    new_movie = min(ages)
    average_movie = math.ceil(sum(ages) / len(ages))

    return (old_movie, new_movie, average_movie)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60

    return f"{hours}ч {mins}м"


# Этап 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015 and year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3
def not_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def find_first_best(movies):
    i = 0

    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break

        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


# Этап 4
def normalize_title(title):
    words = title.split()
    res = []

    for word in words:
        res.append(word[0].upper() + word[1:])

    return " ".join(res)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])

    return (f'"{title}" ({movie["year"]}) - {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}")


# Этап 5
def titles_sorted_by_rating(movies):
    sort_movies = sorted(movies,
        key=lambda movie: movie["rating"],
        reverse=True)

    titles = []

    for movie in sort_movies:
        titles.append(movie["title"])

    return titles


def top_n_by_rating(movies, n=3):
    sort_movies = sorted(movies,
        key=lambda movie: movie["rating"],
        reverse=True)

    res = []

    for movie in sort_movies[:n]:
        res.append((movie["title"], movie["rating"]))

    return res


# Этап 6
def count_by_genre(movies):
    genre_count = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1

    return genre_count


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography


def upper_average_ratings(movies):
    average = average_rating(movies)

    return {movie["title"]: movie["rating"]
            for movie in movies
            if movie["rating"] > average}


# Этап 7
def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b


# Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_high_rated_duration(movies):
    return sum(movie["duration_min"]
               for movie in movies
               if movie["rating"] > 7)


def high_rated_movies(movies):
    res = []

    for movie in iter_high_rated(movies):
        res.append(format_report_line(movie))

    return res


# Этап 9
def build_report(movies):
    average = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)

    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()

    print("Топ-3 фильма:")
    top_movies = sorted(movies,
        key=lambda movie: movie["rating"],
        reverse=True)[:3]

    for movie in top_movies:
        print(f" {format_report_line(movie)}")

    print()

    print("Фильмов по жанрам:")
    genre_count = count_by_genre(movies)
    sorted_genres = sorted(genre_count.items(),
        key=lambda item: item[1],
        reverse=True)

    for genre, count in sorted_genres:
        print(f" {genre} - {count}")

    print()

    genres = sorted(all_genres(movies))
    print(f'Все жанры каталога: {", ".join(genres)}')


if __name__ == "__main__":
    build_report(movies)