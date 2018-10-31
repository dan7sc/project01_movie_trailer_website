"""
A set of strings to store html content
"""

# Styles and scripting for the page
main_page_head = (
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Fresh Blueberries</title>

        <!-- Bootstrap 4 -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2'''
    + '''/css/bootstrap.min.css" '''
    + '''rel="stylesheet" integrity="sha384-Smlep5jCw/wG7hdkwQ'''
    + '''/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B"'''
    + '''crossorigin="anonymous">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1'''
    + '''/jquery.min.js" '''
    + '''integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" '''
    + '''crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/'''
    + '''js/bootstrap.min.js" '''
    + '''integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbH'''
    + '''FLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" '''
    + '''crossorigin="anonymous"></script>

        <link rel="stylesheet" href="./styles/style.css">
        <script src="./scripts/script.js"></script>
    </head>
    ''')


main_page_styles = (
    '''
    body {
        background-color: #202020;
        color: #aaa;
    }
    .navbar {
        background-color: #557;
        width: 100%;
        margin-bottom: 20px;
    }
    .navbar-header a {
        color: #113;
        font-weight: bold;
        font-style: italic;
    }
    #trailer .modal-dialog {
        margin-top: 100px;
        margin-right: auto;
        margin-left: auto;
        width: auto;
        height: auto;
    }
    #info .modal-dialog {
        top: 50px;
        border-width: 3px;
        border-style: inset;
        box-shadow: 5px 5px 20px #779;
    }
    .hanging-close {
        position: absolute;
        top: -12px;
        right: -12px;
        z-index: 9001;
    }
    #trailer-video {
        width: 100%;
        height: 100%;
    }
    .scale-media {
        padding-bottom: 56.25%;
        position: relative;
    }
    .scale-media iframe {
        border: none;
        height: 100%;
        position: absolute;
        width: 100%;
        left: 0;
        top: 0;
        background-color: white;
    }
    .card {
        border: none;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 15px;
        margin-bottom: 15px;
        position: relative;
        height: 342px;
        width: 220px;
        overflow: hidden;
        color: #ffffff;
    }
    .card-body {
        position: absolute;
        height: 150px;
        width: 220px;
        bottom: -150px;
        background: linear-gradient(180deg, '''
    + '''transparent 0, rgba(0, 0, 0, .8) 30%, #000);
    }
    @media only screen and (max-width: 580px) {
        .card-body {
            transform: translateY(-150px);
        }
    }
    .card:hover .card-body {
        transform: translateY(-150px);
    }
    .card-title h4 {
        text-shadow: 2px 2px 4px #999;
        color: white;
        padding-top: 20px;
    }
    .card-option a {
        font-weight: bold;
        font-size: 18px;
        color: lightblue;
        cursor: pointer;
    }
    .card-option:hover {
        font-weight: bold;
        color: yellow;
        text-decoration: none;
    }
    #info-data {
        padding-bottom: 40px;
    }
    #info-container {
        padding: 10px;
        background-color: #aad;
        font-size: 18px;
        color: #222;
    }
    #title {
        text-align: center;
        font-size: 24px;
    }
    #storyline {
        text-align: justify;
    }
    ''')

main_page_scripts = (
    '''
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, \
        .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself
        // gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '#play-trailer', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + \
            trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });
    // Show information about the movie whenever the info modal is opened
    $(document).on('click', '#info-data', function (event) {
        var title = $(this).attr('data-title');
        var storyline = $(this).attr('data-storyline');
        var released = $(this).attr('data-released');
        var runtime = $(this).attr('data-runtime');
        var genre = $(this).attr('data-genre');
        var director = $(this).attr('data-director');
        var rated = $(this).attr('data-rated');
        var rating = $(this).attr('data-rating');

        $("#info-container #title").empty().html("<i><b>" \
            + title + "</b> (" + released + ")</i>");
        $("#info-container #storyline").html("<i>&emsp;" + storyline + "</i>");
        $("#info-container #runtime").html("<b>Runtime: </b>" + runtime);
        $("#info-container #genre").html("<b>Genre: </b>" + genre);
        $("#info-container #director").html("<b>Director: </b>" + director);
        $("#info-container #rated").html("<b>Rated: </b>" + rated);
        $("#info-container #rating").html("<b>Rating: </b>" + rating);
    });
    // Animate in the movies when the page loads
    $(document).ready(function () {
      $('.anime').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
      });
    });
    ''')


# The main page layout and title bar
main_page_content = (
    '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal">
            <img src="https://lh5.ggpht.com/'''
    + '''v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_'''
    + '''qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Information Video Modal -->
    <div class="modal" id="info">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" '''
    + '''data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/'''
    + '''v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_'''
    + '''qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div id="info-container">
            <p id="title"></p>
            <p id="storyline"></p>
            <p id="genre"></p>
            <p id="director"></p>
            <p id="runtime"></p>
            <p id="rated"></p>
            <p id="rating"></p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="navbar navbar-expand" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Fresh Blueberries Movie Trailers</a>
        </div>
      </div>
    </div>

    <div class="container">
        <div class="row">
          {movie_cards}
        </div>
    </div>
  </body>
</html>
    ''')


# A single movie entry html template
movie_card_content = (
    '''
    <div class="anime col-sm-6 col-md-4 col-lg-3 text-center">
        <div class="card">
          <img class="card-img-top" '''
    + '''src="{poster_image_url}" width=220 height=342>
            <div class="card-body">
                <div class="card-title">
                    <h4>{movie_title}</h4>
                    <div class="card-option">
                        <a id="play-trailer" '''
    + '''data-trailer-youtube-id="{trailer_youtube_id}" '''
    + '''data-toggle="modal" data-target="#trailer">Trailer</a>
                    </div>
                    <div class="card-option">
                        <a id="info-data" data-toggle="modal" '''
    + '''data-target="#info" data-title="{movie_title}" '''
    + '''data-storyline="{movie_storyline}" '''
    + '''data-released="{movie_released}" '''
    + '''data-runtime="{movie_runtime}" '''
    + '''data-genre="{movie_genre}" '''
    + '''data-director="{movie_director}" '''
    + '''data-rated="{movie_rated}" '''
    + '''data-rating="{movie_rating}">Info</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    ''')
