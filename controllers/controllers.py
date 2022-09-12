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
        data = request.jsonrequest
        for value in data['data']['line']:
            line = request.env['purchase.order.line'].search([('id', '=', value['id'])])
            line.sudo().price_unit = value['unit_price']
            request.env['purchase.order'].sudo().search([('id', '=', int(data['data']['order_id']))]).vendor_price_update = True

        user = request.env['purchase.order'].sudo().search([('id', '=', int(data['data']['order_id']))]).user_id
        template = request.env.ref('odoo_tricks.mail_template_purchase_order_unit_price_updated', raise_if_not_found=False).sudo()
        
        if user and template:
            template.email_to = user.email
            template.send_mail(int(data['data']['order_id']), force_send=True)
        return {
            'done': 'Done',
        }

    @http.route('/404', auth='public', website=True)
    def not_found(self, **kw):
        return http.request.render('odoo_tricks.404', {})


    
