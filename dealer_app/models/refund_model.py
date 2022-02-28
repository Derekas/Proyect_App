# -*- coding: utf-8 -*-

from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class RefundModel(models.Model):
    _name = 'dealer_app.refund_model'
    _description = 'Refund_model'
    
    reference = fields.Integer(string="Ref",required=True,index=True,help="Refound Reference")
    date = fields.Date(string="Date",required=True,help="Refound Date",default=datetime.now())
    base = fields.Float(string="Base",default=0,compute="_check_base",help="Base",store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')],default='21',help="VAT")
    total = fields.Float(string="Total",default=0,compute="_check_total",help="Total",store=True)
    status = fields.Selection(string="Status",selection=[('Draft','Draft'),('Confirm','Confirm')],help="Status", default="Draft")
    
    lines_ids=fields.One2many("dealer_app.lines_model","refund_id",string="Lines")
    client_id=fields.Many2one("dealer_app.client_model",string="Client")

    def confirm(self):
        self.ensure_one()
        self._cr.autocommit(False)
        if self.status=="Draft":
            self.status="Confirm"
            for rec in self.lines_ids:
                if rec.quantity <=rec.product_id.stock:
                    rec.product_id.stock += rec.quantity
                else:
                    raise ValidationError("There is no Stock of "+rec.product_id.name+"!")
        self._cr.commit()
        self._cr.autocommit(True)
        return True

    @api.depends("lines_ids")
    def _check_base(self):
        sum = 0
        for line in self.lines_ids:
            sum += line.product_id.price*line.quantity
        self.base = sum

    @api.depends("base", "vat")
    def _check_total(self):
        self.total = self.base*int(self.vat)/100.0 + self.base

    def confirm(self):
        self.ensure_one()
        if self.status=="Draft":
            self.status="Confirm"
            for rec in self.lines_ids:
                if rec.quantity <=rec.product_id.stock:
                    rec.product_id.stock -= rec.quantity
                else:
                    raise ValidationError("There is no Stock of "+rec.product_id.name+"!")
        return True

    
    @api.model 
    def create(self, vals): 
     
        vals['reference'] =self.env['ir.sequence'].next_by_code('reference.test')      
        return super(RefundModel, self).create(vals)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
