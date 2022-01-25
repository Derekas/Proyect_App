# -*- coding: utf-8 -*-

from datetime import datetime
from xml.dom import ValidationErr
from odoo import models, fields, api


class RefundModel(models.Model):
    _name = 'dealer_app.refund_model'
    _description = 'Refund_model'
    
    reference = fields.Integer(string="Ref",required=True,index=True,help="Invoice Reference")
    date = fields.Date(string="Date",required=True,help="Invoice Date",default=datetime.now())
    base = fields.Float(string="Base",default=0,compute="_check_base",help="Base",store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')],default='21',help="VAT")
    total = fields.Float(string="Total",default=0,compute="_check_total",help="Total",store=True)
    status = fields.Selection(string="Status",selection=[('Draft','Draft'),('Confirm','Confirm')],help="Status", default="Draft")
    
    
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
