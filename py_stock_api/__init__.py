from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS


class RootACL:
    __acl__ = [
        (Allow, 'admin', ALL_PERMISSIONS),
        (Allow, 'view', ['read']),
    ]

    def __init__(self, request):
        pass


def add_role_principles(userid, request):
    return request.jwt_claims.get('roles', [])

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('pyramid_jwt')
    #acl (access control list)

    config.set_root_factory(RootACL)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(
        'superseekrit',  # os.environ.get('SECRET')
        auth_type='Bearer',
        callback=add_role_principles,
    )

    config.include('pyramid_restful')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
