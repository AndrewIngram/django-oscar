from soaplib.server.wsgi import Application
from django.http import HttpResponse

class DjangoSoapApplication(Application):

    def __call__(self, request):
        django_response = HttpResponse()
        def start_response(status, headers):
            status = status.split(' ', 1)[0]
            django_response.status_code = int(status)
            for header, value in headers:
                django_response[header] = value
        response = super(DjangoSoapApplication, self).__call__(request.META, start_response)
        django_response.content = "\n".join(response)

        return django_response