from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/

        # Use the `id` to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )


    # Just an example
    # def list(self, request):
    #     # http :6543/api/v1/company/
    #     pass
