# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime
from odoo.exceptions import UserError, ValidationError

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	cedis = fields.Char(string="Cedis")
	transporte = fields.Char(string="Transporte")
	enatencion = fields.Char(string="En atención")

	tipo_de = fields.Selection([('tipo1', 'Insumos'),('tipo2', 'Herramientas de trabajo'),('tipo3','Materiales'),('tipo4','Servicios'),
		('tipo5','Subministros'),('tipo6','Refacciones'),('tipo7','Compra'),('tipo','Producto a fabricación')], string="Tipo de")

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
	estado_reserva = fields.Selection([
		('Anticipo','Anticipo'),
		('Autorizado_sin_pago','Autorizado sin pago'),
		('Pago_total_sin_documentos','Pago total sin documentos'),
		('Listo_para_entregar','Listo para entregar'),
		('listo_para_recibir','Listo para recibir')],
		string="Estado de reserva")
	estado_reserva_ro = fields.Selection([
		('Anticipo','Anticipo'),
		('Autorizado_sin_pago','Autorizado sin pago'),
		('Pago_total_sin_documentos','Pago total sin documentos'),
		('Listo_para_entregar','Listo para entregar'),
		('listo_para_recibir','Listo para recibir')],
		string="Estado de reserva", related='estado_reserva', readonly=True)

	is_devolucion = fields.Boolean(string="¿Es devolución?", default=False) 

	@api.one
	def _compute_fecha_actual(self):
		fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.fecha_actual = fecha

	@api.onchange('picking_type_code')
	def onchange_picking_type_code(self):
		if self.picking_type_code == 'incoming':
			self.estado_reserva='listo_para_recibir'
		elif self.picking_type_code =='internal':
			self.estado_reserva="Listo_para_entregar"
		else:
			self.estado_reserva=""
	@api.multi
	def action_assign(self):
		""" Check availability of picking moves.
		This has the effect of changing the state and reserve quants on available moves, and may
		also impact the state of the picking as it is computed based on move's states.
		@return: True
		"""
		self.filtered(lambda picking: picking.state == 'draft').action_confirm()

		moves = self.mapped('move_lines').filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))

		if not self.is_devolucion:
			if not moves:
				raise UserError(_('Nothing to check the availability for.'))

		# If a package level is done when confirmed its location can be different than where it will be reserved.
		# So we remove the move lines created when confirmed to set quantity done to the new reserved ones.
		package_level_done = self.mapped('package_level_ids').filtered(lambda pl: pl.is_done and pl.state == 'confirmed')
		package_level_done.write({'is_done': False})
		moves._action_assign()
		package_level_done.write({'is_done': True})
		return True


class StockMove(models.Model):
	_inherit = "stock.move"

	observacion_pro = fields.Text()
	bultos = fields.Integer()

class FunctionReserv(models.Model):
	_inherit = 'procurement.group'

	@api.model
	def _get_moves_to_assign_domain(self):
		return expression.AND([
			[('state', 'in', ['confirmed', 'partially_available']),('estado_reserva','=','Listo_para_entregar')],
			[('product_uom_qty', '!=', 0.0)]
		])

class hr_inherit(models.Model):
	_inherit="hr.employee"

	number_em = fields.Integer(string="Número de empleado")
	date_in=fields.Date(string="Fecha de ingreso")
	date_out=fields.Date(string="Fecha de baja")
	kind_blood=fields.Char(string="Tipo de sangre")