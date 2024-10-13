from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer

from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        if not query:
            return Response("", status=status.HTTP_400_BAD_REQUEST)
        results = client.perform_search(query)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        results = Product.objects.none()
        if query is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(query, user=user)
        return results
