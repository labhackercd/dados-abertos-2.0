# -*- coding: utf-8 -*-
import os
from pyjavaproperties import Properties

class PackageConfiguration:

    def __init__(self, file_path):
        
        # Lend o arquivo de configurações de um determinado pacote a ser lido
        self.CONFIG_FILE = file_path

        # Lendo o arquivo de configuraões no caminho a ser modificado conforme o caminho acima
        self.PROPERTIES = Properties()
        self.PROPERTIES.load(open(self.CONFIG_FILE))

    
        # Dicionário de Dados para Criação/Update dos Pacotes
        self.PACKAGE_DICT= {
            'author': self.PROPERTIES['AUTHOR'],
            'name':  self.PROPERTIES['NAME'],
            'title':  self.PROPERTIES['TITLE'],
            'notes': self.PROPERTIES['NOTES'],
            'version': self.PROPERTIES['VERSION']
        }



        # Arquivo dos Recursos
        self.PATH_OF_FILES = self.PROPERTIES['PATH_OF_FILES']

