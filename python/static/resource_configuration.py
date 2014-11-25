#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import magic
from pyjavaproperties import Properties

class ResourceConfiguration:

    def __init__(self, package_id, file_path):

        self.FILE_PATH = file_path.decode('utf-8')


        #Dicionário para Criação/Update dos Pacotes
        self.RESOURCE_DICT= {
            'package_id': package_id,
            'name':  os.path.basename(file_path), # Lendo o nome do arquivo
            'size' : os.path.getsize(file_path), # Lendo o tamanho do arquivo 
             'mimetype': magic.from_file(self.FILE_PATH, mime=True), # Lendo o mimetype do arquivo
            'format': os.path.splitext(file_path)[1].split('.')[1].upper() # Lendo a extensão do arquivo
        }
