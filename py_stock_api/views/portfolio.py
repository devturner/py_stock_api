from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):
    def list(self, request):
        """ List all the portfolios
        """
        return Response(json={'message': 'Listing all portfolios'}, status=200)

    def retrieve(self, request):
        """ Get one of their portfolios
        """
        return Response(json={'message': 'Get one portfolio'}, status=200)

    def create(self, request):
        """ Creat a new portfolio
        """
        return Response(json={'message': 'Created a new portfolio'}, status=201)

    def destroy(self, request):
        """ Delete a portfolio from the list
        """
        return Response(json={'message': 'Deleted the portfolio'}, status=204)
