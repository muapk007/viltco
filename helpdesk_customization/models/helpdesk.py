# -*- coding: utf-8 -*-


import datetime
from odoo import models, fields, api
from datetime import datetime


class AlarmType(models.Model):
    _name = 'alarm.type'
    _description = 'Alarm Type'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    alarm_ids = fields.Many2many('helpdesk.ticket.type')


class HelpDeskInh(models.Model):
    _inherit = 'helpdesk.ticket'

    part_ids = fields.One2many('helpdesk.parts.line', 'ticket_id')
    ticket_ids = fields.Many2many('helpdesk.ticket.type')
    location_id = fields.Many2one('stock.location', required=True)
    location_dest_id = fields.Many2one('stock.location', required=True)

    cctv_installed = fields.Many2many('product.product', 'name', 'uom_id',related='site_id.cctv_installed')
    ptz_camera = fields.Many2one('product.product', related='site_id.ptz_camera')
    contractor_name = fields.Many2one('res.partner', related='site_id.contractor_name')
    site_contactor = fields.Many2one('contact.name', related='site_id.site_contactor')
    no_of_ptz = fields.Many2many('product.product', 'type', 'barcode',related='site_id.no_of_ptz')
    cctv_camera = fields.Many2one('product.product', related='site_id.cctv_camera')
    ptz_contactor_name = fields.Many2one('res.partner', related='site_id.ptz_contactor_name')
    ptz_site_name = fields.Many2one('contact.name', related='site_id.ptz_site_name')
    no_of_fibre = fields.Many2many('product.product', 'default_code', 'categ_id' ,related='site_id.no_of_fibre')
    fibre_info = fields.Many2one('product.product', related='site_id.fibre_info')
    fibre_contractor_name = fields.Many2one('res.partner', related='site_id.fibre_contractor_name')
    fibre_site_name = fields.Many2one('contact.name', related='site_id.fibre_site_name')
    ip_address = fields.Char('IP Address', related='site_id.ip_address')

    is_pole = fields.Boolean('Pole & Pole Foundation', related='site_id.is_pole')
    is_outdoor = fields.Boolean('Outdoor Closures', related='site_id.is_outdoor')
    is_battery = fields.Boolean('Battery Closures', related='site_id.is_battery')
    is_civil = fields.Boolean('Civil & Fiber Network', related='site_id.is_civil')
    is_optical = fields.Boolean('Optical Testing: Fiber Optical Length Measurement', related='site_id.is_optical')
    is_attenuation = fields.Boolean('Optical Testing: Attenuation Test', related='site_id.is_attenuation')
    is_camera = fields.Boolean('Cameras', related='site_id.is_camera')
    is_site = fields.Boolean('Site Power', related='site_id.is_site')
    is_wireless = fields.Boolean('Wireless System', related='site_id.is_wireless')

    site_id = fields.Many2one('maintenance.equipment')

    pole_lines = fields.One2many('pole.line', 'site_id', related='site_id.pole_lines')
    outdoor_lines = fields.One2many('outdoor.line', 'site_id', related='site_id.outdoor_lines')
    battery_lines = fields.One2many('battery.line', 'site_id', related='site_id.battery_lines')
    civil_lines = fields.One2many('civil.line', 'site_id', related='site_id.civil_lines')
    fibre_lines = fields.One2many('fibre.line', 'site_id', related='site_id.fibre_lines')
    attenuation_lines = fields.One2many('attenuation.line', 'site_id', related='site_id.attenuation_lines')
    camera_lines = fields.One2many('camera.line', 'site_id', related='site_id.camera_lines')
    site_lines = fields.One2many('site.line', 'site_id', related='site_id.site_lines')
    wireless_lines = fields.One2many('wireless.line', 'site_id', related='site_id.wireless_lines')

    # pole_pic = fields.Binary('Attach Picture', related='site_id.pole_pic')
    # outdoor_pic = fields.Binary('Attach Picture', related='site_id.outdoor_pic')
    # battery_pic = fields.Binary('Attach Picture', related='site_id.battery_pic')
    # civil_pic = fields.Binary('Attach Picture', related='site_id.civil_pic')
    # fibre_pic = fields.Binary('Attach Picture', related='site_id.fibre_pic')
    # attenuation_pic = fields.Binary('Attach Picture', related='site_id.attenuation_pic')
    # camera_pic = fields.Binary('Attach Picture', related='site_id.camera_pic')
    # site_pic = fields.Binary('Attach Picture', related='site_id.site_pic')
    # wireless_pic = fields.Binary('Attach Picture', related='site_id.wireless_pic')

    pole_pic = fields.Many2many('ir.attachment', 'res_model', related='site_id.pole_pic')
    outdoor_pic = fields.Many2many('ir.attachment', 'file_size', related='site_id.outdoor_pic')
    battery_pic = fields.Many2many('ir.attachment', 'url', related='site_id.battery_pic')
    civil_pic = fields.Many2many('ir.attachment', 'name', related='site_id.civil_pic')
    fibre_pic = fields.Many2many('ir.attachment', 'original_id', related='site_id.fibre_pic')
    attenuation_pic = fields.Many2many('ir.attachment', 'res_id', related='site_id.attenuation_pic')
    camera_pic = fields.Many2many('ir.attachment', 'res_name', related='site_id.camera_pic')
    site_pic = fields.Many2many('ir.attachment', 'public', related='site_id.site_pic')
    wireless_pic = fields.Many2many('ir.attachment', 'type', related='site_id.wireless_pic')

    pole_comment = fields.Text('Comments', related='site_id.pole_comment')
    outdoor_comment = fields.Text('Comments', related='site_id.outdoor_comment')
    battery_comment = fields.Text('Comments', related='site_id.battery_comment')
    civil_comment = fields.Text('Comments', related='site_id.civil_comment')
    fibre_comment = fields.Text('Comments', related='site_id.fibre_comment')
    attenuation_comment = fields.Text('Comments', related='site_id.attenuation_comment')
    camera_comment = fields.Text('Comments', related='site_id.camera_comment')
    site_comment = fields.Text('Comments', related='site_id.site_comment')
    wireless_comment = fields.Text('Comments', related='site_id.wireless_comment')

    is_client_approved = fields.Boolean('Client Approved', tracking=True)
    is_contractor_approved = fields.Boolean('Contractor Approved', tracking=True)

    def action_contractor_approve(self):
        self.is_contractor_approved = True

    def action_client_approve(self):
        self.is_client_approved = True

    def action_validate(self):
        for rec in self.part_ids:
            if not rec.is_picking_created:
                if rec.type == 'add':
                    outgoing_pick = self.env['stock.picking.type'].search([('code', '=', 'outgoing')], limit=1)
                    vals = {
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'partner_id': self.partner_id.id,
                        'picking_type_id': outgoing_pick.id,
                        'scheduled_date': datetime.now(),
                        'move_type': 'direct',
                    }
                    picking = self.env['stock.picking'].create(vals)
                    lines = {
                        'picking_id': picking.id,
                        'product_id': rec.product_id.id,
                        'name': rec.product_id.name,
                        'product_uom': rec.product_id.uom_id.id,
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'product_uom_qty': rec.qty,
                    }
                    stock_move = self.env['stock.move'].create(lines)
                    picking.action_confirm()
                    rec.delivered_id = picking.id
                    rec.is_picking_created = True
                if rec.type == 'remove':
                    incoming_pick = self.env['stock.picking.type'].search([('code', '=', 'incoming')], limit=1)
                    vals = {
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'partner_id': self.partner_id.id,
                        'picking_type_id': incoming_pick.id,
                        'scheduled_date': datetime.now(),
                        'move_type': 'direct',
                    }
                    picking = self.env['stock.picking'].create(vals)
                    lines = {
                        'picking_id': picking.id,
                        'product_id': rec.product_id.id,
                        'name': rec.product_id.name,
                        'product_uom': rec.product_id.uom_id.id,
                        'location_id': self.location_id.id,
                        'location_dest_id': self.location_dest_id.id,
                        'product_uom_qty': rec.qty,
                    }
                    stock_move = self.env['stock.move'].create(lines)
                    picking.action_confirm()
                    rec.received_id = picking.id
                    rec.is_picking_created = True


