#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
import urllib2
from setup_configuration import SetupConfiguration
from response import Response


class Request:

    def __init__(self):
        self.setup_configuration = SetupConfiguration()
       

    def do_Request(self, url_request, params_request):

        data_string = urllib.quote(json.dumps(params_request))
        
        # Formantando o Endereço da Requisição
        request = urllib2.Request("{URL_BASE}".format(URL_BASE=self.setup_configuration.URL_BASE)+url_request)
        
        # Adicionando a Autorização para requisção
        request.add_header('Authorization', self.setup_configuration.AUTH)
     
        # Fazendo a Requisição HTTP com o dicionário convertido em String
        response_http = urllib2.urlopen(request, data_string)
        
        # Convertendo a resposta para um dicioário
        response_list_dict = json.loads(response_http.read())

        # Criando uma Resposta com o código HTTP da resposta, o resultado e se a requisição teve sucesso ou não
        response = Response(response_http.code, response_list_dict['result'], response_list_dict['success'])
     
        # Retornando Resultado da Requisição
        return response

        




