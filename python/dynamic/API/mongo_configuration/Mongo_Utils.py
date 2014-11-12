#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response
from werkzeug.routing import BaseConverter, ValidationError
from base64 import urlsafe_b64encode, urlsafe_b64decode
from bson.objectid import ObjectId
from bson.errors import InvalidId
import datetime

try:
    import json
except ImportError:
    import simplejson as json

try:
    from bson.objectid import ObjectId
except:
    pass


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.strftime("%d/%m/%Y")
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def jsonify(data):
    return Response(json.dumps(data, cls=APIEncoder),
                    mimetype='application/json')


def json_return(collection, collection_name):
   json_results =[]
   for result in collection:
      json_results.append(result)
   return jsonify({collection_name:json_results})



class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(urlsafe_b64decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return urlsafe_b64encode(value.binary)