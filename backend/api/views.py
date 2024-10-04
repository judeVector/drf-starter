from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
