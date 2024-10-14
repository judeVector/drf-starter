from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    # related_products = ProductLinlineSerializer(
    #     #     source="user.product_set.all", read_only=True, many=True
    #     # )

    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title]
    )
    body = serializers.CharField(source="content")

    class Meta:
        model = Product
        fields = [
            "owner",
            "pk",
            "title",
            "body",
            "price",
            "public",
            "path",
            "endpoint",
        ]

    def get_my_user_data(self, obj):
        return {"username": obj.user.username}

    def get_edit_url(self, obj):
        request = self.context.get("request")  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # This can alslo be writtenn here or moved to a special file for more cleanliness
    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists as a product")
    #     return value
