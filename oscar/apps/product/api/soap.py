from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.model.primitive import String, Integer
from soaplib.model.clazz import ClassSerializer, Array

import logging

class Product(ClassSerializer):
    __namespace__ = 'product'
    upc = String
    brand = String
    subbrand = String
    title = String
    classification = String
    primary_category = String
    secondary_category = String
    
class ProductManager(DefinitionBase):    
    def _create_product(self, data):
        logging.info('Adding product: %s' % str(data))
    
    @rpc(Array(Product), _returns=Array(Integer))
    def add_products(self, products):
        for p in products:
            self._create_product(p)