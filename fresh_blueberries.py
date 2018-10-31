import webbrowser
import os
import re
import page_content
import cards


def open_movie_cards_page(movies):
    """
    Description: Open a browser to show movies content
    Parameter: a instance of the class Movie
    Return: Nothing
    """

    # Create or overwrite the output file
    index_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = page_content.main_page_content.format(
        movie_cards=cards.create_movie_cards_content(movies))

    # Write the content in index.html file and close it
    index_file.write(page_content.main_page_head + rendered_content)
    index_file.close()

    # Create directory styles and a css file
    create_dir_file('styles', 'style.css')
    style_file = open('./styles/style.css', 'w')
    style_file.write(page_content.main_page_styles)
    style_file.close()

    # Create directory scripts and a js file
    create_dir_file('scripts', 'script.js')
    script_file = open('./scripts/script.js', 'w')
    script_file.write(page_content.main_page_scripts)
    script_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(index_file.name)
    webbrowser.open('file://' + url, new=2)


def create_dir_file(dir, file):
    """
    Description: Create a directory and a file within this
    Parameter: a diretory name, a file name
    Return: Nothing
    """
    if os.path.exists(dir):
        if os.path.exists(dir + '/' + file):
            os.remove(dir + '/' + file)
        os.rmdir(dir)
    os.makedirs(dir)
