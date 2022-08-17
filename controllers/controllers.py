# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTricks(http.Controller):
#     @http.route('/odoo_tricks/odoo_tricks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_tricks/odoo_tricks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_tricks.listing', {
#             'root': '/odoo_tricks/odoo_tricks',
#             'objects': http.request.env['odoo_tricks.odoo_tricks'].search([]),
#         })

#     @http.route('/odoo_tricks/odoo_tricks/objects/<model("odoo_tricks.odoo_tricks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_tricks.object', {
#             'object': obj
#         })
