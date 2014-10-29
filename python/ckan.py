#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from package import Package
from resource import Resource
from package_configuration import PackageConfiguration
from resource_configuration import ResourceConfiguration




# Função que procura os arquivos de rercurso em um diretorio

def files_path(directory):
  file_paths = []
  for root, directories, files in os.walk(directory):
       for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Adicionando a Listas

  return file_paths



def main():

	for package_path in files_path(os.path.dirname(os.path.realpath(__file__))+"/config/packages/"):
		
		# Criando a configuração dos pacotes
		package_configuration = PackageConfiguration(package_path)
		
		# Criando uma instância de um pacote
		package = Package()

		# Resposta da Criação de um determinado pacote
		response = package.create_or_update_package(package_configuration)
		
		# Obtendo o id do Pacote no CKAN
		package_id = response.result['id']


		# Para arquvivo de configurações de recurso
		for file_path in files_path(package_configuration.PATH_OF_FILES):

			# Criando a configuração de um recurso
			resource_configuration = ResourceConfiguration(package_id, file_path)

			# Criando o recurso
			resource = Resource()

			# Obtendo a resposta do Recurso
			response = resource.create_or_update_resource(resource_configuration)
			
			# Obtendo o resultado
			#print response
	

if __name__ == "__main__":
    main()


