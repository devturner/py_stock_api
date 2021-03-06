from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """ This takes a request and returns a message.
        request is not used at the moment
    """
    message = 'Hello World!'
    return Response(body=message, status=200)
