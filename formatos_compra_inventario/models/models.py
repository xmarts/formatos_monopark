# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	cedis = fields.Char(string="Cedis")
	transporte = fields.Char(string="Transporte")
	enatencion = fields.Char(string="En atención")

	tipo_de = fields.Selection([('tipo1', 'Tipo 1'),('tipo2', 'Tipo 2')], string="Tipo de")
	empleado = fields.Many2one('hr.employee', string="Empleado")
	num_pedido = fields.Char(string="Número de pedido")
	fecha_limite_pago = fields.Date(string="Fecha limite de pago")

	client=fields.Binary(string='Cliente')
	consul=fields.Binary(string='Consultor')

class ResPartner(models.Model):
	_inherit = "res.partner.bank"

	clabe_campo = fields.Char(string="Clabe")

class ResPartner2(models.Model):
	_inherit = "res.partner"

	clabe_campo = fields.Char(string="Clabe")

class StockPicking(models.Model):
	_inherit = "stock.picking"

	entrega = fields.Char(string="Entrega")
	instaladores = fields.Char(string="Instaladores")