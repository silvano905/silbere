from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2  # show two post per page
    max_limit = 10
