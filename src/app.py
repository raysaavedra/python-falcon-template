import falcon

from falcon_cors import CORS

import src.conf as settings
from .middleware.permissions import APIPermission
from .core.routes import (
    api_routes,
    register_routes
)

def create_app():
    cors = CORS(allow_origins_list=settings.ALLOWED_HOSTS)

    middlewares = [
        cors.middleware,
        APIPermission(),
    ]

    app = falcon.API(middleware=middlewares)

    register_routes(api_routes, app, prefix='api/v1')

    return app

app = application = create_app()
