from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^$', 'oscar.apps.api.soap.views.service'),
    (r'^service.wsdl$', 'oscar.apps.api.soap.views.service'),
)