from src.modules.module1.routes import routes as module1_routes

api_routes = [
    module1_routes,
]

def register_routes(routes, app, prefix=None):
    for module in routes:
        for route in module:
            if prefix:
                app.add_route(f'/{prefix}/{route[0]}', route[1])
            else:
                app.add_route(f'/{route[0]}', route[1])