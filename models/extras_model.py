# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class ExtrasModel(models.Model):
    _name = 'dealer_app.extras_model'
    _description = 'Extras_model'
    
    name = fields.Char(string="name",required=True,index=True,help="Extra Name")
    description = fields.Html(string="Description",required=True)
    price = fields.Float(string="Price",required=True, default=0 ,help="Price for extras")
    stock = fields.Integer(string="Stock",required=True,default=1,help="Quantity for this extra")
    photo = fields.Binary(string="Photo",help="Photo")

    

    @api.constrains("price")
    def check_price(self):
        if self.price < 0:
            raise ValidationError("Price must be greater o equal than 0!!")

    @api.constrains("stock")
    def check_stock(self):
        if self.stock < 0:
            raise ValidationError("Stock must be greater o equal than 0!!")
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
