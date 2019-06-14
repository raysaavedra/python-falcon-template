import falcon

from src.core.resource import BaseResource


class TestResourceView(BaseResource):

    def on_get(self, req, resp):
        self.ok(resp, {'message': 'here on get'})
