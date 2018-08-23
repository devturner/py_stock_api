from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    def list(self, request):
        """ List all the stocks
        """
        return Response(json={'message': 'listing all stocks in portfollio'}, status=200)

    def retrieve(self, request):
        """ Get one of their stocks
        """
        return Response(json={'message': 'Get one stock from portfollio'}, status=200)

    def create(self, request):
        """ Creat a new stock record
        """
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request):
        """ Delete a stock from the user
        """
        return Response(json={'message': 'Deleted the record'}, status=204)
