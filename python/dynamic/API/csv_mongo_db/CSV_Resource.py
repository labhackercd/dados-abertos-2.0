# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'baufaker'
import os
import datetime
import csv
from pyjavaproperties import Properties


class CSVResource:

    def __init__(self):
        
        # Lendo o arquivo de configuração do recurso CSV
        self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/config/csv.properties"

        # Lendo o arquivo de configurações no caminho a ser modificado conforme o caminho acima
        self.PROPERTIES = Properties()
        self.PROPERTIES.load(open(self.CONFIG_FILE))

        # Lendo Qual ambiente deve ser utilizado: Homologação ou Test
        self.ENV = self.PROPERTIES['ENV']

        # Lendo o caminho do CSV
        self.PATH = self.PROPERTIES["{ENV}_PATH".format(ENV=self.ENV)]

        self.FIELDS = self.PROPERTIES["INTERESTING_FIELS"].split(',')

        # Lendo o tipo de Delimitador do CSV (Vírgula, Ponto-Vírgula, Tabulação)
        self.DELIMITER = self.PROPERTIES["{ENV}_DELIMITER".format(ENV=self.ENV)]

        # Abrindo o Arquivo
        self.FILE = open(self.PATH, mode='rb')

    def read_file(self):

        # Criando um Leitor de CSV
        spamreader = csv.reader(self.FILE, delimiter=self.DELIMITER)

        return spamreader


    def format_toMongo(self, dictionary):

        # Filtrando em cada um dos campos que foram determinados
        object = dict(filter(lambda i:i[0] in self.FIELDS , dictionary.iteritems()))


        # Formatando as Datas de cada hash
        for key in object.keys():
            if not key.startswith("DAT"):
                continue
            if object[key]:
                object[key] = datetime.datetime.strptime(object[key], "%d-%m-%Y")
            else:
                object[key] = None
        return object