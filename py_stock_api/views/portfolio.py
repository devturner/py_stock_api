from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response

import json

@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    url = ''


class PortfolioAPIView(APIViewSet):
    def create(self, request):
        """ Creat a new portfolio
        """
        try:
            kwargs = json.loads(request.body)
        except json>JSONDecodeError as e:
            return Response(e.msg, status=400)

        if 'portfolio_name' not in kwargs:
            return Response(json='Expected value; portfolio name', status=400)
        try:
            # create the new portfolio

        except IntegrityError:
            return Response(json='Duplicate key Error. Portfolio already exsists' status=409)


        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)

    def list(self, request):
        """ List all the portfolios
        """
        return Response(json={'message': 'Listing all portfolios'}, status=200)

    def retrieve(self, request, id=None):
        """ Get one of their portfolios
        """
        return Response(json={'message': 'Get one portfolio'}, status=200)

    def destroy(self, request, , id=None):
        """ Delete a portfolio from the list
        """
        if not id:
            return Response(json={json: 'Not Found'}, status=404)

        try:
            Portfolio.remove(request=request, pk=id)

            return Response(status=204)
        except (DataError, AttributeError):
            return Responce(json='Not found' status=404)

        return Response(status=204)


def StockAPIView(APIViewSet):
    pass

def CompanyAPIView(APIViewSet):
    pass
