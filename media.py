import webbrowser


class Movie():
    """
    Movie() Class builds a constructor that stores
    information about the movie and a method that
    displays the movie trailer
    """
    def __init__(self, movie_title, movie_storyline,
                 movie_released, movie_runtime,
                 movie_genre, movie_director,
                 movie_rated, movie_rating,
                 poster_image, trailer_youtube):
        """
        Constructor that initializes a movie with
        the following information: title, storyline,
        realeased, runtime, genre, director,
        rated, rating, poster image and
        youtube trailer

        :param movie_title: string
        :param movie_storyline: string
        :param movie_released: string
        :param movie_runtime: string
        :param movie_genre: string
        :param movie_director: string
        :param movie_rated: string
        :param movie_rating: string
        :param poster_image: string
        :param trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.released = movie_released
        self.runtime = movie_runtime
        self.genre = movie_genre
        self.director = movie_director
        self.rated = movie_rated
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Method that opens a web browser and
        displays youtube movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
