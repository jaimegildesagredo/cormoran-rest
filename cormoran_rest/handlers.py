# -*- coding: utf-8 -*-

import httplib

from tornado import web
from tornado import escape


class RestHandler(web.RequestHandler):
    def initialize(self, store, model):
        self._store = store
        self._model = model

    def post(self):
        entity = self._model(**escape.json_decode(self.request.body))
        self._store.add(entity)
        self._store.commit()
        self.set_status(httplib.CREATED)
        self.write(dict(entity))

    def get(self):
        self.write(escape.json_encode([dict(x) for x in self._store.find(self._model)]))
        self.set_header('Content-Type', 'application/json')
