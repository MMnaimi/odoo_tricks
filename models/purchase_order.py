# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_price_update = fields.Boolean(default=False)
    
    def view_purchase_order(self):
        for rec in self:
            web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            action = self.env.ref('purchase.purchase_rfq', raise_if_not_found=False)
            return f"{web_base_url}/web#id={self.id}&view_type=form&model=purchase.order&action={action.id}"


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    vendor_price_update = fields.Boolean(related='order_id.vendor_price_update')
    