# Fresh Tomatoes Movie Trailers

## What is it?

A script that generates a webpage displaying information about movies based on data objects fed into it.

## How to use

Run the `fresh_tomatoes.py` script. A file called `fresh_tomatoes.html` will be created in the same directory. By default, `fresh_tomatoes.html` will be populated with information about my favorite movies. You can add or modify movie information by editing `entertainment_center.py`. Re-rynnung `fresh_tomatoes.py` will overwrite `fresh_tomatoes.html`.

## Differences from original project

- Upon first viewing the page, only the movies' posters are presented. Hovering over a movie poster will reveal more information about that movie (title, year of release, and synopsis).
- Modifications made to the HTML generated for each movie tile, mostly to accomodate flipping effect when a user hovers their mouse over a poster.
- Slight modifications made to JavaScript to accomodate changes to HTML mentioned above.

# Browser support

At present, the page displays properly in the following browsers:

- Firefox 31+
- Chrome 31+
- Safari 7+
- Opera 27+
- Android Browser 4.1+

The page does NOT display properly in IE.

# Thanks

- [David Walsh](http://davidwalsh.name) for CSS3 code used to create the flipping effect used on movie posters.
