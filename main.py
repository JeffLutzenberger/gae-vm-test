import os
import webapp2
import jinja2
import logging

from google.appengine.api import background_thread

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


def f():
    for i in range(100000):
        x = 3.14159 / float(i + 1)
        if i % 10000 == 0:
            logging.info(x)


class MainPage(webapp2.RequestHandler):
    """
    Demonstrates how to use templates, we're using jinja
    """
    def get(self):
        templ = jinja_environment.get_template("templates/main_page.html")
        self.response.out.write(templ.render({'dict_key': ''}))


class BackendTest(webapp2.RequestHandler):
    """
    Demonstrates a really long running task (>10 min)
    """
    def get(self):
        t = background_thread.BackgroundThread(target=f, args=[])
        t.start()

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/backend-test', BackendTest), ], debug=True)
