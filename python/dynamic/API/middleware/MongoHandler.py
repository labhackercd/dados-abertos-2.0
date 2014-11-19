# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'baufaker'
from mongo_configuration.Mongo_Utils import json_return


class Mongo_Handler:

    def __init__(self, mongo, lim):
        self.mongo = mongo
        self.lim = lim

    def evaluate_request(self, collection_name,request_handler, lim):

        # Efetuando a Consulta Paginada
        collection = self.mongo.db[collection_name] \
            .find(request_handler.params) \
            .skip((request_handler.page_number-1)*self.lim) \
            .limit(self.lim)

        # Total de Registros
        total = collection.count()

        # Total de Páginas
        page_total = (total//self.lim)+1

        # Dicionário de Resultados
        result_dict = {
            'Limite de Exibição por Página': self.lim,
            'Página Atual': request_handler.page_number,
            'Total de Páginas': page_total,
            'Total de Resultados': total
        }


        # Se o número da página solicitado estiver dentro do intervalo válido
        if request_handler.page_number > page_total:
            raise OverflowError

        # Retornando o JSON da coleção
        return json_return(collection, collection_name, result_dict)


