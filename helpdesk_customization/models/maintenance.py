# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class MaintenanceEquipmentInherit(models.Model):
    _inherit = 'maintenance.equipment'

    cctv_installed = fields.Many2many('product.product', 'taxes_id', 'uom_id')
    ptz_camera = fields.Many2one('product.product')
    contractor_name = fields.Many2one('res.partner')
    site_contactor = fields.Many2one('contact.name')
    no_of_ptz = fields.Many2many('product.product', 'tic_category_id', 'uom_po_id')
    cctv_camera = fields.Many2one('product.product')
    ptz_contactor_name = fields.Many2one('res.partner')
    ptz_site_name = fields.Many2one('contact.name')
    no_of_fibre = fields.Many2many('product.product', 'default_code', 'categ_id')
    fibre_info = fields.Many2one('product.product')
    fibre_contractor_name = fields.Many2one('res.partner')
    fibre_site_name = fields.Many2one('contact.name')
    ip_address = fields.Char('IP Address')

    product_ids = fields.Many2many('product.product', 'currency_id', 'activity_type_id', compute='compute_products_added')

    def compute_products_added(self):
        requests = self.env['maintenance.request'].search([('equipment_id', '=', self.id)])
        tickets = self.env['helpdesk.ticket'].search([('site_id', '=', self.id)])
        product_list = []
        for request in requests:
            for request_line in request.part_ids:
                if request_line.type == 'add':
                    product_list.append(request_line.product_id.id)
        for ticket in tickets:
            for ticket_line in ticket.part_ids:
                if ticket_line.type == 'add':
                    product_list.append(ticket_line.product_id.id)
        self.product_ids = product_list

    is_pole = fields.Boolean('Pole & Pole Foundation')
    is_outdoor = fields.Boolean('Outdoor Closures')
    is_battery = fields.Boolean('Battery Closures')
    is_civil = fields.Boolean('Civil & Fiber Network')
    is_optical = fields.Boolean('Optical Testing: Fiber Optical Length Measurement')
    is_attenuation = fields.Boolean('Optical Testing: Attenuation Test')
    is_camera = fields.Boolean('Cameras')
    is_site = fields.Boolean('Site Power')
    is_wireless = fields.Boolean('Wireless System')

    pole_lines = fields.One2many('pole.line', 'site_id')
    outdoor_lines = fields.One2many('outdoor.line', 'site_id')
    battery_lines = fields.One2many('battery.line', 'site_id')
    civil_lines = fields.One2many('civil.line', 'site_id')
    fibre_lines = fields.One2many('fibre.line', 'site_id')
    attenuation_lines = fields.One2many('attenuation.line', 'site_id')
    camera_lines = fields.One2many('camera.line', 'site_id')
    site_lines = fields.One2many('site.line', 'site_id')
    wireless_lines = fields.One2many('wireless.line', 'site_id')

    site_type_id = fields.Many2one('site.type', required=True)
    site_code = fields.Char('Site Code')
    site_no = fields.Char('Site Number')
    site_assigned_to = fields.Date('Site Assigned To Date')
    # region = fields.Char('Region')
    # location = fields.Char('Location')
    # city = fields.Char('City')
    latitude = fields.Float('Latitude')
    longitude = fields.Float('longitude')

    pole_pic = fields.Many2many('ir.attachment','res_model')
    outdoor_pic = fields.Many2many('ir.attachment', 'file_size',)
    battery_pic = fields.Many2many('ir.attachment', 'url',)
    civil_pic = fields.Many2many('ir.attachment', 'name',)
    fibre_pic = fields.Many2many('ir.attachment', 'original_id',)
    attenuation_pic = fields.Many2many('ir.attachment', 'res_id',)
    camera_pic = fields.Many2many('ir.attachment', 'res_name',)
    site_pic = fields.Many2many('ir.attachment', 'public',)
    wireless_pic = fields.Many2many('ir.attachment', 'type',)

    pole_comment = fields.Text('Comments')
    outdoor_comment = fields.Text('Comments')
    battery_comment = fields.Text('Comments')
    civil_comment = fields.Text('Comments')
    fibre_comment = fields.Text('Comments')
    attenuation_comment = fields.Text('Comments')
    camera_comment = fields.Text('Comments')
    site_comment = fields.Text('Comments')
    wireless_comment = fields.Text('Comments')

    @api.onchange('is_pole')
    def onchange_is_pole(self):
        pole_list = []
        if self.is_pole:
            pole = self.env['alarm.type'].search([('name', '=', 'Pole & Pole Foundation')])
            if pole:
                for line in self.pole_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.pole_lines = pole_list

    @api.onchange('is_outdoor')
    def onchange_is_outdoor(self):
        pole_list = []
        if self.is_outdoor:
            pole = self.env['alarm.type'].search([('name', '=', 'Outdoor Closures')])
            if pole:
                for line in self.outdoor_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.outdoor_lines = pole_list

    @api.onchange('is_battery')
    def onchange_is_battery(self):
        pole_list = []
        if self.is_battery:
            pole = self.env['alarm.type'].search([('name', '=', 'Battery Closures')])
            if pole:
                for line in self.battery_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.battery_lines = pole_list

    @api.onchange('is_civil')
    def onchange_is_civil(self):
        pole_list = []
        if self.is_civil:
            pole = self.env['alarm.type'].search([('name', '=', 'Civil & Fiber Network')])
            if pole:
                for line in self.civil_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.civil_lines = pole_list

    @api.onchange('is_optical')
    def onchange_is_optical(self):
        pole_list = []
        if self.is_optical:
            pole = self.env['alarm.type'].search([('name', '=', 'Optical Testing: Fiber Optical Length Measurement')])
            if pole:
                for line in self.fibre_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.fibre_lines = pole_list

    @api.onchange('is_attenuation')
    def onchange_is_attenuation(self):
        pole_list = []
        if self.is_attenuation:
            pole = self.env['alarm.type'].search([('name', '=', 'Optical Testing: Attenuation Test')])
            if pole:
                for line in self.attenuation_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.attenuation_lines = pole_list

    @api.onchange('is_camera')
    def onchange_is_camera(self):
        pole_list = []
        if self.is_camera:
            pole = self.env['alarm.type'].search([('name', '=', 'Cameras')])
            if pole:
                for line in self.camera_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.camera_lines = pole_list

    @api.onchange('is_site')
    def onchange_is_site(self):
        pole_list = []
        if self.is_site:
            pole = self.env['alarm.type'].search([('name', '=', 'Site Power')])
            if pole:
                for line in self.site_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.site_lines = pole_list

    @api.onchange('is_wireless')
    def onchange_is_wireless(self):
        pole_list = []
        if self.is_wireless:
            pole = self.env['alarm.type'].search([('name', '=', 'Wireless System')])
            if pole:
                for line in self.wireless_lines:
                    line.unlink()
                for rec in pole.alarm_ids:
                    pole_list.append((0, 0, {
                        'site_ins': rec.name,
                    }))
        self.wireless_lines = pole_list


class Pole(models.Model):
    _name = 'pole.line'

    site_id = fields.Many2one('maintenance.equipment')
    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class OutDoor(models.Model):
    _name = 'outdoor.line'

    site_id = fields.Many2one('maintenance.equipment')
    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class Battery(models.Model):
    _name = 'battery.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class Civil(models.Model):
    _name = 'civil.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class Fibre(models.Model):
    _name = 'fibre.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class Attenuation(models.Model):
    _name = 'attenuation.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False

class Camera(models.Model):
    _name = 'camera.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False


class Site(models.Model):
    _name = 'site.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False

class Wireless(models.Model):
    _name = 'wireless.line'

    site_ins = fields.Char('Site Inspection')
    is_ok = fields.Boolean('Ok')
    is_not_ok = fields.Boolean('Not Ok')
    remarks = fields.Char('Remarks')
    site_id = fields.Many2one('maintenance.equipment')

    @api.onchange('is_ok')
    def onchange_is_ok(self):
        if self.is_ok:
            self.is_not_ok = False

    @api.onchange('is_not_ok')
    def onchange_is_not_ok(self):
        if self.is_not_ok:
            self.is_ok = False