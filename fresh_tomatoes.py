import webbrowser
import os
import re
import page_content
import cards


def open_movie_cards_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = page_content.main_page_content.format(
        movie_cards=cards.create_movie_cards_content(movies))

    main_page_head = page_content.main_page_head + page_content.main_page_styles + page_content.main_page_scripts
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
