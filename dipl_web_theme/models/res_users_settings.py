# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsersSettings(models.Model):
    _inherit = 'res.users.settings'

    color_scheme = fields.Selection(
        [("system", "System"), ("light", "Light"), ("dark", "Dark")],
        default="system",
        required=True,
        string="Color Scheme",
    )
    homemenu_config = fields.Json(string="Home Menu Configuration", readonly=True)
