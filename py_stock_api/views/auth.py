from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json




class AuthAPIView(APIViewSet):
    """ create the auth endpoints
        make new accounts
        verify a user
    """
    def create(self, request, auth=None):
        data = json.loads(request.body.decode())

        if auth == 'register':
            try:
                account = Account.new(
                    request,
                    email=data['email'],
                    password=data['password'])
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            # TODO: Refactor this for authentication / JSON Web Token tomorrow
            return Response(json='Created', status=201)

        if auth == 'login':
            # TODO: Implement this for login features tomorrow
            pass

        return Response(json='Not Found', status=404)
