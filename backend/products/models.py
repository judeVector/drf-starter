import random

from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ["electronics", "cars", "boats", "movies", "cameras"]


class ProductQuerySet(models.QuerySet):
    def is_publc(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        queryset = self.is_publc().filter(lookup)
        if user is not None:
            second_queryset = queryset.filter(user=user).filter(lookup)
            queryset = (queryset | second_queryset).distinct()
        return queryset


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(max_length=120, null=False)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def body(self):
        return self.content

    @property
    def path(self):
        return f"/products/{self.pk}/"

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    def is_public(self) -> bool:
        return self.public  # True or False

    def get_discount(self):
        return "122"

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
