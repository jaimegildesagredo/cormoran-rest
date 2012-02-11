# -*- coding: utf-8 -*-

import httplib

from tornado import web
from tornado import escape
from tornado import testing

from hamcrest import *
from pyDoubles.framework import *

from cormoran.persistent import Persistent
from cormoran.fields import StringField
from cormoran_rest import handlers

class _Model(Persistent):
    __cormoran_name__ = u'models'

    field = StringField()


class TestRestHandler(testing.AsyncHTTPTestCase):
    def test_create_saves_new_entity_from_json(self):
        response = self.fetch(
            '/resource',
            method='POST',
            body=escape.json_encode(dict(self.entity))
        )

        assert_that(response.code, is_(httplib.CREATED))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(dict(self.entity)))

        assert_that_method(self.store.add).was_called()
        assert_that_method(self.store.commit).was_called()

    def test_index_all_persisted_entities(self):
        when(self.store.find).with_args(self.model).then_return([self.entity])

        response = self.fetch('/resource')

        assert_that(response.code, is_(httplib.OK))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_([dict(self.entity)]))

    def get_app(self):
        self.model = _Model
        self.entity = self.model(field=u'test')

        self.store = empty_spy()

        handler_init = dict(store=self.store, model=self.model)

        return web.Application([
            web.url('/resource', handlers.RestHandler, handler_init)
        ])
