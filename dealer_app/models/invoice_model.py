# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class InvoiceModel(models.Model):
    _name = 'dealer_app.invoice_model'
    _description = 'Invoice_model'
    
    _sql_constraints = [ ('invoice_unique_ref','UNIQUE (reference)','Reference must be unique!!'), ]


    reference = fields.Integer(string="Rederencia",required=True,index=True,help="Invoice Reference")
    date = fields.Date(string="Date",required=True,help="Invoice Date",default=datetime.now())
    base = fields.Float(string="Base",default=0,compute="_check_base",help="Base",store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')],default='21',help="VAT")
    total = fields.Float(string="Total",default=0,compute="_check_total",help="Total",store=True)
    status = fields.Selection(string="Status",selection=[('Draft','Draft'),('Confirm','Confirm')],help="Status", default="Draft")
    
    lines_ids=fields.One2many("dealer_app.lines_model","invoice_id",string="Lines")
    client_id=fields.Many2one("dealer_app.client_model",string="Client")
    
    def confirm(self):
        self.ensure_one()
        self._cr.autocommit(False)
        if self.status=="Draft":
            self.status="Confirm"
            for rec in self.lines_ids:
                if rec.quantity <=rec.product_id.stock:
                    rec.product_id.stock -= rec.quantity
                else:
                    raise ValidationError("There is no Stock of "+rec.product_id.name+"!")
            for lin in self.lines_ids:
                for extras in lin.extras_ids:
                    if extras.quantity <=extras.extras_ids.stock:
                        extras.extras_ids.stock -= extras.quantity
                    else:
                        raise ValidationError("There is no Stock of "+rec.product_id.name+"!")
        self._cr.commit()
        self._cr.autocommit(True)
        return True


    @api.model 
    def create(self, vals): 
     
        vals['reference'] =self.env['ir.sequence'].next_by_code('reference.test')      
        return super(InvoiceModel, self).create(vals)

    @api.depends("lines_ids")
    def _check_base(self):
        sum = 0
        for line in self.lines_ids:
            sum += line.product_id.price*line.quantity
        for lin in self.lines_ids:
            for extras in lin.extras_ids:

                sum += extras.price*lin.quantity
        self.base = sum

    @api.depends("base", "vat")
    def _check_total(self):
        self.total = self.base*int(self.vat)/100.0 + self.base
