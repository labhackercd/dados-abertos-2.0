#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pyjavaproperties import Properties

class ResourceConfiguration:

    def __init__(self, package_id):
   

        # Dicionário de Dados para Criação/Update dos Pacotes
        self.PACKAGE_DICT= {
            'package_id': package_id,
            'name':  self.PROPERTIES['NAME'],
            'description': self.PROPERTIES['VERSION'],
            'size' :, 
            'mimetype':,
            'upload':,
            'format':,
            'last_modified':
        }





# package_id (string) – id of package that the resource needs should be added to.
# url (string) – url of resource
# revision_id – (optional)
# description (string) – (optional)
# format (string) – (optional)
# hash (string) – (optional)
# name (string) – (optional)
# resource_type (string) – (optional)
# mimetype (string) – (optional)
# mimetype_inner (string) – (optional)
# webstore_url (string) – (optional)
# cache_url (string) – (optional)
# size (int) – (optional)
# created (iso date string) – (optional)
# last_modified (iso date string) – (optional)
# cache_last_updated (iso date string) – (optional)
# webstore_last_updated (iso date string) – (optional)
# upload (FieldStorage (optional) needs multipart/form-data) – (optional)