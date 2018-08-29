from ..models.schemas import PortfolioSchema
from ..models.schemas import StockSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
from ..models import Portfolio
from ..models import Stock
import requests
import json


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """ Lookup a stock by the symbol
    """
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(
        request.matchdict['symbol']
    )
    # time_url = 'https://api.iextrading.com/1.0/stock/{}}/time-series'.format(
    #     request.matchdict['time']
    # )
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class PortfolioAPIView(APIViewSet):
    def create(self, request):
        """ Creat a new portfolio
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(e.msg, status=400)

        if 'portfolio_name' not in kwargs:
            return Response(json='Expected value; portfolio name', status=400)
        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate key Error. Portfolio already exsists', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)

    def list(self, request):
        """ List all the portfolios
        """
        return Response(json='Listing all portfolios', status=200)

    def retrieve(self, request, id=None):
        """ Get one of their portfolios
        """
        return Response(json='Get one portfolio', status=200)

    def destroy(self, request, id=None):
        """ Delete a portfolio from the list
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            Portfolio.remove(request=request, pk=id)

            return Response(status=204)
        except (DataError, AttributeError):
            return Response(json='Not found', status=404)

        return Response(status=204)


class StockAPIView(APIViewSet):
    def retrieve(self, request):
        """ Get one of their stocks
        """
        return Response(json={'message': 'Get one stock from portfollio'}, status=200)

    def list(self, request):
        """ List all the stocks
        """
        return Response(json={'message': 'listing all stocks in portfollio'}, status=200)

    def create(self, request):
        """ Creat a new stock record
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value; stock symbol', status=400)
        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate key Error. Stock already exists', status=409)

        schema = StockSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

    def destroy(self, request):
        """ Delete a stock from the user
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            Stock.remove(request=request, pk=id)

            return Response(status=204)
        except (DataError, AttributeError):
            return Response(json='Not found', status=404)

        return Response(status=204)


# these are not working
class CompanyAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """get one of the companies
        """
        # http :6543/api/v1/company/{id}/

        # Use the `id` to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )

