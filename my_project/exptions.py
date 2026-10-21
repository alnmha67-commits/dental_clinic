from django.http import Http404
class appointmentteked(Exception):
    pass
class patent_not_found(Exception):
    pass
class patent_exsist(Http404):
    pass