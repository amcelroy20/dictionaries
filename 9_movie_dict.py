import random

movie_ratings = {"Shawshank Redemption": 9.5,
                 "The Room": 2,
                 "Jurassic Park": 9,
                 "Star Wars: A New Hope": 8.5,
                 "National Treasure": 6,
                 "Batman Begins": 8}

good_movie_list = []

for i in movie_ratings:
    if movie_ratings[i] >= 8:
        good_movie_list.append(i)
    else:
        next

random_movie = random.choice(good_movie_list)
movie_title = input('input movie title: ')

def recommend_movie(movie, rating):
    if movie in rating:
        if rating[movie] >= 8:
            print(f'{movie} is recommended!')
        else:
            print(f"Looks like {movie} isn't very good...")
            print(f"How about trying {random_movie} instead?")
    print('Movie not found...')
    print(f"How about trying {random_movie} instead?")

recommend_movie(movie_title, movie_ratings)