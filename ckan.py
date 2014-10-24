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
           	# Costruindo o caminho completo
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Adicionando a Listas

  return file_paths



def main():

	package_configuration = PackageConfiguration()
	
	package = Package()

	response =  package.create_or_update_package(package_configuration)

	print response.result

	# Obtendo os arquivos de diretório de arquivos
	#files = files_path(configuration.PATH_OF_FILES)
	#print files


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

# if package_url != None:
#  	print package_url.get_full_url()
# # We'll use the package_create function to create a new dataset.
# request = urllib2.Request(
#     'http://dados-teste.camara.gov.br/api/action/package_update')

# assert response.code == 200
