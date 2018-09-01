from pyramid.response import Response
from pyramid.view import forbidden_view_config, notfound_view_config


@forbidden_view_config()
def forbidden(request):
    """ Return a message to the user if they hit a forbidden endpoint
    """
    return Response(json_body={'message': 'Forbidden Request'}, status=403)


@notfound_view_config()
def not_found(request):
    """ Return a message to the user if they hit an unknown endpoint
    """
    return Response(json_body={'message': 'Not Found'}, status=404)
