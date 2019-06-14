import falcon

import src.conf as settings


class APIPermission:
    '''
        This will handle all incoming requests.
        Incoming requests should include a header:
        Token - [secret key]
    '''

    def process_request(self, req, resp):
        token = req.headers.get('TOKEN', None)

        if token != settings.SECRET_KEY:
            raise falcon.HTTPUnauthorized()