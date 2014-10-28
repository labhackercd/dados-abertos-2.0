#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from package_configuration import PackageConfiguration
from package import Package



# Função que procura os arquivos de rercurso em um diretorio

def files_path(directory):
  file_paths = []
  for root, directories, files in os.walk(directory):
       for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Adicionando a Listas

  return file_paths



def main():

	for path in files_path(os.path.dirname(os.path.realpath(__file__))+"/config/packages/"):
		
		# Criando a configuração dos pacotes
		package_configuration = PackageConfiguration(path)
		
		# Criando uma instância de um pacote
		package = Package()

		# Resposta da Criação de um determinado pacote
		response = package.create_or_update_package(package_configuration)
		
		# Obtendo o id do Pacote no CKAN
		package_id = response.result['id']
		print package_id
	
	

if __name__ == "__main__":
    main()




# res_dict = {
#     'package_id': package_id,
#     'name': 'Proposições Legislativas de 2014',
#     'description': 'A long description of my resource!',
#     'format':'CSV'
# }

# res_url = '{URL_BASE}/action/resource_create'.format(URL_BASE=URL_BASE)


# f = [('upload', file('pathToMyFile'))]

# r = requests.post(res_url, data=res_dict, headers=auth, files=f)

