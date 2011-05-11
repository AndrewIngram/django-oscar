from oscar.apps.api.soap import DjangoSoapApplication
from soaplib.service import DefinitionBase
from django.conf import settings
from soaplib import Application
import inspect

definitions = []

for app in settings.INSTALLED_APPS:
    try:
        module = __import__(app + '.api.soap', [], [], [''])
        for key in module.__dict__:
            cls = module.__dict__[key]
            if inspect.isclass(cls) and issubclass(cls,DefinitionBase):
                definitions.append(cls)
    except ImportError, e:
        pass

service = DjangoSoapApplication(Application(definitions, 'tns'))