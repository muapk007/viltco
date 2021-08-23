
from odoo import models, fields, api, _


class AlarmType(models.Model):
    _name = 'site.type'

    name = fields.Char(string='Name')


class ContactName(models.Model):
    _name = 'contact.name'

    name = fields.Char(string='Name')
