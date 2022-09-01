# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class OdooTricks(http.Controller):
    @http.route('/students', auth='user', methods=['GET', 'POST'], website=True)
    def index(self, **kw):
        students = request.env['student.student'].search([])
        return http.request.render('odoo_tricks.students', {
            'objects': students
        })

    @http.route('/test', auth='user', method=['POST'], type="json")
    def update_po(self, **kw):
        print(".>>>> hello and welcome")
        data = request.jsonrequest
        for value in data['data']:
            line = request.env['purchase.order.line'].search([('id', '=', value['id'])])
            line.sudo().price_unit = value['unit_price']
        return {
            'done': 'Done',
        }
    
    @http.route('/404', auth='public', website=True)
    def not_found(self, **kw):
        return http.request.render('odoo_tricks.404', {})


    
