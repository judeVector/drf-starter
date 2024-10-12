from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title
from api.serializers import UserPublicSerializer


class ProductLinlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )

    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    related_products = ProductLinlineSerializer(
        source="user.product_set.all", read_only=True, many=True
    )
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    # email = serializers.EmailField(source="user.email", read_only=True)
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            "owner",
            "url",
            "edit_url",
            "pk",
            "related_products",
            # "email",
            "title",
            "content",
            "price",
            "my_discount",
        ]

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

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
