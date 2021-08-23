# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class ProductInherit(models.Model):
    _inherit = 'product.template'

    ip_address = fields.Char(string='IP Address')
