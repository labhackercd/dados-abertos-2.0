#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pyjavaproperties import Properties

class SetupConfiguration:

    def __init__(self):
        
        
        # Lendo o arquivo de configuração
        self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/config/myconfig.properties"

        # Lendo o arquivo de configuraões no caminho a ser modificado conforme o caminho acima
        self.PROPERTIES = Properties()
        self.PROPERTIES.load(open(self.CONFIG_FILE))


        # Lendo Qual ambiente deve ser utilizado: Homologação ou Test
        self.ENV = self.PROPERTIES['ENV']

        # URL_AMBIENTE
        self.URL_BASE = self.PROPERTIES[self.ENV]

        # Lendo a Chave Privada do Arquivo de Configurações de acordo com o ambiente
        self.AUTH = self.PROPERTIES["AUTH_{ENV}".format(ENV=self.ENV)]