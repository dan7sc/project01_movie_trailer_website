"""
Create instances of the class Movie,
add this instance to a list and
call a function to open a webbrowser
and display the information about the movies.
"""


import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "1995",
                        "81 min",
                        "Animation, Adventure, Comedy",
                        "John Lasseter",
                        "G",
                        "8.3/10 (imdbRating)",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "2009",
                     "162 min",
                     "Action, Adventure, Fantasy",
                     "James Cameron",
                     "PG-13",
                     "7.8/10 (imdbRating)",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                     "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                     "2013",
                     "108 min",
                     "Comedy, Music",
                     "Richard Linklater",
                     "PG-13",
                     "7.1/10 (imdbRating)",
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                     "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                     "2007",
                     "111 min",
                     "Animation, Adventure, Comedy",
                     "Brad Bird, Jan Pinkava(co-director)",
                     "G",
                     "8.0/10 (imdbRating)",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiancee's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                     "2011",
                     "94 min",
                     "Comedy, Fantasy, Romance",
                     "Woody Allen",
                     "PG-13",
                     "7.7/10 (imdbRating)",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                     "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                     "2012",
                     "142 min",
                     "Adventure, Sci-Fi, Thriller",
                     "Gary Ross",
                     "PG-13",
                     "7.2/10 (imdbRating)",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movie_cards_page(movies)
