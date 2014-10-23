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
        return self.request.do_Request(url_request, params_request={});

	# Função que atualiza ou cria um novo pacote de dados
	# Params Nome do Pacote
	def verify_package(self, package_configuration):

		package_list_response = self.package_list()

		package_list_dict = package_list_response.result

		# Verificando se o pacote será atualizado ou criado
		for package in package_list_dict:

			# Se o pacote já exitir, obté-se a URL de Update e o id daquele pacote no CKAN
			if package['name'] == package_configuration['NAME']:
				package_url = 'action/package_update'
				#package_update(package_url)

			else:
				package_url = '/action/package_create'
				package_create(package_url, package_configuration)




	def create_package(self, package_url, params_request):
		  return self.request.do_Request(url_request, params_request={});