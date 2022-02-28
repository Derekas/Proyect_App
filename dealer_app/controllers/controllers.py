# -*- coding: utf-8 -*-
# from odoo import http


# class DealerApp(http.Controller):
#     @http.route('/dealer_app/dealer_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dealer_app/dealer_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dealer_app.listing', {
#             'root': '/dealer_app/dealer_app',
#             'objects': http.request.env['dealer_app.dealer_app'].search([]),
#         })

#     @http.route('/dealer_app/dealer_app/objects/<model("dealer_app.dealer_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dealer_app.object', {
#             'object': obj
#         })
