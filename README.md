A couple notes:

You can find your user agent here: 
http://www.whoishostingthis.com/tools/user-agent/

For your directory path, be sure to use \\ for each 
single backslash in the path string. For example, 
"C:\user..." becomes "C:\\user..."

This loveliness is written in Python 3.6 so #input, 
literal string interpolation, and the urllib module 
will be different for earlier versions of Python. 

// A bit a background (if you're interested)...
I somehow got it in my head that my second project 
should be to create a program that would download 
the nth image in a Google Images search. I'm totally
new to this proogramming thing and it seemed pretty 
straightforward. Little did I know.

The Wild West of web scraping is a lot crazier than
I imagined. A full day was wasted as I tried to make 
Selenium happen. (Selenium did not happen.) Another
day was devoted to hunting for APIs. Nothing seemed 
to fit.

A thousand thank yous to Charles and rishabhr0y for 
finally getting me on the right track. My code is
mostly based on their code here:
https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search#answer-28487500

Also, BeautifulSoup, I love you.

Please enjoy, suggest changes, etc.

~ Mariel