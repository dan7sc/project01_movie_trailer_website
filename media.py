import webbrowser


class Movie():
    """Class for movie information"""
    def __init__(self, movie_title, movie_storyline,
                 movie_released, movie_runtime,
                 movie_genre, movie_director,
                 movie_rated, movie_rating,
                 poster_image, trailer_youtube):
        """Constructor"""
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
        """Show movie trailer in youtube"""
        webbrowser.open(self.trailer_youtube_url)
