# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from odoo import models, fields, api


class ArticleModel(models.Model):
    _name = 'dealer_app.article_model'
    _description = 'Article_model'
    
    name = fields.Char(string="name",required=True,index=True,help="Client Name")
    description = fields.Html(string="Description",required=True)
    price = fields.Float(compute="_value_pc", store=True)
    stock = fields.Text()
    photo = fields.Binary(string="Photo",help="Photo")

    @api.constrains("price")
    def check_price(self):
        if self.price < 0:
            raise ValidationErr("Price must be greater o equal than 0!!")

    @api.constrains("stock")
    def check_stock(self):
        if self.stock < 0:
            raise ValidationErr("Stock must be greater o equal than 0!!")
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
