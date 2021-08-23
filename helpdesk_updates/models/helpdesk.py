# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HelpdeskTicket(models.AbstractModel):
    _inherit = "helpdesk.ticket"

    maintenance_equipment_id = fields.Many2one('maintenance.equipment', string='Site Name')
    maintenance_equipment_category_id = fields.Many2one('maintenance.equipment.category', string='Site Type')

    @api.onchange('maintenance_equipment_category_id', 'maintenance_equipment_id')
    def change_maintenance_equipment_category_id(self):
        for record in self:
            if record.maintenance_equipment_category_id:
                maintenance_equipment_ids = self.env['maintenance.equipment'].\
                    search([('category_id.id', '=', record.maintenance_equipment_category_id.id)])
                maintenances = []
                for main in maintenance_equipment_ids:
                    maintenances.append(main.id)
                domain = {'maintenance_equipment_id': [('id', 'in', maintenances)]}
                return {'domain': domain}
