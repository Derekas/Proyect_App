# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class CategoryModel(models.Model):
    _name = 'dealer_app.category_model'
    _description = 'Category_model'
    
    name = fields.Char(string="Name",required=True,index=True,help="Category Name")
    description = fields.Html(string="Description",required=True)
    
    subcategory_ids=fields.One2many("dealer_app.subcategory_model","category_id",String="Subcategory")