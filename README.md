# Fresh Tomatoes Movie Trailers

## What is it?

A script that generates a webpage displaying information about movies based on data objects fed into it.

## How to use

Run the `entertainment_center.py` script. A file called `fresh_tomatoes.html` will be created in the same directory. That HTML file will display movie information specified in `entertainment_center.py`.

By default, `entertainment_center.py` will be populated with information about my favorite movies. You can add or modify movie information by editing `entertainment_center.py`. Re-running `entertainment_center.py` will overwrite `fresh_tomatoes.html`.

### Tip: Running a Python script

The easiest way to run a Python script is to open the file in the IDLE Python IDE and press F5 (or, click on "Run" in the menu bar, then select "Run Module").

Alternatively, you can open a terminal window (or a command line window if you're running Windows) and enter the following command:

`python entertainment_center.py`

Ensure your working directory is set to the directory containing the files `entertainment_center.py`, `fresh_tomatoes.py`, and `media.py`.

## Differences from original project

- Upon first viewing the page, only the movies' posters are presented. Hovering over a movie poster will reveal more information about that movie (title, year of release, and synopsis).
- Modifications made to the HTML generated for each movie tile, mostly to accomodate flipping effect when a user hovers their mouse over a poster.
- Slight modifications made to JavaScript to accomodate changes to HTML mentioned above.

## Browser support

At present, the page displays properly in the following browsers:

- Firefox 31+
- Chrome 31+
- Safari 7+
- Opera 27+
- Android Browser 4.1+

The page does NOT display properly in IE.

## Thanks

- [David Walsh](http://davidwalsh.name) for CSS3 code used to create the flipping effect used on movie posters.
