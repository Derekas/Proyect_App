# -*- coding: utf-8 -*-

import re
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class ClientModel(models.Model):
    _name = 'dealer_app.client_model'
    _description = 'Client_model'
    
    name = fields.Char(string="name",required=True,index=True,help="Client Name")
    surname = fields.Char(string="Surname",required=True,index=True,help="Surname")
    dni = fields.Char(string="DNI",size=9,required=True,index=True,help="DNI")
    photo = fields.Binary(string="Photo",help="Photo")
    phone = fields.Char(string="Phone",size=9,help="Phone")
    email = fields.Char(string="Email",required=True,help="Email")

    invoices_ids=fields.One2many("dealer_app.invoice_model","client_id",string="Invoices")
    refund_ids=fields.One2many("dealer_app.refund_model","client_id",string="Invoices")


    @api.constrains("dni")
    def _check_DNI(self):
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        
            
        dni = self.dni
        letter = dni[-1].upper()
        number = dni[:-1]
        if (len(dni) == 9 and number.isdigit()):
            number = int(dni[:-1])
        else:
            raise ValidationError("Incorrect Format DNI")

        mod = number%23
        if letters[mod] != letter:
            raise ValidationError("Incorrect Letter")

    @api.constrains("email")
    def _check_Email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, self.email)):
                pass
        else:
            raise ValidationError("Gmail incorrecto")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
