# -*- coding: utf-8 -*-

import datetime
from xml.dom import ValidationErr
from odoo import models, fields, api


class LinesModel(models.Model):
    _name = 'dealer_app.lines_model'
    _description = 'Lines_model'
    
    quantity = fields.Integer(string="Quantity",required=True,index=True,default=1,help="Quantity")
    invoice_id= fields.Many2one("dealer_app.invoice_model",string="Invoice",help="Invoice reference")
    product_id=fields.Many2one("dealer_app.article_model",string="Article",help="Product reference")
    refund_id= fields.Many2one("dealer_app.refund_model",string="Refund",help="Refund reference")
    
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
