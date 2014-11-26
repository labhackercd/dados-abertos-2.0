#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.pymongo import PyMongo
from pyjavaproperties import Properties
from flask import Flask
from pymongo import MongoClient

class MongoConfiguration:

    def __init__(self):

        # Lendo o arquivo de configuração
        self.CONFIG_FILE = os.path.dirname(os.path.realpath(__file__))+"/config/mongo.properties"

        # Lendo o arquivo de configurações no caminho a ser modificado conforme o caminho acima
        self.PROPERTIES = Properties()
        self.PROPERTIES.load(open(self.CONFIG_FILE))


        # Lendo Qual ambiente deve ser utilizado: Homologação ou Test
        self.ENV = self.PROPERTIES['ENV']



    def flask_context(self,app):

        # Conectando ao Mongo com HOST, PORT, DB_NAME
        app.config['MONGO1_HOST'] = self.PROPERTIES["{ENV}_HOST".format(ENV=self.ENV)]
        app.config['MONGO1_PORT'] = self.PROPERTIES["{ENV}_PORT".format(ENV=self.ENV)]
        app.config['MONGO1_DBNAME'] = self.PROPERTIES["{ENV}_DBNAME".format(ENV=self.ENV)]
        database = PyMongo(app, config_prefix='MONGO1')
        return database

    def general_context(self):
        connection = MongoClient(self.PROPERTIES["{ENV}_HOST".format(ENV=self.ENV)],
                                      int(self.PROPERTIES["{ENV}_PORT".format(ENV=self.ENV)]))

        database = connection[self.PROPERTIES["{ENV}_DBNAME".format(ENV=self.ENV)]]

        return database
