from pyramid_restful.routers import ViewSetRouter
# from .views.stocks import StocksAPIView
from .views.portfolio import PortfolioAPIView
from .views.portfolio import StockAPIView
from .views.portfolio import CompanyAPIView
# from .views.company import CompanyAPIViewset
from .views.auth import AuthAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', '/api/v1/lookup/{symbol}')

    router = ViewSetRouter(config, trailing_slash=False)
    # router.register('api/v1/location', WeatherLocationAPIView, 'location')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
    router.register('api/v1/stocks', StockAPIView, 'stock portfolio')
    router.register('api/v1/portfolio', PortfolioAPIView, 'Portfolio view')
    router.register('api/v1/company', CompanyAPIView, 'Company view')

