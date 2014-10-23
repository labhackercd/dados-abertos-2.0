# -*- coding: utf-8 -*-
import os
from pyjavaproperties import Properties

class PackageConfiguration:

    def __init__(self):
        
		# Lend o arquivo de configurações de um determinado pacote a 
		self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/package.properties"

		# Lendo o arquivo de configuraões no caminho a ser modificado conforme o caminho acima
		self.PROPERTIES = Properties()
		self.PROPERTIES.load(open(self.CONFIG_FILE))

	
		# Dicionário de Dados para Criação/Update dos Pacotes
		self.PACKAGE_DICT= {
			'author': self.PROPERTIES['AUTHOR'],
		    'name':  self.PROPERTIES['NAME'],
		    'notes': self.PROPERTIES['NOTES'],
		    'version': self.PROPERTIES['VERSION']
		}
