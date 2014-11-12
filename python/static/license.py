#!/usr/bin/env python
# -*- coding: utf-8 -*-
from request import Request

class License:

    def __init__(self):
        self.request = Request()


    # Função que retorna uma Lista de Pacotes
    def list_license(self):
        
        # Url da Requisição
        url_request = "/api/action/license_list"
        
        # Parametros da Requisição (Para essa requisição não há nenhum parametro, logo o dicionário vai vazio
        return self.request.do_Request(url_request, params_request={})