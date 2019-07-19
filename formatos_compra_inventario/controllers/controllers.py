# -*- coding: utf-8 -*-
from odoo import http

# class FormatosCompraInventario(http.Controller):
#     @http.route('/formatos_compra_inventario/formatos_compra_inventario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formatos_compra_inventario/formatos_compra_inventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formatos_compra_inventario.listing', {
#             'root': '/formatos_compra_inventario/formatos_compra_inventario',
#             'objects': http.request.env['formatos_compra_inventario.formatos_compra_inventario'].search([]),
#         })

#     @http.route('/formatos_compra_inventario/formatos_compra_inventario/objects/<model("formatos_compra_inventario.formatos_compra_inventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formatos_compra_inventario.object', {
#             'object': obj
#         })