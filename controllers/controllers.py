# -*- coding: utf-8 -*-
# from odoo import http


# class Reunions(http.Controller):
#     @http.route('/reunions/reunions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reunions/reunions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reunions.listing', {
#             'root': '/reunions/reunions',
#             'objects': http.request.env['reunions.reunions'].search([]),
#         })

#     @http.route('/reunions/reunions/objects/<model("reunions.reunions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reunions.object', {
#             'object': obj
#         })

