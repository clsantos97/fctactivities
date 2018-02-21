# -*- coding: utf-8 -*-
from odoo import http

# class Fctactivities(http.Controller):
#     @http.route('/fctactivities/fctactivities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fctactivities/fctactivities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fctactivities.listing', {
#             'root': '/fctactivities/fctactivities',
#             'objects': http.request.env['fctactivities.fctactivities'].search([]),
#         })

#     @http.route('/fctactivities/fctactivities/objects/<model("fctactivities.fctactivities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fctactivities.object', {
#             'object': obj
#         })