class HelpDeskPartsLine(models.Model):
    _name = 'helpdesk.parts.line'

    ticket_id = fields.Many2one('helpdesk.ticket')
    request_id = fields.Many2one('maintenance.request')
    type = fields.Selection([('add', 'Add'),
                                ('remove', 'Remove')], string='Type', required=True)
    product_id = fields.Many2one('product.product', required=True)
    name = fields.Char(related='product_id.name')
    lot_id = fields.Many2one('stock.production.lot', domain="[('product_id', '=', product_id)]")
    # quant_id = fields.Many2one('stock.quant')
    qty = fields.Float('Qty')
    uom_id = fields.Many2one('uom.uom', related='product_id.uom_id')
    received_id = fields.Many2one('stock.picking')
    delivered_id = fields.Many2one('stock.picking')
    receive_qty = fields.Float(compute='compute_qty_done')
    delivered_qty = fields.Float(compute='compute_qty_done')
    is_picking_created = fields.Boolean()

    product_ids = fields.Many2many('product.product', 'currency_id', 'activity_type_id',
                                   compute='compute_products_added')

    @api.depends('type')
    def compute_products_added(self):
        for rec in self:
            product_list = []
            products = self.env['product.product'].search([])
            if rec.type == 'remove':
                if rec.request_id:
                    rec.product_ids = rec.request_id.equipment_id.product_ids.ids
                if rec.ticket_id:
                    rec.product_ids = rec.ticket_id.site_id.product_ids.ids
            else:
                rec.product_ids = products.ids

    def compute_qty_done(self):
        for rec in self:
            qty = 0
            if rec.received_id:
                for line in rec.received_id.move_line_ids_without_package:
                    qty = qty + line.qty_done
            if rec.delivered_id:
                for line in rec.delivered_id.move_line_ids_without_package:
                    qty = qty + line.qty_done
            rec.receive_qty = qty
            rec.delivered_qty = qty
