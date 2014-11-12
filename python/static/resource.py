#!/usr/bin/env python
# -*- coding: utf-8 -*-
from request import Request

class Resource:

     def __init__(self):
        self.request = Request()


     def create_or_update_resource(self, resource_configuration):

       
        # Verificando se o pacote será atualizado ou criado
        #for package in package_list_dict:

            # Se o pacote já existir, obté-se a URL de Update e o id daquele pacote no CKAN
            #if package['name'] == package_configuration.PACKAGE_DICT['name']:
                #resource_url = 'resource_update'
                #return self.request.do_Request(resource_url, resource_configuration.RESOURCE_DICT)
     
            #else:
    	resource_url = 'api/action/resource_create'
        return self.request.doResource_Request(resource_url, resource_configuration.RESOURCE_DICT, resource_configuration.FILE_PATH)