from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    """
    Custom Authentication adding the keyword Bearer
    """

    keyword = "Bearer"
