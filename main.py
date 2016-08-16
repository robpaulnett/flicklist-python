import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.

        crossOff_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross-off
                <input type="text" name="watched-movie" />
                from my watchlist.
            </label>
            <input type="submit" value="remove-it" />
        </form>
        """
        # try delete list as a dropdown instead
        # <select>
        #   <option value="volvo">Volvo</option>
        #   <option value="saab">Saab</option>
        #   <option value="mercedes">Mercedes</option>
        #   <option value="audi">Audi</option>
        # </select>

        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)


        response = page_header + edit_header + add_form + crossOff_form + page_footer
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
    """ Handles request coming into /cross-off
        e.g. www.flicklist.com/cross-off
    """
    def post(self):
        # look inside the request to figure out what the user typed
        watched_movie = self.request.get("watched-movie")

        # build response content
        watched_movie_element = "<strong>" + watched_movie + "</strong>"
        sentence = "<strike>" + watched_movie_element + "</strike>" + " has been crossed off your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)
], debug=True)
