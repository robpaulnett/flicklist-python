import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # list of movies to select from
        movies = ("The Big Lebowski", "Hero", "Training Day", "Pee-Wee's Big Adventure", "Ray")

        # randomly choose one of the movies


        return random.choice(movies)

    def get(self):
        movie = self.getRandomMovie()
        tomorrow_movie = self.getRandomMovie()
        while movie == tomorrow_movie:
            tomorrow_movie == self.getRandomMovie()
        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"
        response += "<h1>Tomorrow's Movie</h1>"
        response += "<p>" + tomorrow_movie + "</p>"
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
