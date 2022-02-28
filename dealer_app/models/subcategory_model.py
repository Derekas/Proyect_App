# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class SubcategoryModel(models.Model):
    _name = 'dealer_app.subcategory_model'
    _description = 'Subcategory_model'
    
    name = fields.Char(string="Name",required=True,index=True,help="Category Name")
    description = fields.Html(string="Description",required=True)
    category_id= fields.Many2one("dealer_app.category_model", String="Category")