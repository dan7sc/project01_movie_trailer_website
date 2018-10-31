# Styles and scripting for the page
main_page_head = '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="utf-8">
	    <title>Fresh Tomatoes!</title>

	    <!-- Bootstrap 4 -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>

	    <link rel="stylesheet" href="./styles/style.css">
	    <script src="./scripts/script.js"></script>
	</head>
'''


main_page_styles = '''
    body {
        padding-top: 80px;
    }
    #trailer .modal-dialog {
        margin-top: 200px;
        width: 640px;
        height: 480px;
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
    .movie-tile {
        margin-bottom: 20px;
        padding-top: 20px;
    }
    .movie-tile:hover {
        background-color: #EEE;
        cursor: pointer;
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
'''

main_page_scripts = '''
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '#play-trailer', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
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

        $("#info-container #title").empty().html("<i><b>" + title + "</b> (" + released + ")</i>");
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
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
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
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
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
		  <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
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
'''


# A single movie entry html template
movie_card_content = '''
<div class="anime col-sm-6 col-md-4 col-lg-3 text-center">
    <div class="card">
      <img class="card-img-top" src="{poster_image_url}" width=220 height=342>
        <div class="card-body">
            <div class="card-title">
                <h4>{movie_title}</h4>
                <div class="card-option">
                    <a id="play-trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Trailer</a>
                </div>
                <div class="card-option">
                    <a id="info-data" data-toggle="modal" data-target="#info" data-title="{movie_title}" data-storyline="{movie_storyline}" data-released="{movie_released}" data-runtime="{movie_runtime}" data-genre="{movie_genre}" data-director="{movie_director}" data-rated="{movie_rated}" data-rating="{movie_rating}">Info</a>
                </div>
            </div>
        </div>
    </div>
</div>
'''
