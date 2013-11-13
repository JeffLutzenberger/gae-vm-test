import os
import datetime
import json
import webapp2
import jinja2
import logging

from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import background_thread

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


def f():
    x = 1.0
    for i in range(100000):
        x = x / float(i)
        if i % 1000:
            logging.info(x)


class BackendTest(webapp2.RequestHandler):
    """
    Demonstrates a really long running task (>10 min)
    """
    def get(self):
        t = background_thread.BackgroundThread(target=f, args=None)
        t.start()

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/backend-test', BackendTest), ], debug=True)