from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import views


if __name__ == "__main__":
    config = Configurator()

    config.add_route('hello', '/')
    config.add_route('about', '/about')
    config.add_route('contact_page', '/contact')
    config.scan(views)

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
