# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
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


    @api.constrains('dni')
    def validate_dni(self):
        if not self.check_DNI(self.dni):
            raise ValidationErr("Error DNI!!!!")

    def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False

    @api.constrains('email')
    def validate_dni(self):
        if "@" and "." not in self.email:
            raise ValidationErr("Email format error!!!!")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
