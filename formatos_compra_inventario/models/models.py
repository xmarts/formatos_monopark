# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	cedis = fields.Char(string="Cedis")
	transporte = fields.Char(string="Transporte")
	enatencion = fields.Char(string="En atención")

	tipo_de = fields.Selection([('tipo1', 'Insumos'),('tipo2', 'Herramientas de trabajo'),('tipo3','Materiales'),('tipo4','Servicios'),('tipo5','Subministros'),('tipo6','Refacciones'),('tipo7','Compra')], string="Tipo de")
	empleado = fields.Many2one('hr.employee', string="Atención a.")

	#CAMBIOS DEL 201019
	solicito = fields.Many2one('hr.employee', string="Solicitado por")
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
	destino = fields.Char(string="Destino")
	obser_recep = fields.Text(string="Observaciones")
	obser_esp = fields.Text(string="Condiciones especiales")
	fecha_actual = fields.Char(string="Fecha actual", compute="_compute_fecha_actual")
	estado_reserva = fields.Selection([('Anticipo','Anticipo'),('Autorizado_sin_pago','Autorizado sin pago'),('Pago_total_sin_documentos','Pago total sin documentos'),('Listo_para_entregar','Listo para entregar'),('listo_para_recibir','Listo para recibir')],string="Estado de reserva")
	estado_reserva_ro = fields.Selection([('Anticipo','Anticipo'),('Autorizado_sin_pago','Autorizado sin pago'),('Pago_total_sin_documentos','Pago total sin documentos'),('Listo_para_entregar','Listo para entregar'),('listo_para_recibir','Listo para recibir')],string="Estado de reserva", related='estado_reserva', readonly=True)

	@api.one
	def _compute_fecha_actual(self):
		fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.fecha_actual = fecha

	@api.onchange('picking_type_code')
	def onchange_picking_type(self):
		if self.picking_type_code == 'incoming':
			self.estado_reserva='listo_para_recibir'
		else:
			self.estado_reserva=""

class StockMove(models.Model):
	_inherit = "stock.move"

	observacion_pro = fields.Text()
	bultos = fields.Integer()

class hr_inherit(models.Model):
	_inherit="hr.employee"

	number_em = fields.Integer(string="Número de empleado")
	date_in=fields.Date(string="Fecha de ingreso")
	date_out=fields.Date(string="Fecha de baja")
	kind_blood=fields.Char(string="Tipo de sangre")