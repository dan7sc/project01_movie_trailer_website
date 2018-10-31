import re
import page_content


def create_movie_cards_content(movies):
    """
    Description: Create content about movies
    Parameter: a instance of the class Movie
    Return: string content
    """

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += page_content.movie_card_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_released=movie.released,
            movie_runtime=movie.runtime,
            movie_genre=movie.genre,
            movie_director=movie.director,
            movie_rated=movie.rated,
            movie_rating=movie.rating,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content
