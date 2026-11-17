from rest_framework.pagination import PageNumberPagination

class Pagination_Api(PageNumberPagination):
    page_size=4
    page_size_query_param="size"
    max_page_size=10