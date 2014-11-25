# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'baufaker'

import os
import datetime
from pyjavaproperties import Properties


class API_Configuration:
     def __init__(self):

        # Lendo o arquivo de configuração do recurso CSV
        self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/api.properties"

        # Lendo o arquivo de configurações no caminho a ser modificado conforme o caminho acima
        self.PROPERTIES = Properties()
        self.PROPERTIES.load(open(self.CONFIG_FILE))

        # Montando o arquivo base da Base

        self.LIMIT_PAGE = int(self.PROPERTIES['LIMIT_PAGE'])


        self.BASE_URL = self.PROPERTIES['BASE_API'] + self.PROPERTIES['API_VERSION']