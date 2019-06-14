import json
import falcon


class BaseResource(object):
    
    def __init__(self):
        self.SUCCESS = falcon.HTTP_200
        self.BAD_REQUEST = falcon.HTTP_BAD_REQUEST
        self.INTERNAL_ERROR = falcon.HTTP_500
        self.NOT_FOUND = falcon.HTTP_404
        self.content_type = 'application/json'

    def ok(self, resp, message):
        resp.status = self.SUCCESS
        resp.content_type = 'application/json'
        resp.body = json.dumps(message)

    def error(self, resp, code, message):
        resp.status = code
        resp.content_type = 'application/json'
        resp.body = json.dumps(message)

