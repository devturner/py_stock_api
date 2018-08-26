from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView
from .views.portfolio import PortfolioAPIView
from .views.company import CompanyAPIViewset


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/stocks', StocksAPIView, 'stock portfolio')
    router.register('api/v1/portfolio', PortfolioAPIView, 'Portfolio view')
    router.register('api/v1/company', CompanyAPIViewset, 'Company view')

