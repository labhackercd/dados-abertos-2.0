#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pyjavaproperties import Properties

class SetupConfiguration:

    def __init__(self):
        
       
		self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/myconfig.properties"

		# Lendo o arquivo de configuraões no caminho a ser modificado conforme o caminho acima
		self.PROPERTIES = Properties()
		self.PROPERTIES.load(open(self.CONFIG_FILE))


		# Lendo Qual ambiente deve ser utilizado: Homologação ou Test
		self.ENV = self.PROPERTIES['ENV']

		# URL_AMBIENTE
		self.URL_BASE = self.PROPERTIES[self.ENV]

		# Lendo a Chave Privada do Arquivo de Configurações
		self.AUTH = self.PROPERTIES['AUTH']


		# Arquivo dos Recursos
		self.PATH_OF_FILES = self.PROPERTIES['PATH_OF_FILES']

		
		# Lend o arquivo de configurações de um determinado pacote a 
		self.PACKAGE_CONFIG = os.path.dirname(os.path.realpath(__file__))+"/package.properties"