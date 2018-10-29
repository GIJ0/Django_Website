<!DOCTYPE html>
<html>
  <head>
  	<?php
  	$characterName = ($_GET["character"]);
  	?>
	   <meta charset="utf-8">
	   

          <link rel="stylesheet" href="styles.css">
  </head>
    <header>
       <a src="Test" href="\index.html">N D 7.💣R G </a>
       <div class="topnav">
  <a class="active" href="\index.html">Home</a>
  <a href="#COTW">COMBOS OF THE WEEK</a>
  <a href="#GOATC">GOAT COMBOS</a>
  <a href="\submitpage.php"> SUBMIT A COMBO</a>

</div>
    </header>

      <body>
      <p1><?php echo $characterName; ?><p1>
        <main>
          <button>
            back
          </button>
            <iframe src="https://clips.twitch.tv/embed?autoplay=false&clip=BovineBrainyKiwiKappaClaus&tt_content=embed&tt_medium=clips_embed" width="640" height="360" frameborder="0" scrolling="no" allowfullscreen="true"></iframe>
            <button>
              Forwards
            </button>
        </main>
      </body>
    <footer>
      <div class="stars">
        <form action"">
          <input class="star star-5" id="star-5" type="radio" name="star" />
          <label class="star star-5" for="star-5"></label>
          <input class="star star-4" id="star-4" type="radio" name="star"/>
          <label class="star star-4" for="star-4"></label>
          <input class="star star-3" id="star-3" type="radio" name="star"/>
          <label class="star star-3" for="star-3"></label>
          <input class="star star-2" id="star-2" type="radio" name="star"/>
          <label class="star star-2" for="star-2"></label>
          <input class="star star-1" id="star-1" type="radio" name="star"/>
          <label class="star star-1" for="star-1"></label>
        </form>
      </div>





    </footer>

    <html>
    <!--https://www.cssscript.com/simple-5-star-rating-system-with-css-and-html-radios/
    https://css-tricks.com/centering-css-complete-guide/
    looking for a way to use the mario stars for the rating system...good progress so far
    move CSS to a seperate stlye sheet to see if we can get that faster load time!-->
