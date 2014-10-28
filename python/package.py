#!/usr/bin/env python
# -*- coding: utf-8 -*-
from request import Request


class Package:

    def __init__(self):
        self.request = Request()


    # Função que retorna uma Lista de Pacotes
    def list_package(self):
        
        # Url da Requisição
        url_request = "current_package_list_with_resources"
        
        # Parametros da Requisição (Para essa requisição não há nenhum parametro, logo o dicionário vai vazio
        return self.request.do_Request(url_request, params_request={})


    def create_or_update_package(self, package_configuration):
        

        # Consultando a Lista de Pacotes  
        package_list_response = self.list_package()
        
        # Criando um dicionário com os Pacotes
        package_list_dict = package_list_response.result

       
        # Verificando se o pacote será atualizado ou criado
        for package in package_list_dict:

            # Se o pacote já existir, obté-se a URL de Update e o id daquele pacote no CKAN
            if package['name'] == package_configuration.PACKAGE_DICT['name']:
                package_url = 'package_update'
                return self.request.do_Request(package_url, package_configuration.PACKAGE_DICT)
     
            else:
                package_url = 'package_create'
                return self.request.do_Request(package_url, package_configuration.PACKAGE_DICT)
                   
