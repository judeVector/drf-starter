from rest_framework import generics, mixins, authentication


from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

from api.authentication import TokenAuthentication


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Using generics in class-based views
class ProductListCreateAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]

    def perform_create(self, serializer):
        email = serializer.validated_data.pop("email")
        # print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None

        if content is None:
            content = title
            serializer.save(user=self.request.user, content=content)

    # This will make authenticated users to only see their own post and not others
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)


# Using mixins and generics in class-based views
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None

        if content is None:
            content = title
            serializer.save(content=content)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
